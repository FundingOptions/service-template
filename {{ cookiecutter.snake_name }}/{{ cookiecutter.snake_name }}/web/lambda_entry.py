from mangum import Mangum
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from {{ cookiecutter.snake_name }} import lambda_boostrap

from .app import app

lambda_boostrap.init_all()

handler = Mangum(SentryAsgiMiddleware(app))
