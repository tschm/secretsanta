# 🐳 Docker Support for Secret Santa

This directory contains Docker-related files for the Secret Santa application.

## 📄 Files

- `Dockerfile`: The main Dockerfile for building the Secret Santa application container
- `.dockerignore`: Specifies which files should be
  excluded from the Docker build context
- `test_docker.sh`: Shell script for testing the Docker container

## 🏗️ Building the Docker Image

You can build and run the Docker image using the `build` target in the Makefile:

```bash
make build
```

This will build the Docker image and run the container,
exposing the application on port 7860.

## 🧪 Testing the Docker Container

The Docker container can be tested using the `test-docker` target in the Makefile:

```bash
make test-docker
```

This will run the `test_docker.sh` script, which performs the following tests:

1. 🏗️ **Build Test**: Verifies that the Docker image builds successfully
2. 🚀 **Run Test**: Checks that the container starts correctly
3. 🌐 **HTTP Test**: Ensures the application is accessible on port 7860
4. 💓 **Health Check**: Verifies the container's health check is working
5. 👤 **User Test**: Confirms the container is running as the non-root user
6. 📦 **Marimo Test**: Checks that Marimo is installed correctly
7. 📦 **pysanta Test**: Verifies that the pysanta package is installed correctly

## 📦 pysanta Package

The Docker container includes the `pysanta` package, which provides the core
functionality for the Secret Santa application:

- **process_names**: Processes a comma-separated string of names into a list
- **shuffle_names**: Shuffles a list of names for random assignments

The package is installed in the Docker container during the
build process using the `pyproject.toml` file.

## 🔒 Security Features

The Docker container includes several security features:

- Runs as a non-root user (`user`)
- Uses a minimal base image (Python slim)
- Minimizes the number of layers to reduce attack surface
- Includes a health check to monitor container health

## 🛠️ Customization

You can customize the Docker build by modifying the following:

- Port mapping (default: 7860)
- Environment variables in the Dockerfile
- Build arguments (if needed)

Example of running with a different port:

```bash
docker run -it --rm -p 8080:7860 marimo-app
```

This will map the container's port 7860 to the host's port 8080.
