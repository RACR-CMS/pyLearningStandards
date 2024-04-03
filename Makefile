LICENSE=LICENSE
LICENSE_HEADER=LICENSE_HEADER
VENV=.venv
$(VENV):
	$(MAKE) install

.PHONY: clean
clean:
	rm -rf .venv

.PHONY: deps-show
deps-show:
	poetry show

.PHONY: deps-show
deps-show-outdated:
	poetry show --outdated

.PHONY: deps-update
deps-update:
	poetry update

.PHONY: docker-build
docker-build:
	cd racr_plugin_framework && $(MAKE) docker-build
	cd racr_plugin_framework_api && $(MAKE) docker-build

.PHONY: install
install: poetry-ensure-installed
	poetry config --local virtualenvs.in-project true
	poetry env use python3.8
	poetry install

.PHONY: format
format: $(VENV)
	poetry run black .

LICENSE:
	@echo "you must have a LICENSE file" 1>&2
	exit 1

LICENSE_HEADER:
	@echo "you must have a LICENSE_HEADER file" 1>&2
	exit 1

.PHONY: license
license: LICENSE LICENSE_HEADER $(VENV)
	poetry run python -m licenseheaders -t LICENSE_HEADER -d py_learning_standards/ $(args)
	poetry run python -m licenseheaders -t LICENSE_HEADER -d tools $(args)

.PHONY: poetry-ensure-installed
poetry-ensure-installed:
	sh ./tools/poetry_ensure_installed.sh

.PHONY: test
test:
	cd racr_plugin_framework && $(MAKE) test
	cd racr_plugin_framework_api && $(MAKE) test

.PHONY: test-not-slow
test-not-slow:
	cd racr_plugin_framework && $(MAKE) test-not-slow
	cd racr_plugin_framework_api && $(MAKE) test-not-slow

.PHONY: test-all
test-all:
	cd racr_plugin_framework && $(MAKE) test-all
	cd racr_plugin_framework_api && $(MAKE) test-all

.PHONY: test-all-not-slow
test-all-not-slow:
	cd racr_plugin_framework && $(MAKE) test-all-not-slow
	cd racr_plugin_framework_api && $(MAKE) test-all-not-slow

.PHONY: test-format
test-format: $(VENV)
	poetry run black --check .

.PHONY: test-lint
test-lint: $(VENV)
	poetry run flake8 ./py_learning_standards

.PHONY: test-license
test-license: LICENSE LICENSE_HEADER
	args="--check" $(MAKE) license

.PHONY: test-types
test-types: $(VENV)
	poetry run mypy py_learning_standards
