# Makefile for Welcome to the Internet Documentation

.PHONY: help test lint format build deploy clean validate install serve stats update

# Default target
help:
	@echo "📚 Welcome to the Internet - Development Tools"
	@echo ""
	@echo "Available commands:"
	@echo "  help     - Show this help message"
	@echo "  test     - Run all tests and validations"
	@echo "  lint     - Check code quality and formatting"
	@echo "  format   - Format all markdown files"
	@echo "  build    - Build static site for deployment"
	@echo "  deploy   - Deploy to GitHub Pages"
	@echo "  validate - Validate all links and content"
	@echo "  clean    - Clean build artifacts"
	@echo "  serve    - Serve documentation locally"
	@echo "  install  - Install dependencies"
	@echo "  stats    - Generate repository statistics"
	@echo "  update   - Update content with automated tools"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install requests beautifulsoup4 markdownify feedparser pyyaml jinja2 python-frontmatter click rich
	@echo "✅ Dependencies installed"

# Test suite
test:
	@echo "🧪 Running tests..."
	python3 scripts/content-validator.py
	@echo "✅ All tests completed"

# Linting
lint:
	@echo "🔍 Linting markdown files..."
	@if command -v npx >/dev/null 2>&1; then \
		npx markdownlint-cli2 "**/*.md" || true; \
	else \
		echo "⚠️ npx not found. Install Node.js for markdown linting."; \
	fi
	@echo "✅ Linting completed"

# Validation
validate:
	@echo "🔍 Validating content..."
	python3 scripts/content-validator.py
	python3 scripts/trend-analyzer.py
	@echo "✅ Validation completed"

# Format markdown files
format:
	@echo "📝 Formatting markdown files..."
	@if command -v npx >/dev/null 2>&1; then \
		npx prettier --write "**/*.md" || true; \
	fi
	@echo "✅ Formatting completed"

# Generate statistics
stats:
	@echo "📊 Generating statistics..."
	@echo "Documentation files: $$(find docs -name '*.md' | wc -l)"
	@echo "Total lines: $$(wc -l docs/**/*.md 2>/dev/null | tail -1 | awk '{print $$1}' || echo 'N/A')"
	@echo "Platform analyses: $$(find docs/platforms -name '*.md' | grep -v README | wc -l)"
	@echo "Cultural topics: $$(find docs/culture -name '*.md' | grep -v README | wc -l)"
	python3 scripts/trend-analyzer.py
	@echo "✅ Statistics generated"

# Build static site
build:
	@echo "🏗️ Building static site..."
	mkdir -p dist
	cp -r docs/* dist/
	cp README.md dist/
	cp LICENSE dist/
	cp CONTRIBUTING.md dist/
	@echo "✅ Build completed"

# Serve documentation locally
serve:
	@echo "🌐 Serving documentation locally..."
	@cd docs && python3 -m http.server 8000
	@echo "✅ Serving at http://localhost:8000"

# Update content with automated tools
update:
	@echo "🔄 Updating content..."
	python3 scripts/trend-analyzer.py
	python3 scripts/content-validator.py
	@echo "✅ Content updated"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning..."
	rm -rf dist/
	rm -f *.json *.log
	@echo "✅ Clean completed"

# Deploy to GitHub Pages (if gh-pages is available)
deploy: build validate
	@echo "🚀 Ready for deployment"
	@echo "📝 Deployment would be handled by GitHub Actions"
	@echo "✅ Build validated and ready"

# Full workflow
all: install validate test build
	@echo "🎯 Complete workflow finished"

# Development workflow
dev: install validate serve
	@echo "🔧 Development environment ready"

# DevContainer workflow
devcontainer:
	@echo "🐳 Setting up development container..."
	@if command -v code >/dev/null 2>&1; then \
		echo "✅ VS Code found - opening DevContainer..."; \
		code --workspace-folder . --new-window; \
	else \
		echo "⚠️ VS Code not found - install from https://code.visualstudio.com/"; \
	fi

# Development server in container
dev-serve:
	@echo "🌐 Starting development servers in container..."
	docker-compose -f docker-compose.yml up --build

# Development shell in container
dev-shell:
	@echo "🐚 Opening shell in development container..."
	docker-compose -f docker-compose.yml exec app bash

# Development logs
dev-logs:
	@echo "📊 Showing development logs..."
	docker-compose -f docker-compose.yml logs -f

# Development status
dev-status:
	@echo "🔍 Checking development container status..."
	docker-compose -f docker-compose.yml ps

# Clean development environment
dev-clean:
	@echo "🧹 Cleaning development environment..."
	docker-compose -f docker-compose.yml down -v
	docker system prune -f

# Production workflow
prod: validate build
	@echo "🚀 Production build ready"