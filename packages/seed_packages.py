from collections import defaultdict
import json
import os
import subprocess

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models import register_models

def load_json():
  try:
    os.chdir("packages")
    sub = True
  except:
    sub = False

  with open("packages.json") as json_f:
    packages = json.load(json_f)

  if sub:
    os.chdir("..")

  return packages

def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()
    Package, InstallMethod = register_models(Base)
    Base.metadata.create_all(bind=engine)
    return db_session, Package, InstallMethod

def convert_icons():
  os.chdir("static/images")
  subprocess.check_call("./convert.sh")
  os.chdir("../..")

def print_stderr(s):
  import sys
  print >>sys.stderr, s

def parse_packages(package_list, db_session, Package, InstallMethod):
  packages = db_session.query(Package).delete()
  install_methods = db_session.query(InstallMethod).delete()
  try:
    db_session.commit()
  except Exception as e:
    print_stderr("FAILED!")
    print_stderr(str(e))
    db_session.rollback()

  print_stderr( "======" * 3)
  print_stderr( "deleting {} packages".format(packages))
  print_stderr( "deleting {} install_methods".format(install_methods))
  print_stderr( "======" * 3)
  methods_by_package = defaultdict(list)

  for p in package_list:
    p_obj = Package(name=p['name'],
                    description=p['description'],
                    icon_url=p['icon_url'],
                    category=p['category'])
    methods = []
    for t, c in p['installers'].iteritems():
      m = InstallMethod(method_type=t,
                        pre_install="\n".join(c['pre_install']),
                        package_name=c['package_name'],
                        post_install="\n".join(c['post_install']))
      m.package = p_obj
      methods.append(m)
    db_session.add(p_obj)
    [db_session.add(m) for m in methods]
    db_session.commit()

def main(db_session, Package, InstallMethod):
  j = load_json()
  parse_packages(j, db_session, Package, InstallMethod)

if __name__ == "__main__":
  import sys
  if len(sys.argv) > 1:
    uri = sys.argv[1]
  else:
    uri = 'sqlite:///test.db'
  db_session, Package, InstallMethod = init_db(uri)
  main(db_session, Package, InstallMethod)
