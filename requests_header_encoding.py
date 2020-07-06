import re
from html import unescape
from urllib.parse import urljoin

with open('dp.html') as f:
    html=f.read()

for partial_html in re.findall('r<a itemprop='url)