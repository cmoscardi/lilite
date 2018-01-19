import os

prod_uri = os.environ.get("DATABASE_URL", "")
PROD_CONFIG = {
  "DB_URI": prod_uri
}

DEV_CONFIG = {
  "DB_URI": "sqlite:///test.db"
}


CONFIGS = {
  "PROD": PROD_CONFIG,
  "DEV": DEV_CONFIG
}

assert PROD_CONFIG.keys() == DEV_CONFIG.keys()
