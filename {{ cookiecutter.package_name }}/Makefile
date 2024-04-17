PACKAGE := {{ cookiecutter.package_name }}
PACKAGE_DIR := src/${PACKAGE}
MODULES := $(wildcard $(PACKAGE_DIR)/*.py)

# MAIN TASKS ##################################################################

.PHONY: all
all: doctor format check test ## Run all tasks that determine CI status

.PHONY: dev
dev: install  ## Continuously run all CI tasks when files chanage
	rye run ptw

.PHONY: ipython
ipython: install
	rye run ipython --ipython-dir=notebooks --profile-dir=notebooks/.ipython_profile

.PHONY: demo
demo: install
	rye run nbstripout notebooks/demos/*.ipynb 2>/dev/null || true
	rye run jupyter notebook --ServerApp.root_dir=notebooks --ServerApp.preferred_dir=notebooks/demos

.PHONY: notebook
notebook: install
	rye run jupyter notebook --ServerApp.root_dir=notebooks

# SYSTEM DEPENDENCIES #########################################################

.PHONY: bootstrap
bootstrap: ## Attempt to install system dependencies
	asdf plugin add rye || asdf plugin update rye
	asdf install

.PHONY: doctor
doctor: ## Confirm system dependencies are available
	bin/verchew

# PROJECT DEPENDENCIES ########################################################

VIRTUAL_ENV ?= .venv
DEPENDENCIES := $(VIRTUAL_ENV)/.deps-$(shell bin/checksum pyproject.toml requirements.lock requirements-dev.lock)

.PHONY: install
install: $(DEPENDENCIES) .cache ## Install project dependencies

$(DEPENDENCIES): requirements.lock requirements-dev.lock
	@ rm -rf $(VIRTUAL_ENV)/.deps-*
	rye sync --features test
	@ touch $@

requirements.lock requirements-dev.lock: pyproject.toml
	rye lock
	@ touch $@

.cache:
	@ mkdir -p .cache

# CHECKS ######################################################################

.PHONY: format
format: install
	@ echo
	@ echo '#### RUFF'
	rye run ruff check ${PACKAGE_DIR} tests
	@ echo
	@ echo '#### BLACK'
	rye run black $(PACKAGE_DIR) tests
	@ echo

.PHONY: check
check: install  ## Run formaters, linters, and static analysis
	@ echo
	@ echo '#### MYPY'
	rye run mypy ${PACKAGE_DIR}
	@ echo
	@ echo '#### DEPTRY'
	rye run deptry --config pyproject.toml ${PACKAGE_DIR} tests
	@ echo
	@ echo '#### RUFF'
	rye run ruff check --output-format=full --no-fix
	@ echo
	@ echo '#### BLACK'
	rye run black $(PACKAGE_DIR) tests --diff

# TESTS #######################################################################

.PHONY: test
test: install  ## Run unit and integration tests
	rye run pytest --random --doctest-modules

.PHONY: test-repeat
test-repeat: install
	rye run pytest --count=5 --random --doctest-modules --exitfirst

# RELEASE #####################################################################

# DIST_FILES := dist/*.tar.gz dist/*.whl

# .PHONY: dist
# dist: install $(DIST_FILES)
# $(DIST_FILES): $(MODULES) pyproject.toml
# 	rm -f $(DIST_FILES)
# 	poetry build

# .PHONY: upload
# upload: dist  ## Upload the current version to PyPI
# 	git diff --name-only --exit-code
# 	poetry publish
# 	bin/open https://pypi.org/project/$(PACKAGE)

# CLEANUP #####################################################################

.PHONY: clean
clean:  ## Delete all generated and temporary files
	rm -rf .venv

# HELP ########################################################################

.PHONY: help
help: install
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help