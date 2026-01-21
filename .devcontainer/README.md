# 🐳 DevContainer Environment

<div align="center">

**Professional Development Environment** 🚀

*Isolated workspace that won't affect your main computer* 🔒

</div>

---

## 🎯 Overview

The **DevContainer** provides a complete, isolated development environment with all tools, dependencies, and services pre-configured for contributing to the **Welcome to the Internet** project.

---

## 🛠️ Included Components

### **🐧 Core Development Tools**
- **Python 3.11** with all dependencies pre-installed
- **Node.js 18** with npm and build tools
- **Git** with pre-commit hooks configured
- **VS Code** with curated extensions for development

### **📊 Development Services**
- **PostgreSQL Database** for data persistence
- **Redis Cache** for performance optimization
- **Nginx Reverse Proxy** for multi-service routing
- **SQLite** for local development data

### **🔧 Automation Tools**
- **Pre-commit hooks** for code quality
- **File watchers** for auto-reloading
- **Development logging** and monitoring
- **Database migration** tools

---

## 🚀 Quick Start

### **Option 1: VS Code (Recommended)**
```bash
# Open in DevContainer
make devcontainer
```

### **Option 2: Command Line**
```bash
# Start development environment
make dev-serve

# Open shell in container
make dev-shell

# View logs
make dev-logs

# Check status
make dev-status
```

### **Option 3: Manual Docker**
```bash
# Build and start containers
docker-compose -f docker-compose.yml up --build

# Run commands in container
docker-compose -f docker-compose.yml exec app bash
```

---

## 🌐 Available Services

### **Development Servers**
| Service | URL | Description |
|---------|-----|-----------|
| **Documentation** | http://localhost:8000 | Live documentation server |
| **Interactive Features** | http://localhost:3000 | Search, trends, analytics |
| **API Server** | http://localhost:5000 | REST API endpoints |
| **Analytics Dashboard** | http://localhost:6000 | Real-time metrics |
| **Nginx Gateway** | http://localhost:80 | Load balancer |

### **Database Services**
| Service | Port | Connection String |
|---------|------|------------------|
| **PostgreSQL** | 5432 | `postgresql://brainrot_user:brainrot_password@localhost:5432/brainrot_dev` |
| **Redis** | 6379 | `redis://localhost:6379` |
| **SQLite** | N/A | `/workspace/data/dev.db` |

---

## 🔧 Development Workflow

### **📝 Making Changes**
1. **Edit files** in VS Code with auto-formatting
2. **See live changes** via file watcher
3. **Automatic validation** runs on save
4. **Pre-commit hooks** ensure code quality

### **🧪 Testing**
```bash
# Run all tests
make test

# Run specific test suites
make validate          # Content validation
make lint              # Code quality checks
make format            # Auto-formatting
```

### **📚 Local Development**
```bash
# Serve documentation locally
make serve

# Build static site
make build

# Generate statistics
make stats
```

---

## 🎨 VS Code Extensions

### **🐍 Python Development**
- **Python** - IntelliSense, debugging, testing
- **Pylance** - Type checking and autocompletion
- **Black Formatter** - Code formatting
- **isort** - Import organization

### **📝 Markdown & Documentation**
- **Markdown All in One** - Comprehensive markdown editing
- **Markdown Preview** - Live preview with GitHub styles
- **MarkdownLint** - Real-time validation
- **Spell Checker** - Grammar and spelling

### **🔧 Development Tools**
- **GitHub Copilot** - AI-powered coding assistance
- **GitLens** - Enhanced Git capabilities
- **Docker** - Container management
- **YAML Support** - Configuration file editing

---

## 🗄️ File Structure in DevContainer

```
/workspace/                          # Main workspace
├── docs/                           # Documentation files
├── scripts/                         # Automation scripts
├── .git/                            # Git repository
├── .vscode/                         # VS Code settings
├── .devcontainer/                    # Container configuration
├── data/                            # Development database
├── logs/                            # Development logs
├── temp/                            # Temporary files
└── node_modules/                      # Node.js dependencies
```

---

## 🔄 Environment Variables

### **🐍 Python Environment**
```bash
PYTHONPATH=/workspace                # Python path
PYTHONUNBUFFERED=1               # Unbuffered output
VIRTUAL_ENV=/workspace              # Virtual environment
```

### **📦 Node.js Environment**
```bash
NODE_ENV=development              # Development mode
PATH=/usr/local/bin:$PATH        # Enhanced PATH
```

### **🔧 Development Configuration**
```bash
GIT_AUTHOR_NAME="DevContainer User"     # Git author
GIT_AUTHOR_EMAIL="devcontainer@example.com"  # Git email
EDITOR=code                      # Default editor
```

---

## 🎯 Development Commands

### **🐚 Container Management**
```bash
# Start development environment
make dev-serve

# Stop development environment
make dev-clean

# Restart services
make dev-down && make dev-serve

# View logs
make dev-logs
```

### **🔍 Development Tools**
```bash
# Install new dependencies
pip install package-name
npm install package-name

# Run database migrations
python scripts/migrate.py

# Generate development data
python scripts/seed.py
```

### **📊 Monitoring**
```bash
# Check service health
curl http://localhost/health

# View database status
sqlite3 /workspace/data/dev.db ".tables"

# Monitor logs
tail -f /workspace/logs/dev-session.log
```

---

## 🚨 Troubleshooting

### **🔧 Common Issues**

**Port Conflicts:**
```bash
# Check what's using ports
netstat -tulpn | grep :8000
netstat -tulpn | grep :3000

# Kill conflicting processes
sudo kill -9 <PID>
```

**Permission Issues:**
```bash
# Fix file permissions
chmod +x scripts/*.sh
sudo chown -R appuser:appuser /workspace
```

**Container Issues:**
```bash
# Rebuild container
docker-compose down
docker-compose up --build

# Clear volumes
docker-compose down -v
docker volume prune -f
```

---

## 🎯 Best Practices

### **📝 Development Workflow**
1. **Use VS Code** for integrated development experience
2. **Commit frequently** with pre-commit validation
3. **Test changes** before pushing
4. **Use database** for development data only
5. **Keep workspace clean** with regular cleanup

### **🔐 Security Considerations**
- **Never commit** development database files
- **Use environment variables** for sensitive data
- **Regular updates** of dependencies
- **Security scanning** in CI/CD pipeline
- **Code review** before merging changes

### **📊 Performance Tips**
- **Use Redis** for caching frequently accessed data
- **Database indexing** for faster queries
- **Nginx optimization** for static file serving
- **File watching** for automatic reloading
- **Resource monitoring** to identify bottlenecks

---

## 📞 Getting Help

### **🐛 Issues & Support**
- **Container Issues**: Check `make dev-logs`
- **Development Problems**: Use `make help`
- **Documentation**: Read project README files
- **Community**: GitHub Issues and Discussions

### **🔗 Useful Links**
- [DevContainer Documentation](https://code.visualstudio.com/docs/devcontainers/containers/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/containers/)

---

## 🔗 Related Topics

- [Development Tools](../docs/assets/scripts.md) - Automation scripts
- [Contributing Guidelines](../CONTRIBUTING.md) - How to contribute
- [Project README](../docs/core/README.md) - Main documentation
- [Automation Workflows](../.github/workflows/) - CI/CD pipeline

---

*"Big facts" - development environment on lockdown* 🐳

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>