from . import lambda_bootstrap

lambda_bootstrap.init_all()


def handler(event, context):
    return {"hello", "World!"}
