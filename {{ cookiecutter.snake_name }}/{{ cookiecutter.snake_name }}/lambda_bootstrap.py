# This file contains everything we want to run when initialising during
# a cold boot.
# The premise is, everything is loaded into memory, and cached at the end
# of the context.
# You usually want to initialise clients here, such as X-Ray, Boto, or Sentry.

import logging
import os

import aws_xray_sdk
import sentry_sdk
from aws_xray_sdk.core import patch_all as xray_patch_all
from aws_xray_sdk.core import xray_recorder
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


def init_all(**kwargs):
    init_sentry(**kwargs)
    init_xray(**kwargs)


def init_sentry(sentry_dsn=None, sentry_integrations=None, **_):
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[
            *(sentry_integrations or []),
            AwsLambdaIntegration(timeout_warning=True),
            LoggingIntegration(level=logging.DEBUG, event_level=logging.WARNING),
        ],
        environment=os.environ.get("APP_STAGE"),
    )


def init_xray(xray_service_name=None, xray_enabled=None, **_):
    if xray_enabled is None:
        xray_enabled = os.environ.get("XRAY_ENABLED", "") == "true"

    if xray_enabled:
        xray_service_name = (
            xray_service_name
            or f"{os.environ.get('APP_NAME')} - {os.environ.get('APP_STAGE')}"
        )
        xray_recorder.configure(service=xray_service_name)
        xray_patch_all()
    else:
        aws_xray_sdk.global_sdk_config.set_sdk_enabled(False)
