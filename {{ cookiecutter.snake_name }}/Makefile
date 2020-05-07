STAGE ?= dev
RUN_IN_PIPENV ?= true

pipenv = PIPENV_IGNORE_VIRTUALENVS=1 PIPENV_DEV=1 pipenv
ifeq ($(RUN_IN_PIPENV), true)
	run = $(pipenv) run --
else
	run =
endif

SRC_DIRS = {{ cookiecutter.snake_name }}
TEST_DIRS = tests

##@ bootup

.PHONY: install setup
install:  ## installs all your dependencies
install: python-install
setup: install

.PHONY: python-install
python-install:  ## Installs your python dependencies
	$(pipenv) clean
	$(pipenv) sync

.PHONY: install-deploy-deps
install-deploy-deps:  ## Installs dependencies for deploying
	npm install

.PHONY: upgrade
upgrade: ## updates all your dependencies (regenerates the lock files)
upgrade:
	$(pipenv) update

{%- if cookiecutter.is_web_app %}
##@ Execution

.PHONY: serve
serve:  ## Runs the server
serve:
	$(run) uvicorn {{ cookiecutter.snake_name }}.web.app:app --reload
{%- endif %}

##@ Code Checks

.PHONY: test
test: ## Runs all the tests
test:
	$(run) python -m pytest tests

.PHONY: fixlint autofix
fixlint: autofix
autofix: ## Attempts to rectify any linting issues
autofix:
	$(run) autoflake --in-place --remove-unused-variables --recursive $(SRC_DIRS) $(TEST_DIRS)
	$(run) isort --recursive $(SRC_DIRS) $(TEST_DIRS)
	$(run) black $(SRC_DIRS) $(TEST_DIRS)

.PHONY: lint
lint: ## Checks the code for any style violations
lint:
	$(run) autoflake --check --remove-unused-variables --recursive $(SRC_DIRS) $(TEST_DIRS)
	$(run) isort --check-only --recursive $(SRC_DIRS) $(TEST_DIRS)
	$(run) black --check $(SRC_DIRS) $(TEST_DIRS)

##@ Deployment

SLS = npm run sls --

.PHONY: deploy
deploy: ## Full Deploy to `STAGE`
deploy:
	$(SLS) deploy --stage '$(STAGE)'

.PHONY: code-deploy
code-deploy:  ## Code Only deploy to `STAGE`
code-deploy:
	$(SLS) deploy function --stage '$(STAGE)' --function main

{%- if cookiecutter.is_web_app %}
.PHONY: setup-domain
setup-domain:  # oneshot command for setting up a certificate and custom domain
setup-domain:
	$(SLS) --stage '$(STAGE)' create-cert
	$(SLS) --stage '$(STAGE)' create_domain
{%- endif %}

##@ Helpers

ifndef NO_COLOUR
  cyan = \033[36m
  bold = \033[1m
  reset = \033[0m
  target_style ?= $(cyan)
  header_style ?= $(bold)
endif

.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN { \
		FS = ":.*##"; \
		printf "\n"; \
		printf "$(header_style)Usage:$(reset)"; \
	    printf "\n"; \
		printf "  make $(target_style)<target>$(reset)"; \
		printf "\n"; \
	}; \
	/^[a-zA-Z_-]+:.*?##/ { \
		printf "  $(target_style)%-15s$(reset) %s", $$1, $$2; \
		printf "\n" \
	}; \
	/^##@/ { \
		printf "\n"; \
		printf "$(header_style)%s$(reset)", substr($$0, 5); \
		printf "\n"; \
	};' $(MAKEFILE_LIST)
