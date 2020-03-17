from mangum import Mangum
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from {{ cookiecutter.project_slug }} import lambda_boostrap

from .app import app

lambda_boostrap.init_all()

handler = Mangum(SentryAsgiMiddleware(app))
