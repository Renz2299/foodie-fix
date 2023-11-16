import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "your_secret_key")
os.environ.setdefault("DEBUG", "True") # set to false when complete
os.environ.setdefault("DEVELOPMENT", "True") # set to false when complete
os.environ.setdefault("DB_URL", "postgresql:///db_name") # /// means local db, // means hosted db