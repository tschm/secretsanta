# syntax=docker/dockerfile:1.16
# This enables the use of Docker's BuildKit frontend version 1.16,
# which provides advanced features and performance improvements

# Use a more specific Python slim image to reduce size
# The slim variant contains only essential packages, resulting in a smaller image size
FROM python:3.13-slim AS base

# Install uv for fast package management
# uv is a Python package installer that's significantly faster than pip
# We copy it from an official image rather than installing it to save time and reduce layers
COPY --from=ghcr.io/astral-sh/uv:0.7.9 /uv /bin/uv

# Set environment variables in one layer
# Combining multiple ENV commands into one reduces the number of layers in the final image
ENV PATH="/home/user/.local/bin:$PATH" \
    UV_SYSTEM_PYTHON=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Explanation of environment variables:
# - PATH: Adds user's local bin to the PATH to find executables installed with --user
# - UV_SYSTEM_PYTHON=1: Tells uv to use the system Python instead of creating a virtual environment
# - PYTHONUNBUFFERED=1: Prevents Python from buffering stdout/stderr (better for logging in containers)
# - PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files (reduces image size)
# - PIP_NO_CACHE_DIR=1: Prevents pip from using a cache directory (reduces image size)

# Create non-root user and chown the app directory
# Running as a non-root user is a security best practice for containers
# - useradd -m: Creates a user with a home directory
# - -u 1000: Sets the user ID to 1000 (standard for first non-root user)
# - mkdir /app: Creates the application directory
# - chown user:user /app: Gives the new user ownership of the app directory
RUN useradd -m -u 1000 user && mkdir /app && chown user:user /app

# Set working directory and switch to user early
# This sets the default directory for subsequent commands
WORKDIR /app

# Copy and install dependencies first for better caching
# Docker caches layers, so putting dependency installation before code copy
# means we don't reinstall dependencies when only the code changes
# Note: We use the 'user' account created earlier for file ownership
RUN uv pip install --no-cache-dir marimo==0.13.15

# Copy application code
# The main app.py file contains the Marimo application entry point
COPY --chown=user:user app.py app.py


FROM base as prod

# Switch to non-root user
# This is a security best practice to limit the potential damage if the container is compromised
USER user

# Add healthcheck
# This allows Docker to monitor the health of the container
# Parameters:
# - interval=30s: Check every 30 seconds
# - timeout=30s: Allow 30 seconds for the check to complete
# - start-period=5s: Give 5 seconds grace period on startup
# - retries=3: Fail after 3 consecutive failed checks
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Expose port
# This documents that the container listens on port 7860
# Note: This doesn't actually publish the port - that's done at runtime with -p flag
EXPOSE 7860

# Use exec form of ENTRYPOINT with CMD for proper signal handling
# The exec form is preferred as it doesn't start a shell, allowing signals to be passed correctly
ENTRYPOINT ["marimo"]
# The CMD provides default arguments to the ENTRYPOINT:
# - run: Runs the Marimo application
# - app.py: The main application file
# - --host 0.0.0.0: Binds to all network interfaces (required for container access)
# - --port 7860: The port the application listens on
CMD ["run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
