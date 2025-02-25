PY=python3

# Perform all checks and tests, then copy the main script to INSTALL_ROOT
install: fmt-check type-check test
	chmod +x {{ cookiecutter.main_name }}.py
	cp {{ cookiecutter.main_name }}.py $(INSTALL_ROOT)/

# Installation directory of the main script
# if in your PATH, then the main script will imediately be executable
# it should be an existing directory
INSTALL_ROOT=~/bin

# Check type-annotations soundness
type-check:
	$(PY) -m mypy *.py

# Run unit-test and cram tests
test:
	$(PY) -m unittest *.py
	$(PY) -m cram tests.t

# Update cram tests expectation with whatever the current output is
test-promote:
	$(PY) -m cram -i -y tests.t

# Format source code
fmt:
	-$(PY) -m black *.py
fmt-check: # Ensure source code is formatted
	$(PY) -m black *.py

# Install required dev dependencies
setup:
	$(PY) -m pip install -r requirements.txt

venv: .venv/bin/activate
	echo "Call 'source .venv/bin/activate" to activate virtual environment

.venv:
	$(PY) -m venv .venv

.venv/bin/activate: .venv # Handle bug https://stackoverflow.com/questions/41687841/there-is-no-activate-when-i-am-trying-to-run-my-virtual-env
	$(PY) -m venv .venv

.PHONY: fmt type-check test setup install

ifeq ($(OS), Windows_NT)
AWK_AVAILABLE=$(shell where /Q awk && echo yes)
INSTALL_AWK=echo Auto-generated help message requires 'awk', you can install awk from chocolatey: 'choco install awk'
else
AWK_AVAILABLE=$(shell which awk > /dev/null && echo yes)
INSTALL_AWK=echo "Auto-generated help message requires 'awk' $(AWK_AVAILABLE), you can install awk from your package manager, e.g. 'apt-get install awk'"
endif

# Prints this help message
help:
ifeq (yes, $(AWK_AVAILABLE))
	@awk '\
	/^##/{ print $$0; doc = 0; next }\
	/^#/{ if (doc != 1) { comments = $$0; doc = 1 } else { comments = comments "\n\t" $$0 } next }\
	/^([^=])+[=]/{ if (doc == 1) { print "(variable) " $$0 "\n\t" comments "\n"; doc = 0 } next }\
	/^([^:])+:/{ if (doc == 1) { print $$1 "\n\t" comments "\n"; doc = 0 } next }\
	/./{ doc = 0 }\
	' Makefile
else
	@$(INSTALL_AWK)
endif
