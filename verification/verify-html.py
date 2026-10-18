from html.parser import HTMLParser
from pathlib import Path
import re
import sys

class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.select_id = None
        self.values = {}
        self.option_open = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'select':
            self.select_id = attrs.get('id')
            self.values[self.select_id] = []
        if tag == 'option':
            assert self.select_id is not None, 'option outside select'
            assert not self.option_open, 'option not explicitly closed'
            self.option_open = True
            self.values[self.select_id].append(attrs.get('value'))
    def handle_endtag(self, tag):
        if tag == 'option':
            assert self.option_open, 'orphan option end tag'
            self.option_open = False
        if tag == 'select':
            assert not self.option_open, 'unclosed option'
            self.select_id = None

html = (Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1] / 'index.html').read_text(encoding='utf-8')
markup = html.split('<script>')[0]
assert not re.search(r'</[a-zA-Z][^>]*\s[^>]*>', markup), 'closing tag must not contain attributes'
parser = Structure()
parser.feed(markup)
assert parser.values['budget'] == ['9999', '80', '150', '250'], parser.values['budget']
assert len(parser.values['meal-cuisine']) == 4
assert len(parser.values['meal-emoji']) == 8
print('PASS: valid closing tags; all 4 budget options exist in HTML; all category and emoji options exist.')
