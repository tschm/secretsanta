# 🎅 Secret Santa

[![CodeFactor](https://www.codefactor.io/repository/github/tschm/secretsanta/badge)](https://www.codefactor.io/repository/github/tschm/secretsanta)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/renovatebot/renovate)
[![Docker Test](https://github.com/tschm/secretsanta/actions/workflows/docker-test.yml/badge.svg)](https://github.com/tschm/secretsanta/actions/workflows/docker-test.yml)

## 🎁 About

A simple yet effective Secret Santa generator application built with Marimo.
This tool helps organize gift exchanges by randomly pairing
participants from two different groups.

## ✨ Features

- 🎯 Create random pairings between two groups
- 🔄 Shuffle names for truly random assignments
- 🖥️ Clean, interactive web interface
- 🚀 Easy to use with simple text input
- 📦 Modular design with the `pysanta` package

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.10+
- Marimo package (installed automatically via `pyproject.toml`)

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/tschm/secretsanta.git
cd secretsanta

# Install dependencies
make install
```

### 🎮 Running the Application

```bash
# Start the Marimo app
make app
```

## 📦 pysanta Package

The application is built around the `pysanta` package, which provides the core functionality:

- **process_names**: Processes a comma-separated string of names into a list
- **shuffle_names**: Shuffles a list of names for random assignments

The package is installed automatically when you run `make install` and
is also included in the Docker container.

### 🛠️ Development Setup

The project uses a `pyproject.toml` file for package configuration
and dependency management with `uv`. Development
dependencies are available as optional dependencies:

```bash
# Install development dependencies
uv pip install -e ".[dev]"
```

This will install:

- **pre-commit**: For code quality checks
- **pytest**: For running tests

## 🐳 Docker Support

```bash
# Build and run the Docker container
make build

# Test the Docker container
make test-docker
```

The Docker container is automatically tested on each push and pull request
using GitHub Actions. The tests verify that the container builds correctly,
starts up, and functions as expected.

## 🎄 How to Use

1. Enter comma-separated names for the first group
2. Enter comma-separated names for the second group
3. The app will automatically shuffle and display the results
4. Use these pairings for your Secret Santa gift exchange

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
