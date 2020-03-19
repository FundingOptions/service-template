# {{ cookiecutter.project_name }}

{{ cookiecutter.project_name }} deals with ...

\# TODO: a brief overview.

This bird was raised by [The Hatchery][the-hatchery].
Please contribute changes upstream to help raise more birds!

## Set up

You will need [Pipenv][pipenv] for managing the python dependencies.
Follow the [install][pipenv-install] instructions, or just run:
```
pip install --user pipenv
```

A `Makefile` is used to make sure your dependencies are up to date:

`make install` will do everything you need.

## Linting

3 Linters have been set up to adhere to our style guidelines:
- isort
- black
- autoflake

You can check your changes by running `make lint` to get a report.

To fix any linting issues, run:
```sh
make fixlint
```

## Testing

Testing is as simple as running:

```
make test
```

This will run the pytest suite.
Note that there are 2 important plugins loaded as part of this:

- pytest-cov
  Generates a coverage report of the tests
- pytest-randomly
  Ensures that tests don't always run in the same order (prevents order dependent tests)

{%- if cookiecutter.is_web_app %}
## Running locally

For development purposes, `uvicorn` has been setup to run a local server.
The server will reload whenever you change a file, allowing for quickly checking behaviour.

run using:
```
make serve
```

### Configuring

Any configurations should go in via environment variables.
If you're using the `make` commands, or using `pipenv`, you can load up your variables
into a `.env` file.
{%- endif %}

## How to deploy

### Overview

{{ cookiecutter.project_name }} is deployed using [serverless][serverless].
At Funding Options, we use Serverless as it enables us to quickly spin up:
- WSGI/ASGI web applications (such as Flask, Django, Starlette)
- Event driven applications (SNS, Cloudwatch Alarms)

Serverless is based on CloudFormation, and includes an extensible plugin system. This allows
us to deploy lots of resources in a clean fashion, and through the use of SSM, allow plugging in variables
from our master Terraform configs for the infrastructure as a whole.

### Setup

You will need [node][node] installed on your system. We recommend using the latest LTS release.

First, you need to install the dependencies:

```sh
make install-deploy-deps
# OR
npm install
```

### Running

You should then be able to deploy using:

```sh
make deploy
```

It is recommended to use [`aws-vault`][aws-vault] for running this command. It:

- Stores your actual AWS credentials in your encrypted system keyring.
- Provides a way of rotating said credentials quickly and easily.
- Makes MFA easy, as it manages sessions for you (usually MFA needed very 6 hours).
- It never exposes your AWS Credentials to the software, and instead uses temporary tokens.

command with aws-vault:

```sh
aws-vault exec fo -- make deploy
```

### Different environments

By default, this deploys to the dev environment.

You can change environment by specifying the environment variable `STAGE`:

```sh
STAGE=prod aws-vault exec fo -- make deploy
```

[aws-vault]: https://github.com/99designs/aws-vault
[the-hatchery]: https://github.com/FundingOptions/hatchery
[serverless]: https://serverless.com/
[node]: https://nodejs.org/
[pipenv]: https://pipenv.kennethreitz.org/en/latest/
[pipenv-install]: https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv
