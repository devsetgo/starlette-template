# Makefile for Python project

# Set the name of the virtualenv directory
VENV_NAME = _venv

# Set the Python version to use in the virtualenv
PYTHON_VERSION = 3.10.6

# Set the name of the requirements file
REQUIREMENTS_FILE = requirements.txt

# Define the default target (what gets run when you type "make" with no arguments)
.PHONY: all
all: $(VENV_NAME)/bin/activate

# Define the target for the virtualenv
$(VENV_NAME)/bin/activate: src/requirements.txt
	python3 -m venv $(VENV_NAME)
	touch source $(VENV_NAME)/bin/activate
# $(VENV_NAME)/bin/pip install --upgrade pip
# $(VENV_NAME)/bin/pip install -r $(REQUIREMENTS_FILE)
# touch $(VENV_NAME)/bin/activate

# Define a clean target to remove the virtualenv
.PHONY: clean
clean:
	rm -rf $(VENV_NAME)
