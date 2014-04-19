
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "c33a33ac-8513-466e-bdd2-91f66c807421f01ceef9-6b7f-4717-af35-8543e0192b323382cff4-d63e-4ab9-9adf-b0ab1ad1d2bb"
NEVERCACHE_KEY = "81401492-7436-4794-ac9a-f29f97479364c7d5c3f5-74be-4de9-b0e4-3d83d2045b078148b597-5033-415a-8f93-e83d4e572db2"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
