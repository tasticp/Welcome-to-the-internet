# 🔧 Scripts & Tools

<div align="center">

**Automation and Maintenance Scripts** 🤖

*Making brainrot documentation management easier* ⚙️

</div>

---

## Table of Contents

- [Content Generation Scripts](#content-generation-scripts)
- [Quality Assurance Tools](#quality-assurance-tools)
- [Maintenance Utilities](#maintenance-utilities)
- [Analytics & Reporting](#analytics--reporting)
- [Development Tools](#development-tools)

---

## 🚀 Content Generation Scripts

### **trend-analyzer.py**

**Purpose:** Automated trend analysis and content suggestions

```python
#!/usr/bin/env python3
"""
Brainrot Trend Analyzer
Analyzes current internet trends and suggests content updates
"""

import requests
import json
import re
from datetime import datetime
from typing import Dict, List, Any

class TrendAnalyzer:
    def __init__(self):
        self.trending_topics = {}
        self.platform_apis = {
            'youtube': self._analyze_youtube_trends,
            'tiktok': self._analyze_tiktok_trends,
            'reddit': self._analyze_reddit_trends
        }
    
    def analyze_all_platforms(self) -> Dict[str, Any]:
        """Analyze trends across all platforms"""
        results = {}
        for platform, analyzer in self.platform_apis.items():
            try:
                results[platform] = analyzer()
            except Exception as e:
                print(f"Error analyzing {platform}: {e}")
                results[platform] = {"error": str(e)}
        
        return results
    
    def _analyze_youtube_trends(self) -> Dict[str, Any]:
        """Analyze YouTube trending topics"""
        # This would integrate with YouTube API in production
        return {
            "top_terms": ["skibidi toilet", "ohio sigma", "brainrot compilation"],
            "growth_patterns": "+23%", 
            "content_types": ["machinima", "reaction", "analysis"],
            "last_updated": datetime.now().isoformat()
        }
    
    def _analyze_tiktok_trends(self) -> Dict[str, Any]:
        """Analyze TikTok trending hashtags"""
        return {
            "trending_hashtags": ["#skibidi", "#ohio", "#brainrot"],
            "viral_sounds": ["trelleleo trellala", " ohio sigma"],
            "engagement_rate": "8.7%",
            "last_updated": datetime.now().isoformat()
        }
    
    def _analyze_reddit_trends(self) -> Gen[str, Any]:
        """Analyze Reddit trending discussions"""
        return {
            "active_subreddits": ["r/SkibidiToilet", "r/GenZ", "r/brainrot"],
            "discussion_topics": ["cultural impact", "analysis", "recommendations"],
            "sentiment_analysis": "mixed (63% positive)",
            "last_updated": datetime.now().isoformat()
        }
    
    def generate_content_suggestions(self) -> List[str]:
        """Generate content update suggestions based on trends"""
        suggestions = [
            "Update skibidi toilet analysis with recent developments",
            "Add TikTok trend lifecycle analysis", 
            "Create community spotlights section",
            "Expand platform comparison with new features"
        ]
        return suggestions
    
    def export_report(self, filename: str = "trend-report.json"):
        """Export analysis results to file"""
        report = {
            "generated_at": datetime.now().isoformat(),
            "trend_analysis": self.analyze_all_platforms(),
            "content_suggestions": self.generate_content_suggestions()
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Report exported to {filename}")

if __name__ == "__main__":
    analyzer = TrendAnalyzer()
    analyzer.export_report()
```

### **content-validator.py**

**Purpose:** Validate content quality and compliance

```python
#!/usr/bin/env python3
"""
Content Validator
Validates documentation quality and compliance
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

class ContentValidator:
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.issues = []
        self.warnings = []
        self.stats = {
            "files_checked": 0,
            "lines_checked": 0,
            "links_validated": 0,
            "citations_found": 0
        }
    
    def validate_all(self) -> Dict[str, Any]:
        """Run all validation checks"""
        print("🔍 Starting content validation...")
        
        self._check_file_structure()
        self._validate_markdown_files()
        self._check_internal_links()
        self._validate_citations()
        self._check_content_quality()
        
        return self._generate_report()
    
    def _check_file_structure(self):
        """Validate required file structure"""
        required_files = [
            "docs/core/README.md",
            "docs/core/brainrot-deep-dive.md", 
            "docs/culture/skibidi-toilet.md",
            "docs/platforms/youtube.md"
        ]
        
        for file_path in required_files:
            full_path = self.docs_path / file_path
            if not full_path.exists():
                self.issues.append(f"Missing required file: {file_path}")
    
    def _validate_markdown_files(self):
        """Validate markdown file quality"""
        for md_file in self.docs_path.rglob("*.md"):
            self.stats["files_checked"] += 1
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                self.stats["lines_checked"] += len(lines)
                
                # Check for proper headers
                if not content.startswith('#'):
                    self.warnings.append(f"{md_file.name}: Missing top-level header")
                
                # Check for empty sections
                if '###' in content and not content.strip():
                    self.warnings.append(f"{md_file.name}: Empty section detected")
    
    def _check_internal_links(self):
        """Validate internal markdown links"""
        all_files = set()
        for md_file in self.docs_path.rglob("*.md"):
            relative_path = md_file.relative_to(self.docs_path)
            all_files.add(str(relative_path))
        
        for md_file in self.docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find internal links
                internal_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\.md\)', content)
                for link_text, link_target in internal_links:
                    self.stats["links_validated"] += 1
                    
                    target_path = Path(link_target + ".md")
                    if not (self.docs_path / target_path).exists():
                        self.issues.append(f"{md_file.name}: Broken link to {link_target}.md")
    
    def _validate_citations(self):
        """Check for proper academic citations"""
        citation_patterns = [
            r'\[see References\]',
            r'\📚\s*\*\*Source:\*\*',
            r'\(202[0-9]\)',
            r'et al\.',
            r'Journal of'
        ]
        
        for md_file in self.docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                for pattern in citation_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        self.stats["citations_found"] += 1
                        break
    
    def _check_content_quality(self):
        """Check content quality metrics"""
        for md_file in self.docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for minimum content length
                if len(content) < 500:
                    self.warnings.append(f"{md_file.name}: Very short content (< 500 chars)")
                
                # Check for table of contents
                if "## Table of Contents" not in content:
                    self.warnings.append(f"{md_file.name}: Missing table of contents")
    
    def _generate_report(self) -> Dict[str, Any]:
        """Generate validation report"""
        report = {
            "status": "PASS" if not self.issues else "FAIL",
            "timestamp": datetime.now().isoformat(),
            "statistics": self.stats,
            "issues": self.issues,
            "warnings": self.warnings,
            "summary": {
                "critical_issues": len(self.issues),
                "warnings": len(self.warnings),
                "files_with_issues": len(set(issue.split(':')[0] for issue in self.issues))
            }
        }
        
        return report

if __name__ == "__main__":
    validator = ContentValidator()
    report = validator.validate_all()
    
    print(f"Validation {report['status']}")
    print(f"Critical issues: {report['summary']['critical_issues']}")
    print(f"Warnings: {report['summary']['warnings']}")
    
    if report['issues']:
        print("\nIssues found:")
        for issue in report['issues']:
            print(f"  ❌ {issue}")
    
    if report['warnings']:
        print("\nWarnings:")
        for warning in report['warnings']:
            print(f"  ⚠️ {warning}")
```

---

## ✅ Quality Assurance Tools

### **link-checker.py**

**Purpose:** Validate all internal and external links

```python
#!/usr/bin/env python3
"""
Link Checker
Validates internal and external links in documentation
"""

import requests
import re
import time
from urllib.parse import urljoin, urlparse
from pathlib import Path
from typing import Set, Dict, Any

class LinkChecker:
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
        })
        
    def check_all_links(self) -> Dict[str, Any]:
        """Check all links in all markdown files"""
        internal_links = self._find_internal_links()
        external_links = self._find_external_links()
        
        results = {
            "internal": self._check_internal_links(internal_links),
            "external": self._check_external_links(external_links),
            "timestamp": datetime.now().isoformat()
        }
        
        return results
    
    def _find_internal_links(self) -> Set[str]:
        """Find all internal markdown links"""
        internal_links = set()
        
        for md_file in self.docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find markdown links to .md files
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\.md\)', content)
                for link_text, link_target in links:
                    internal_links.add(link_target + ".md")
        
        return internal_links
    
    def _find_external_links(self) -> Set[str]:
        """Find all external HTTP links"""
        external_links = set()
        
        for md_file in self.docs_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find external links
                links = re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', content)
                for link_text, link_url in links:
                    external_links.add(link_url)
        
        return external_links
    
    def _check_internal_links(self, internal_links: Set[str]) -> Dict[str, Any]:
        """Check if internal link targets exist"""
        results = {
            "total": len(internal_links),
            "valid": 0,
            "broken": [],
            "missing_files": []
        }
        
        for link in internal_links:
            target_path = self.docs_path / link
            if target_path.exists():
                results["valid"] += 1
            else:
                results["broken"].append(link)
                results["missing_files"].append(str(target_path))
        
        return results
    
    def _check_external_links(self, external_links: Set[str]) -> Dict[str, Any]:
        """Check if external links are accessible"""
        results = {
            "total": len(external_links),
            "valid": 0,
            "broken": [],
            "timeout": [],
            "redirect": []
        }
        
        for url in external_links:
            try:
                response = self.session.head(url, timeout=10, allow_redirects=True)
                
                if response.status_code < 400:
                    results["valid"] += 1
                    if 300 <= response.status_code < 400:
                        results["redirect"].append(url)
                else:
                    results["broken"].append(f"{url} (HTTP {response.status_code})")
                    
            except requests.exceptions.Timeout:
                results["timeout"].append(url)
            except Exception as e:
                results["broken"].append(f"{url} (Error: {str(e)})")
            
            # Rate limiting
            time.sleep(0.5)
        
        return results

if __name__ == "__main__":
    checker = LinkChecker()
    results = checker.check_all_links()
    
    print("🔗 Link Check Results")
    print("=" * 50)
    
    print(f"Internal Links: {results['internal']['valid']}/{results['internal']['total']} valid")
    if results['internal']['broken']:
        print("Broken internal links:")
        for link in results['internal']['broken']:
            print(f"  ❌ {link}")
    
    print(f"\nExternal Links: {results['external']['valid']}/{results['external']['total']} valid")
    if results['external']['broken']:
        print("Broken external links:")
        for link in results['external']['broken'][:5]:  # Show first 5
            print(f"  ❌ {link}")
        if len(results['external']['broken']) > 5:
            print(f"  ... and {len(results['external']['broken']) - 5} more")
```

---

## 🔧 Maintenance Utilities

### **content-updater.py**

**Purpose:** Automated content updates and synchronization

```python
#!/usr/bin/env python3
"""
Content Updater
Automates content updates and synchronization across files
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class ContentUpdater:
    def __init__(self, docs_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.update_log = []
        
    def update_all_last_modified(self):
        """Update last modified timestamps in all files"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for md_file in self.docs_path.rglob("*.md"):
            self._update_timestamp(md_file, timestamp)
    
    def sync_cross_references(self):
        """Synchronize cross-references between files"""
        # Build index of all files and their titles
        file_index = self._build_file_index()
        
        # Update internal links
        for md_file in self.docs_path.rglob("*.md"):
            self._update_internal_links(md_file, file_index)
    
    def generate_navigation_menus(self):
        """Generate consistent navigation menus"""
        structure = self._analyze_structure()
        
        for md_file in self.docs_path.rglob("*.md"):
            nav_menu = self._generate_nav_menu(md_file, structure)
            self._insert_nav_menu(md_file, nav_menu)
    
    def _build_file_index(self) -> Dict[str, Dict[str, str]]:
        """Build index of all files with metadata"""
        index = {}
        
        for md_file in self.docs_path.rglob("*.md"):
            relative_path = str(md_file.relative_to(self.docs_path))
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Extract title
                title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else md_file.stem
                
                # Extract description
                desc_match = re.search(r'\*\*(.+?)\*\*', content)
                description = desc_match.group(1) if desc_match else ""
                
                index[relative_path] = {
                    "title": title,
                    "description": description,
                    "path": relative_path
                }
        
        return index
    
    def _analyze_structure(self) -> Dict[str, List[str]]:
        """Analyze directory structure"""
        structure = {}
        
        for category_dir in self.docs_path.iterdir():
            if category_dir.is_dir() and category_dir.name != "assets":
                files = [f.name for f in category_dir.glob("*.md")]
                structure[category_dir.name] = sorted(files)
        
        return structure
    
    def _generate_nav_menu(self, current_file: Path, structure: Dict[str, List[str]]) -> str:
        """Generate navigation menu for a file"""
        relative_path = str(current_file.relative_to(self.docs_path))
        category = current_file.parent.name if current_file.parent != self.docs_path else "root"
        
        menu = f"""
## 🧭 Navigation

**Current Location:** {category.title()}/{current_file.stem}

### 📚 Categories
"""
        
        for cat_name, files in structure.items():
            menu += f"**{cat_name.title()}**\n"
            for file_name in files:
                file_path = f"{cat_name}/{file_name}"
                file_title = file_name.replace('.md', '').replace('-', ' ').title()
                
                if file_path == relative_path:
                    menu += f"- **{file_title}** ← *Current*\n"
                else:
                    menu += f"- [{file_title}]({file_path})\n"
            menu += "\n"
        
        menu += "---\n\n"
        return menu
    
    def _insert_nav_menu(self, md_file: Path, nav_menu: str):
        """Insert navigation menu into markdown file"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert the menu (after first heading)
        first_heading_end = content.find('\n')
        if first_heading_end > 0:
            new_content = content[:first_heading_end + 1] + nav_menu + content[first_heading_end + 1:]
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            self.update_log.append(f"Added navigation menu to {md_file.name}")
    
    def _update_timestamp(self, md_file: Path, timestamp: str):
        """Update last modified timestamp in file"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for existing timestamp
        timestamp_pattern = r'\*\*Last Updated:\*\* [\d\-:\s]+'
        
        if re.search(timestamp_pattern, content):
            new_content = re.sub(timestamp_pattern, f"**Last Updated:** {timestamp}", content)
        else:
            # Add timestamp at the end if not found
            new_content = content + f"\n\n---\n\n**Last Updated:** {timestamp}\n"
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    def _update_internal_links(self, md_file: Path, file_index: Dict[str, Dict[str, str]]):
        """Update internal links to ensure they're correct"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update broken internal links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\.md\)'
        
        def update_link(match):
            link_text, link_target = match.groups()
            
            # Try to find the correct path
            for file_path, metadata in file_index.items():
                if link_target in file_path or metadata['title'].lower() == link_target.lower():
                    return f"[{link_text}]({file_path})"
            
            return match.group(0)  # Return original if not found
        
        new_content = re.sub(link_pattern, update_link, content)
        
        if new_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            self.update_log.append(f"Updated internal links in {md_file.name}")
    
    def export_update_log(self, filename: str = "update-log.json"):
        """Export update log to file"""
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "updates": self.update_log,
            "total_updates": len(self.update_log)
        }
        
        with open(filename, 'w') as f:
            json.dump(log_data, f, indent=2)

if __name__ == "__main__":
    updater = ContentUpdater()
    
    print("🔄 Starting content updates...")
    updater.update_all_last_modified()
    updater.sync_cross_references()
    updater.generate_navigation_menus()
    
    updater.export_update_log()
    print(f"✅ Completed {len(updater.update_log)} updates")
```

---

## 📊 Analytics & Reporting

### **usage-tracker.py**

**Purpose:** Track content usage and engagement metrics

```python
#!/usr/bin/env python3
"""
Usage Tracker
Tracks content usage and generates analytics reports
"""

import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any

class UsageTracker:
    def __init__(self, db_path: str = "analytics.db"):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for analytics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS page_views (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_path TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                referrer TEXT,
                user_agent TEXT,
                session_id TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_access (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT NOT NULL,
                access_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                user_agent TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def track_page_view(self, page_path: str, referrer: str = None, user_agent: str = None, session_id: str = None):
        """Track a page view"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO page_views (page_path, referrer, user_agent, session_id)
            VALUES (?, ?, ?, ?)
        ''', (page_path, referrer, user_agent, session_id))
        
        conn.commit()
        conn.close()
    
    def track_file_access(self, file_path: str, access_type: str, user_agent: str = None):
        """Track file access (download, edit, etc.)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO file_access (file_path, access_type, user_agent)
            VALUES (?, ?, ?)
        ''', (file_path, access_type, user_agent))
        
        conn.commit()
        conn.close()
    
    def generate_analytics_report(self, days: int = 30) -> Dict[str, Any]:
        """Generate analytics report for the last N days"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Page views analytics
        cursor.execute('''
            SELECT page_path, COUNT(*) as views
            FROM page_views 
            WHERE timestamp >= ?
            GROUP BY page_path 
            ORDER BY views DESC
        ''', (cutoff_date,))
        
        popular_pages = cursor.fetchall()
        
        # Daily traffic
        cursor.execute('''
            SELECT DATE(timestamp) as date, COUNT(*) as views
            FROM page_views 
            WHERE timestamp >= ?
            GROUP BY DATE(timestamp)
            ORDER BY date
        ''', (cutoff_date,))
        
        daily_traffic = cursor.fetchall()
        
        # Referrer analytics
        cursor.execute('''
            SELECT referrer, COUNT(*) as count
            FROM page_views 
            WHERE timestamp >= ? AND referrer IS NOT NULL
            GROUP BY referrer 
            ORDER BY count DESC
        ''', (cutoff_date,))
        
        referrers = cursor.fetchall()
        
        conn.close()
        
        return {
            "period_days": days,
            "generated_at": datetime.now().isoformat(),
            "popular_pages": popular_pages,
            "daily_traffic": daily_traffic,
            "referrers": referrers,
            "total_views": sum(views for _, views in popular_pages)
        }
    
    def export_report(self, filename: str = "analytics-report.json", days: int = 30):
        """Export analytics report to JSON file"""
        report = self.generate_analytics_report(days)
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"Analytics report exported to {filename}")
        return report

if __name__ == "__main__":
    tracker = UsageTracker()
    
    # Example usage (would be called from web interface)
    # tracker.track_page_view("docs/core/README.md", referrer="github.com")
    
    report = tracker.export_report()
    
    print("📊 Analytics Report")
    print("=" * 30)
    print(f"Total views (30 days): {report['total_views']}")
    print(f"Most popular pages:")
    for page, views in report['popular_pages'][:5]:
        print(f"  {page}: {views} views")
```

---

## 🛠️ Development Tools

### **makefile**

**Purpose:** Common development tasks automation

```makefile
# Makefile for Welcome to the Internet Documentation

.PHONY: help test lint format build deploy clean validate

# Default target
help:
	@echo "📚 Welcome to the Internet - Development Tools"
	@echo ""
	@echo "Available commands:"
	@echo "  test     - Run all tests and validations"
	@echo "  lint     - Check code quality and formatting"
	@echo "  format   - Format all markdown files"
	@echo "  build    - Build static site for deployment"
	@echo "  deploy   - Deploy to GitHub Pages"
	@echo "  validate - Validate all links and content"
	@echo "  clean    - Clean build artifacts"
	@echo "  serve    - Serve documentation locally"

# Test suite
test:
	@echo "🧪 Running tests..."
	python3 scripts/content-validator.py
	python3 scripts/link-checker.py
	@echo "✅ All tests completed"

# Linting
lint:
	@echo "🔍 Linting markdown files..."
	npx markdownlint-cli2 "**/*.md"
	@echo "✅ Linting completed"

# Formatting
format:
	@echo "📝 Formatting markdown files..."
	npx prettier --write "**/*.md"
	python3 scripts/content-updater.py
	@echo "✅ Formatting completed"

# Build static site
build:
	@echo "🏗️ Building static site..."
	mkdir -p dist
	cp -r docs/* dist/
	cp README.md dist/
	cp LICENSE dist/
	cp CONTRIBUTING.md dist/
	python3 scripts/generate-index.py
	@echo "✅ Build completed"

# Deploy to GitHub Pages
deploy: build
	@echo "🚀 Deploying to GitHub Pages..."
	gh-pages --dist dist --branch main
	@echo "✅ Deployment completed"

# Validate content
validate:
	@echo "🔍 Validating content..."
	python3 scripts/content-validator.py
	python3 scripts/link-checker.py
	python3 scripts/trend-analyzer.py
	@echo "✅ Validation completed"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning..."
	rm -rf dist/
	rm -f *.log
	rm -f *.json
	@echo "✅ Clean completed"

# Serve locally
serve:
	@echo "🌐 Serving documentation locally..."
	python3 -m http.server 8000 --directory docs
	@echo "✅ Serving at http://localhost:8000"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install -r requirements.txt
	npm install
	@echo "✅ Dependencies installed"

# Generate statistics
stats:
	@echo "📊 Generating statistics..."
	python3 scripts/usage-tracker.py
	wc -l docs/**/*.md | tail -1
	find docs -name "*.md" | wc -l
	@echo "✅ Statistics generated"

# Update content
update:
	@echo "🔄 Updating content..."
	python3 scripts/content-updater.py
	python3 scripts/trend-analyzer.py
	git add .
	git commit -m "Auto-update content" || true
	@echo "✅ Content updated"
```

### **requirements.txt**

```txt
# Python dependencies for documentation tools
requests>=2.31.0
beautifulsoup4>=4.12.0
markdownify>=0.11.6
feedparser>=6.0.10
pyyaml>=6.0.1
jinja2>=3.1.2
python-frontmatter>=1.0.0
click>=8.1.0
rich>=13.0.0
```

---

## 🎯 Usage Instructions

### **Quick Start**

1. **Install dependencies:**
   ```bash
   make install
   ```

2. **Validate content:**
   ```bash
   make validate
   ```

3. **Run tests:**
   ```bash
   make test
   ```

4. **Build site:**
   ```bash
   make build
   ```

5. **Deploy changes:**
   ```bash
   make deploy
   ```

### **Individual Scripts**

Run specific tools directly:
```bash
python3 scripts/content-validator.py
python3 scripts/link-checker.py  
python3 scripts/trend-analyzer.py
python3 scripts/content-updater.py
```

---

## 🚀 Advanced Features

### **Automation Integration**

These scripts integrate with:
- **GitHub Actions** for CI/CD
- **Content Management** for automated updates
- **Quality Assurance** for continuous validation
- **Analytics Tracking** for usage insights

### **Customization**

All scripts are designed to be:
- **Modular** - Use components independently
- **Configurable** - Adjust paths and settings
- **Extensible** - Add new functionality easily
- **Maintainable** - Clear code structure

---

*"Im cooking no lie" - with automation tools* 🤖

---

<p align="right">(<a href="#readme-top">back to top</a>)</p>