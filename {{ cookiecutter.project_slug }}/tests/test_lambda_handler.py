from {{ cookiecutter.project_slug }} import lambda_handler


def test_handler_says_hello_to_the_world():
    stub_event = {}
    stub_context = {}
    expected_result = {"hello": "World!"}

    result = lambda_handler(event=stub_event, context=stub_context)

    assert expected_result == result
