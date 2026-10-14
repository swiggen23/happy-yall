"""Builds site/index.html from src/template.html + src/data.js. Run: python3 build.py"""
from pathlib import Path

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Find Austin happy hours that match your neighborhood, time, budget and vibe.">
<meta name="theme-color" content="#FF8A5B">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 92 92'%3E%3Ccircle cx='46' cy='46' r='26' fill='%23FFD23F' stroke='%231A1440' stroke-width='5'/%3E%3C/svg%3E">
<link rel="stylesheet" href="vendor/leaflet/leaflet.css">
<script src="vendor/leaflet/leaflet.js"></script>
<script>window.HYA_SITE = true;</script>
<style>:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); } body { margin: 0; } img { max-width: 100%; } [hidden] { display: none !important; }</style>
'''

root = Path(__file__).parent
body = (root / 'src/template.html').read_text().replace('__DATA__', (root / 'src/data.js').read_text())
i = body.index('<style>')
j = body.index('</style>', i) + len('</style>')
html = HEAD + body[:i] + body[i:j] + '\n</head>\n<body>\n' + body[j:] + '\n</body>\n</html>\n'
(root / 'site/index.html').write_text(html)
print('built site/index.html', len(html), 'bytes')
