from itertools import groupby
import json
import os

from flask import Flask, render_template, request, redirect, Response
import sqlalchemy

from models import create_connection, init_db
from packages import register_package_creator, register_models
from config import CONFIGS

if os.environ.get("DATABASE_URL"):
    config = CONFIGS[os.environ.get("ENV", "PROD")]
else:
    config = CONFIGS[os.environ.get("ENV", "DEV")]

app = Flask(__name__,
            static_url_path='/static')


def set_db(config):
    Base, db_session, engine = create_connection(config)
    Package, InstallMethod = register_models(Base)
    init_db(Base, engine)
    return Base, db_session, Package, InstallMethod

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

@app.route("/.well-known/acme-challenge/2KNoLJFbdqcKw-kp7AdoMz7NIBMjphtVCCzvzWqXo9A")
@app.route("/.well-known/acme-challenge/2KNoLJFbdqcKw-kp7AdoMz7NIBMjphtVCCzvzWqXo9A:")
@app.route("/.well-known/acme-challenge/X5V7XUy6JIUkct_Z2-FpZMzi17kxCxM2UK1YXmr02xE")
@app.route("/.well-known/acme-challenge/X5V7XUy6JIUkct_Z2-FpZMzi17kxCxM2UK1YXmr02xE:")
def ahh():
    return "X5V7XUy6JIUkct_Z2-FpZMzi17kxCxM2UK1YXmr02xE.VSiiJ9vHj6AiQauI5ejezPFXlOrJl1sdqak6A0_ol7Q"

@app.route('/')
@app.route('/index')
def index():
    cont = True
    while cont:
        try:
            packages = Package.query.all()
            cont = False
        except:
            db_session.rollback()
            cont = True

    packages.sort(key=lambda p: p.category)
    packages = groupby(packages, lambda p: p.category)
    ua = request.headers.get('User-Agent')
    linux_ua = True
    if 'Linux' not in ua or 'X11' not in ua:
        linux_ua = False
    return render_template('index.html', packages=packages, linux_ua=linux_ua)

Base, db_session, Package, InstallMethod = set_db(config)
register_package_creator(app,
                         db_session,
                         Package, InstallMethod,
                         template_path="packages/templates")

if __name__ == "__main__":
  app.run(debug=True, port=5000)
