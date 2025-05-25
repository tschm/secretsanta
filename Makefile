# This file contains commands for setting up the environment, formatting code,
# building the book, and other maintenance tasks.

.DEFAULT_GOAL := help

# Create a virtual environment using uv
venv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv


# Mark install target as phony (not producing a file named 'install')
.PHONY: install
install: venv ## Install a virtual environment
	@uv pip install --upgrade pip
	@uv sync --dev --frozen  # Install dependencies from pyproject.toml with all extras


# Format and lint the code using pre-commit
.PHONY: fmt
fmt: venv ## Run autoformatting and linting
	@uv pip install --no-cache-dir -e ".[dev]"
	@uv run pre-commit install
	@uv run pre-commit run --all-files


# Clean up generated files and remove stale branches
.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f
	@git branch -v | grep "\[gone\]" | cut -f 3 -d ' ' | xargs git branch -D


# Display help information about available make targets
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort


# Install and run Marimo for interactive notebooks
.PHONY: marimo
marimo: install    ## Install Marimo
	@uv run marimo edit pysanta/app.py

# Run the Marimo application
.PHONY: app
app: install ## Run the Marimo app
	@uv run marimo run pysanta/app.py

# Run tests using pytest
.PHONY: test
test: install ## Run tests
	@uv pip install --no-cache-dir pytest
	@uv run pytest tests
