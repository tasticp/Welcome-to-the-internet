#!/bin/bash
# Development Container Setup Script

echo "🚀 Setting up Welcome to Internet development environment..."

# Create necessary directories
mkdir -p /workspace/.vscode
mkdir -p /workspace/logs
mkdir -p /workspace/temp
mkdir -p /workspace/.git

# Set up Python environment
echo "🐍 Setting up Python environment..."
python3 -m pip install --upgrade pip
pip install -r /workspace/requirements.txt

# Create package.json if it doesn't exist
if [ ! -f "/workspace/package.json" ]; then
    echo "📦 Creating package.json for development tools..."
    cat > /workspace/package.json << 'EOF'
{
  "name": "welcome-to-the-internet-dev",
  "version": "1.0.0",
  "description": "Development environment for Welcome to Internet project",
  "main": "index.html",
  "scripts": {
    "dev": "make dev-serve",
    "build": "make build",
    "validate": "make validate",
    "test": "make test"
  },
  "devDependencies": {
    "http-server": "^14.1.1",
    "live-server": "^1.2.1",
    "nodemon": "^3.0.1",
    "concurrently": "^8.2.0"
  },
  "devDependenciesMeta": {
    "npm": "9.6.7",
    "node": "18.17.0"
  }
}
EOF
fi

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
cd /workspace
npm install

# Set up git configuration
echo "🔧 Setting up Git configuration..."
git config --global user.name "DevContainer User"
git config --global user.email "devcontainer@example.com"

# Set up environment variables
export NODE_ENV=development
export PYTHONPATH=/workspace
export EDITOR=code

# Create development configuration
echo "⚙️ Creating development configuration..."
cat > /workspace/.vscode/settings.json << 'EOF'
{
  "python.pythonPath": "/usr/local/bin/python3",
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "files.associations": {
    "*.md": "markdown",
    "*.yml": "yaml",
    "Makefile": "makefile"
  },
  "editor.formatOnSave": true,
  "markdownlint.config": "/workspace/.markdownlint.json"
}
EOF

# Set up pre-commit hooks
echo "🔗 Setting up pre-commit hooks..."
cat > /workspace/.pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: check-added-large-files
        args: ['--maxkb=1000']

  - repo: https://github.com/psf/black
    rev: 22.12.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/igorshubovych/pre-commit-markdown
    rev: v0.4.0
    hooks:
      - id: markdownlint
        args: [--config=.markdownlint.json]
EOF

# Install pre-commit if not already installed
if ! command -v pre-commit &> /dev/null; then
    echo "📦 Installing pre-commit..."
    pip install pre-commit
fi

# Initialize pre-commit
pre-commit install --config /workspace/.pre-commit-config.yaml

# Set up development database
echo "🗄️ Setting up development database..."
mkdir -p /workspace/data
sqlite3 /workspace/data/dev.db << 'EOF'
CREATE TABLE IF NOT EXISTS content_updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    file_path TEXT NOT NULL,
    change_type TEXT NOT NULL,
    commit_hash TEXT
);

CREATE TABLE IF NOT EXISTS development_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    log_level TEXT NOT NULL,
    message TEXT NOT NULL,
    details TEXT
);

CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    test_name TEXT NOT NULL,
    status TEXT NOT NULL,
    duration_ms INTEGER,
    details TEXT
);
EOF

echo "✅ Development environment setup complete!"
echo ""
echo "🎯 Available Commands:"
echo "  make help      - Show all available commands"
echo "  make test      - Run all tests"
echo "  make validate  - Validate documentation"
echo "  make serve     - Start local development server"
echo "  make build     - Build documentation"
echo "  make deploy    - Deploy to staging"
echo ""
echo "🌐 Development servers will be available on:"
echo "  - Documentation: http://localhost:8000"
echo "  - Interactive features: http://localhost:3000"
echo "  - API: http://localhost:5000"
echo ""
echo "🚀 Happy coding!"