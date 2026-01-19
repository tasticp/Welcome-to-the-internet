#!/bin/bash
# Development Container Start Script

echo "🚀 Starting Welcome to Internet development environment..."

# Set environment variables
export NODE_ENV=development
export PYTHONPATH=/workspace
export GIT_AUTHOR_NAME="DevContainer User"
export GIT_AUTHOR_EMAIL="devcontainer@example.com"
export PYTHONUNBUFFERED=1

# Start background services
echo "🔧 Starting background services..."

# Start development database if not running
if ! pgrep -f "sqlite3" > /dev/null; then
    echo "🗄️ Starting development database..."
    sqlite3 /workspace/data/dev.db &
fi

# Start file watcher for auto-reloading
echo "👀 Starting file watcher..."
python3 -c "
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.md'):
            print(f'📝 Detected changes: {event.src_path}')
            os.system('make validate > /dev/null 2>&1 &')

if __name__ == '__main__':
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/workspace/docs', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
" &

# Check for package.json and install dependencies if needed
if [ -f "/workspace/package.json" ]; then
    echo "📦 Checking Node.js dependencies..."
    cd /workspace
    if [ ! -d "node_modules" ]; then
        echo "Installing Node.js dependencies..."
        npm install
    fi
    cd ..
fi

# Set up development log
echo "📊 Setting up development logging..."
mkdir -p /workspace/logs
echo "$(date): Development environment started" >> /workspace/logs/dev-session.log

# Display development status
echo ""
echo "🎯 Development Environment Status:"
echo "  ✅ Python: $(python3 --version)"
echo "  ✅ Node.js: $(node --version 2>/dev/null || echo 'Not installed')"
echo "  ✅ Git: $(git --version)"
echo "  ✅ Workspace: $(pwd)"
echo "  ✅ Documentation: $(find /workspace/docs -name '*.md' | wc -l) files"

# Show available ports and services
echo ""
echo "🌐 Available Services:"
echo "  📚 Documentation Server: http://localhost:8000"
echo "  🎮 Interactive Features: http://localhost:3000"
echo "  🔍 Search API: http://localhost:5000"
echo "  📊 Analytics Dashboard: http://localhost:6000"

# Display development tips
echo ""
echo "💡 Development Tips:"
echo "  📝 Edit files in VS Code with auto-formatting"
echo "  🧪 Run 'make test' to validate changes"
echo "  🔍 Run 'make serve' to start local server"
echo "  📊 Check '/workspace/logs' for development logs"
echo "  🗄️ Use '/workspace/data/dev.db' for development data"

# Create welcome message
echo ""
echo "🎉 Welcome to Internet development environment ready!"
echo "📚 Happy documentation hacking! 🔥"
echo ""
echo "Run 'make help' to see all available commands"

# Keep the container running
tail -f /dev/null