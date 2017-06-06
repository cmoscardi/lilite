from collections import defaultdict 

from flask import request, render_template, Response

def register_package_creator(app,
                             db_session,
                             Package,
                             InstallMethod,
                             template_path=None):

    @app.route("/get_installer", methods=["POST"])
    def get_installer():
        version = request.form.get('version')
        legal_methods = InstallMethod.ALLOWED_INSTALLERS_BY_VERSION[version]
        package_reqs = request.form.getlist("packages")
        packages_by_name = {p.name: p for p in Package.query.all()}
        methods_by_package = defaultdict(list)
        for m in InstallMethod.query.all():
          methods_by_package[m.package_id].append(m)
        final_methods = []
        for req in package_reqs:
          package = packages_by_name[req]
          methods = [m for m in methods_by_package[package.id] if m.method_type in legal_methods]
          if methods:
            final_methods.append((package.name, methods[0]))


        standard = []
        weird = []
        for name, method in final_methods:
          if (not method.pre_install) and (not method.post_install):
            standard.append(method.package_name)
          else:
            weird.append((method.pre_install, method.package_name, method.post_install))
        path = "script.sh" if not template_path\
                           else template_path + "/script.sh"
        resp= render_template(path, standard=standard, weird=weird)
        return Response(resp, mimetype="text")
