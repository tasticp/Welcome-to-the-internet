# Multi-stage build for development container
FROM python:3.11-slim as base

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    nodejs \
    npm \
    sqlite3 \
    postgresql-client \
    redis-tools \
    watchdog \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install Node.js tools globally
RUN npm install -g \
    markdown-it \
    markdown-it-cli \
    live-server \
    http-server \
    nodemon \
    pm2

# Create app user
RUN useradd -m -u 1000 appuser && \
    mkdir -p /workspace && \
    chown -R appuser:appuser /workspace

# Set working directory
WORKDIR /workspace

# Copy development scripts
COPY .devcontainer/scripts/ /usr/local/bin/
RUN chmod +x /usr/local/bin/*.sh

# Install additional Python tools for development
RUN pip install --no-cache-dir \
    watchdog \
    python-frontmatter \
    jinja2 \
    pyyaml \
    black \
    isort \
    flake8 \
    mypy \
    pytest \
    pre-commit

# Install additional Node.js tools
RUN npm install -g \
    @vscode/vsce \
    typescript \
    ts-node \
    concurrently

# Development stage
FROM base as development

# Switch to app user
USER appuser

# Set environment variables
ENV PATH="/usr/local/bin:${PATH}"
ENV PYTHONPATH="/workspace"
ENV NODE_ENV=development
ENV PYTHONUNBUFFERED=1

# Expose ports
EXPOSE 8000 3000 5000 6000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 -c "import requests; requests.get('http://localhost:8000')" || exit 1

# Start development environment
CMD ["/usr/local/bin/start.sh"]