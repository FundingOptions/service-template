# The Hatchery

Hatchery provides a [Cookiecutter][cookiecutter] template for quickly generating base projects.

_Note_: This is relatively new and untested. Bolivian Tree Lizards may reside here.

## Usage

- [Install Cookiecutter][cookiecutter-install]
- Run `cookiecutter git+ssh://git@github.com/FundingOptions/hatchery.git`
- Fill in your project details

## What is included here

This currently provides a thin template for Python projects, and makes minimal assumptions as for the
type of project you will be making.

That is to say, it does not generate a Django, Flask, or `<insert-framework/>` project. It's about
generating our base config files, dependency management, and task runner.

At a later point, we may add framework generation.

### Frontend

Sorry, nothing here yet.
It might be you want to look into something `node` specific, so we've not imposed anything for you here.

### Testing

#### Pytest

Our testing tool of choice, it's quicker to craft, and the fixture support is incredibly powerful.
Also looks much cleaner than `unittest`.

#### pytest-cov

Coverage support for `pytest`. Best used as an indicator that you have untested code.
**Always remember that covered code doesn't mean it's tested**

#### pytest-randomly

Generates seeds for Python's `random` module, `faker`, and also forces tests to run in different orders each time.

- This helps ensure that each test run is unique, but repeatable (`--randomly-seed`).
- By having tests run in different orders, we expose issues such as one test setting data in a database, and another depending on it being there. This helps avoid flakey tests earlier on in development.

#### Faker

Instead of using static data repeated everywhere, try to use generated data as much as possible.

This will:
- prevent "slimey" implementations, where your implementation isn't flexible enough in the real world
- force more code into fixtures, which thins out your actual test code

A pytest fixture has been configured for you.

### Linting

#### black

[The uncompromising formatter][black].
This takes `PEP8`, applies some opinions onto it, then just formats your code. Safely.

This was selected as "It Just Works", and is relatively stable. It's also been adopted by the PSF

#### autoflake

Remove all our unused variables + imports, to keep things a bit cleaner and less dead.

#### isort

Sorts our imports in accordance with the `black` standards. Who doesn't want alphabetised imports.

### Task runner

#### GNU Make

`make` has been selected as it's ubiquitously installed by default amongst most Operating Systems (Sorry Windows).

Whilest it's not the easiest system to work with, it does allow us to quickly write repeated commands, though
without the option for having parameters.

a `make help` has also been written to allow us to write CLI docs for our `make` targets, even if it is a little hacky.

### Configs

#### .gitignore

a `.gitignore` file is generated by the [gitignore.io][gitignore.io] service.

This service is continually updated with the latest tools + languages, and provides an excellent base to work from.

#### .editorconfig

a [`.editorconfig`][editorconfig] is added, with some useful defaults.
What this amounts to is:

- forces `utf-8` for all files
- forces all files to use `lf` as the line ending (great as we're a multi-OS team)
- ensures we always have a new line at end of files
- trims any trailing whitespace
- sets indenting to 4 spaces
  - Makefiles use tabs with a width of 4 spaces
  - Terraform files use 2 space indentation to align with `terraform fmt`

These enforcements are subject to using an editor with `.editorconfig` support.
See [here][editorconfig-plugins] to see if your editor is supported.

#### .circleci/config.yml

A generic workflow has been created, that Tests, Lints, and deploys your code.

CircleCI was chosen as it's easy to setup, and doesn't require us to self-host.

### Future

#### Frameworks

With an increased focus on Micro-services, it'd make sense to set up support for Flask, Chalice, or `<insert-framework/>`.

Once we've settled on a structure for each framework, we can look at integrating it into the Hatchery.

#### Tools

Some tools that I'd like to look into going forward:
- mypy, for static type checking in Python
- hypothesis, For a bit more structure on fuzzy testing
- ptyest-bdd, for writing User Stories as Tests
- pre-commit, for integrating Git Hooks
- Github Actions, For setting up Repo actions when hosted


[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest/
[cookiecutter-install]: https://cookiecutter.readthedocs.io/en/latest/installation.html
[black]: https://github.com/psf/black
[gitignore.io]: https://gitignore.io/
[editorconfig]: https://editorconfig.org/
[editorconfig-plugins]: https://editorconfig.org/#download
