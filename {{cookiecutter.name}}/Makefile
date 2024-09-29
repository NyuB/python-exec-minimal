PY=python3
INSTALL_ROOT=~/bin

.PHONY: fmt type-check test setup install

install: fmt-check type-check test # Perform all checks then copy the main script to INSTALL_ROOT
	chmod +x {{ cookiecutter.main_name }}.py
	cp {{ cookiecutter.main_name }}.py $(INSTALL_ROOT)/

type-check: # Check type-annotations soundness
	$(PY) -m mypy *.py

test: # Run unit-test and cram tests
	$(PY) -m unittest *.py
	$(PY) -m cram tests.t

test-promote: # Update cram tests expectation with whatever the current output is
	$(PY) -m cram -i -y tests.t

fmt: # Format source code
	-$(PY) -m black *.py
fmt-check: # Ensure source code is formatted
	$(PY) -m black *.py

setup: # Install required dev dependencies
	$(PY) -m pip install -r requirements.txt

venv: .venv/bin/activate
	echo "Call 'source .venv/bin/activate" to activate virtual environment

.venv:
	$(PY) -m venv .venv

.venv/bin/activate: .venv # Handle bug https://stackoverflow.com/questions/41687841/there-is-no-activate-when-i-am-trying-to-run-my-virtual-env
	$(PY) -m venv .venv
