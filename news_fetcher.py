import feedparser
from datetime import datetime

# Define your news sources
sources = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "Bloomberg": "https://www.bloomberg.com/feed/podcast/etf-report.xml",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
}

# Start building the HTML content
html_content = f"""
<html>
<head>
    <title>My Curated News Feed</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: sans-serif; padding: 20px; }}
        h2 {{ color: #333; }}
        .source-block {{ margin-bottom: 40px; }}
        .headline {{ margin: 10px 0; }}
    </style>
</head>
<body>
    <h1>📰 My Curated News Feed</h1>
    <p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
"""

for name, url in sources.items():
    feed = feedparser.parse(url)
    html_content += f"<div class='source-block'><h2>{name}</h2>"
    for entry in feed.entries[:5]:
        html_content += f"<div class='headline'><a href='{entry.link}' target='_blank'>{entry.title}</a></div>"
    html_content += "</div>"

html_content += "</body></html>"

# Write the output to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("News feed generated: index.html")
