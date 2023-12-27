from .base import BASE_DIR, set_db

# ALLOWED_HOSTS = []

dotenv_path = BASE_DIR / ".test.env"
DATABASES = set_db(dotenv_path)