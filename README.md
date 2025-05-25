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

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.10+
- Marimo package (see `requirements.txt`)

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
