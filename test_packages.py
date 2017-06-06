import os
from flask import Flask
from flask.testing import FlaskClient

from models import register_models
from package_endpoint import register_package_creator
import seed_packages as sp



def main():
    sp.main()
    packages = [p['name'] for p in sp.load_json()]
    app, client = create_app_client()

    version = os.environ.get("INSTANCE").split(":")[0]
    form = {"version": version,
            "packages": packages}
    resp, code, headers = client.post("/get_installer", data=form)
    assert code == "200 OK"
    resp = "\n".join(resp)
    with open("test_script.sh", "w+") as test_f:
        test_f.write(resp) 
 
def create_app_client():
    db_session, Package, InstallMethod = sp.init_db()
    app = Flask(__name__)
    client = FlaskClient(app)
    register_package_creator(app,
                             db_session,
                             Package,
                             InstallMethod)
    return app, client

if __name__ == "__main__":
    main()
