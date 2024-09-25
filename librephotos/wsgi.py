import os

from django.core.wsgi import get_wsgi_application

from .cli import prepare_cli

environment = "production"
if os.environ.get("DEBUG", "0") == "1":
    environment = "development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"librephotos.settings.{environment}")

prepare_cli()
application = get_wsgi_application()
