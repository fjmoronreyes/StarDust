SHELL := /bin/bash
POETRY ?= poetry
VENV_DIR := .venv

MAKEFLAGS += --no-print-directory

.PHONY: setup

setup:
	@$(POETRY) config virtualenvs.in-project true --local
	@$(POETRY) config virtualenvs.create true --local
	@if [ -d "$(VENV_DIR)" ]; then \
		read -p "Virtualenv '$(VENV_DIR)' already exists. Reset it? [y/N]: " yn; \
		if [[ $$yn =~ ^[Yy]$$ ]]; then \
			echo "Removing $(VENV_DIR)..."; \
			rm -rf "$(VENV_DIR)"; \
		else \
			echo "Keeping existing $(VENV_DIR)."; \
		fi \
	fi
	@$(POETRY) install
	@echo ""
	@echo "Setup complete."
	@echo "Activate manually with:"
	@echo "  source $(VENV_DIR)/bin/activate"
	@echo "Then you can run commands with 'poetry run <command>'"