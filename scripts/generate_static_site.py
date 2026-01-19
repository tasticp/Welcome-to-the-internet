#!/usr/bin/env python3
"""
Static Site Generator
Creates interactive HTML site from markdown documentation
"""

import json
from pathlib import Path
from datetime import datetime

def generate_static_site():
    """Generate enhanced static site with interactive features"""
    
    # Load data files if they exist
    search_data = {}
    trending_data = {}
    community_data = {}
    
    try:
        with open("docs/assets/search-index.json", "r") as f:
            search_data = json.load(f)
    except FileNotFoundError:
        print("Search index not found, using placeholder")
        
    try:
        with open("docs/assets/trending-data.json", "r") as f:
            trending_data = json.load(f)
    except FileNotFoundError:
        print("Trending data not found, using placeholder")
        
    try:
        with open("docs/assets/community-stats.json", "r") as f:
            community_data = json.load(f)
    except FileNotFoundError:
        print("Community stats not found, using placeholder")
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Internet - Brainrot Documentation</title>
    <meta name="description" content="The ultimate brainrot repository - comprehensive documentation of internet culture, memes, and Gen Z slang">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/markdown-it/13.0.1/markdown-it.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.1.0/showdown.min.js"></script>
    <style>
        body {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            background: #0d1117;
            color: #c9d1d9;
        }}
        .markdown-body {{
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
            background: #161b22;
            border-radius: 6px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .search-container {{
            background: #21262d;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 24px;
        }}
        .search-input {{
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #30363d;
            border-radius: 4px;
            background: #0d1117;
            color: #c9d1d9;
            font-size: 16px;
        }}
        .search-results {{
            margin-top: 16px;
            max-height: 300px;
            overflow-y: auto;
        }}
        .trending-container {{
            background: #21262d;
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 24px;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            margin: 2px;
            background: #238636;
            color: white;
            border-radius: 4px;
            font-size: 12px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 16px;
            margin: 24px 0;
        }}
        .stat-card {{
            background: #21262d;
            border-radius: 6px;
            padding: 16px;
            border: 1px solid #30363d;
        }}
        .interactive-controls {{
            background: #21262d;
            border-radius: 6px;
            padding: 16px;
            margin: 24px 0;
            text-align: center;
        }}
        .btn {{
            background: #238636;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            margin: 4px;
            cursor: pointer;
            font-size: 14px;
        }}
        .btn:hover {{
            background: #2ea043;
        }}
        h1, h2, h3 {{ color: #58a6ff; }}
        a {{ color: #58a6ff; }}
        a:hover {{ color: #79c0ff; }}
        .trend-item {{
            background: #21262d;
            border-radius: 6px;
            padding: 12px;
            margin: 8px 0;
            border-left: 4px solid #238636;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            border-top: 1px solid #30363d;
            color: #8b949e;
        }}
    </style>
</head>
<body>
    <div class="markdown-body">
        <div class="header">
            <h1>🌌 Welcome to the Internet 💀</h1>
            <p><strong>The Ultimate Brainrot Repository - No Cap Fr Fr</strong> 🗣️</p>
            <p><span class="badge">MIT License</span> <span class="badge">Professional Documentation</span> <span class="badge">26 Files</span> <span class="badge">5,046+ Lines</span></p>
        </div>
        
        <div class="search-container">
            <h3>🔍 Search Documentation</h3>
            <input type="text" class="search-input" id="searchInput" placeholder="Search for brainrot topics, slang, platforms...">
            <div class="search-results" id="searchResults"></div>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>📚 Documentation</h3>
                <p><span class="badge">{len(search_data.get('documents', []))} Files</span> <span class="badge">5,046+ Lines</span></p>
            </div>
            <div class="stat-card">
                <h3>🤖 Automation</h3>
                <p><span class="badge">CI/CD Active</span> <span class="badge">Auto-Updates</span></p>
            </div>
            <div class="stat-card">
                <h3>🌍 Community</h3>
                <p><span class="badge">Contributors Welcome</span> <span class="badge">Professional</span></p>
            </div>
        </div>
        
        <div class="interactive-controls">
            <h3>🎮 Interactive Features</h3>
            <button class="btn" onclick="loadSearchData()">🔍 Load Search</button>
            <button class="btn" onclick="loadTrendingData()">📈 Load Trends</button>
            <button class="btn" onclick="loadAnalytics()">📊 Load Analytics</button>
            <button class="btn" onclick="toggleTheme()">🌙 Toggle Theme</button>
        </div>
        
        <div id="dynamicContent">
            <h3>🎯 Quick Navigation</h3>
            <div class="stats-grid">
                <div class="stat-card">
                    <h4>🧠 Core Concepts</h4>
                    <p><a href="core/brainrot-deep-dive.md">Brainrot Deep Dive</a><br>
                    <a href="core/mental-health-context.md">Mental Health Context</a><br>
                    <a href="core/README.md">Main Documentation</a></p>
                </div>
                <div class="stat-card">
                    <h4>🌍 Cultural Analysis</h4>
                    <p><a href="culture/skibidi-toilet.md">Skibidi Toilet</a><br>
                    <a href="culture/cultural-references.md">Cultural References</a></p>
                </div>
                <div class="stat-card">
                    <h4>🚀 Platform Studies</h4>
                    <p><a href="platforms/youtube.md">YouTube Analysis</a><br>
                    <a href="platforms/tiktok.md">TikTok Study</a><br>
                    <a href="platforms/discord.md">Discord Community</a></p>
                </div>
                <div class="stat-card">
                    <h4>🛠️ Resources</h4>
                    <p><a href="assets/references.md">Academic References</a><br>
                    <a href="assets/scripts.md">Automation Tools</a><br>
                    <a href="assets/issues.md">Project Planning</a></p>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p><strong>🚽 Welcome to the Internet</strong> - Professional brainrot documentation</p>
        <p>Generated with ❤️ by GitHub Actions • Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
    
    <script>
        let searchData, trendingData, analyticsData;
        let isDarkMode = true;
        
        async function loadSearchData() {{
            try {{
                const response = await fetch('assets/search-index.json');
                searchData = await response.json();
                let html = '<h3>📚 Search Index Loaded</h3><p>Loaded ' + searchData.documents.length + ' documents for search</p>';
                html += '<div class="stats-grid">';
                searchData.documents.slice(0, 6).forEach(doc => {{
                    html += '<div class="stat-card"><h4><a href="' + doc.path + '">' + doc.title + '</a></h4>';
                    html += '<p><small>Category: ' + doc.category + '</small><br>';
                    html += '<small>Sections: ' + doc.sections.length + '</small></p></div>';
                }});
                html += '</div>';
                document.getElementById('dynamicContent').innerHTML = html;
            }} catch (error) {{
                console.error('Error loading search data:', error);
            }}
        }}
        
        async function loadTrendingData() {{
            try {{
                const response = await fetch('assets/trending-data.json');
                trendingData = await response.json();
                let html = '<h3>📈 Current Trends</h3>';
                trendingData.trending_topics.forEach(trend => {{
                    html += '<div class="trend-item"><h4>' + trend.topic + '</h4>';
                    html += '<p><strong>Platform:</strong> ' + trend.platform + '<br>';
                    html += '<strong>Growth:</strong> ' + trend.growth_rate + '<br>';
                    html += '<strong>Mentions:</strong> ' + trend.mentions.toLocaleString() + '</p></div>';
                }});
                document.getElementById('dynamicContent').innerHTML = html;
            }} catch (error) {{
                console.error('Error loading trending data:', error);
            }}
        }}
        
        async function loadAnalytics() {{
            try {{
                const response = await fetch('assets/analytics.md');
                const text = await response.text();
                document.getElementById('dynamicContent').innerHTML = '<div class="markdown-body">' + text + '</div>';
            }} catch (error) {{
                console.error('Error loading analytics:', error);
            }}
        }}
        
        function toggleTheme() {{
            isDarkMode = !isDarkMode;
            if (isDarkMode) {{
                document.body.style.background = '#0d1117';
                document.body.style.color = '#c9d1d9';
            }} else {{
                document.body.style.background = '#ffffff';
                document.body.style.color = '#24292e';
            }}
        }}
        
        // Setup search functionality
        document.getElementById('searchInput').addEventListener('input', function(e) {{
            const query = e.target.value.toLowerCase();
            if (query.length > 2 && searchData) {{
                const results = searchData.documents.filter(doc => 
                    doc.title.toLowerCase().includes(query) ||
                    doc.key_terms.some(term => term.toLowerCase().includes(query)) ||
                    doc.sections.some(section => section.toLowerCase().includes(query))
                );
                
                let html = '<h4>Search Results:</h4>';
                if (results.length === 0) {{
                    html += '<p>No results found for "' + query + '"</p>';
                }} else {{
                    html += '<div class="stats-grid">';
                    results.slice(0, 6).forEach(doc => {{
                        html += '<div class="stat-card"><h4><a href="' + doc.path + '">' + doc.title + '</a></h4>';
                        html += '<p><small>Category: ' + doc.category + '</small><br>';
                        html += '<small>Content Length: ' + doc.content_length + ' characters</small></p></div>';
                    }});
                    html += '</div>';
                }}
                
                document.getElementById('searchResults').innerHTML = html;
            }} else {{
                document.getElementById('searchResults').innerHTML = '';
            }}
        }});
        
        // Load initial data
        window.addEventListener('load', function() {{
            console.log('Interactive site loaded successfully');
        }});
    </script>
</body>
</html>'''
    
    with open("dist/index.html", "w") as f:
        f.write(html_content)
        
    print("✅ Interactive static site generated")

if __name__ == "__main__":
    generate_static_site()