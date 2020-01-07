# This file contains everything we want to run when initialising during
# a cold boot.
# The premise is, everything is loaded into memory, and cached at the end
# of the context.
# You usually want to initialise clients here, such as X-Ray, Boto, or Sentry.

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all as xray_patch_all


def init_all(**kwargs):
    init_sentry(**kwargs)
    init_xray(**kwargs)


def init_sentry(sentry_dsn=None, sentry_integrations=None, **_):
    sentry_sdk.init(
        sentry_sdk=sentry_dsn,
        integrations=[AwsLambdaIntegration(), *(sentry_integrations or [])],
        environment=os.environ.get("APP_STAGE"),
    )


def init_xray(xray_service_name=None, **_):
    xray_service_name = xray_service_name or f"{os.environ.get("APP_NAME")} - {os.environ.get("APP_STAGE")}"
    xray_recorder.configure(service=xray_service_name)
    xray_patch_all()
