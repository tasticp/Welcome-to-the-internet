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
from datetime import datetime

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
    
    # Export report
    with open("validation-report.json", 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Report exported to validation-report.json")