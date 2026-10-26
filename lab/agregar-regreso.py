"""Inserta el botón "← ARWEN Lab" y el ícono de pestaña en cada guía de esta carpeta.

Uso: python3 lab/agregar-regreso.py
Es seguro correrlo varias veces: si una guía ya tiene el botón, la salta.
"""
from pathlib import Path

MARK = 'id="arwen-back"'
ICONS = '''<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="icon" href="../favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
'''
SNIPPET = '''<!-- ARWEN Lab · botón de regreso -->
<style>
#arwen-back{position:fixed;top:14px;left:14px;z-index:1000;display:inline-flex;align-items:center;gap:8px;
  padding:9px 14px;background:rgba(10,10,11,.82);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);
  border:1px solid rgba(201,151,91,.35);color:#EDE7DC;text-decoration:none;
  font:400 11px/1 'Jost',Futura,'Century Gothic',system-ui,sans-serif;letter-spacing:.22em;text-transform:uppercase;
  transition:border-color .25s,color .25s}
#arwen-back:hover{border-color:#C9975B;color:#C9975B}
#arwen-back:focus-visible{outline:1.5px solid #C9975B;outline-offset:3px}
@media print{#arwen-back{display:none}}
</style>
<a id="arwen-back" href="index.html" aria-label="Volver al ARWEN Lab">← ARWEN Lab</a>
'''

here = Path(__file__).parent
for page in sorted(here.glob('*.html')):
    if page.name == 'index.html':
        continue
    html = page.read_text(encoding='utf-8')
    if 'favicon.svg' not in html and '</head>' in html:
        k = html.index('</head>')
        html = html[:k] + ICONS + html[k:]
        page.write_text(html, encoding='utf-8')
        print(f'ícono agregado: {page.name}')
    if MARK in html:
        print(f'ya tiene botón: {page.name}')
        continue
    i = html.find('<body')
    if i == -1:
        print(f'sin <body>, revisar a mano: {page.name}')
        continue
    j = html.find('>', i) + 1
    page.write_text(html[:j] + '\n' + SNIPPET + html[j:], encoding='utf-8')
    print(f'botón agregado: {page.name}')
