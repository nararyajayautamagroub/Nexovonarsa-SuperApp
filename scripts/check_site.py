from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import tempfile

FILES = ("index.html", "store.html")

class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.title = False
        self.scripts = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise ValueError(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "script":
            self.scripts += 1
    def handle_data(self, data):
        pass

for filename in FILES:
    source = Path(filename).read_text(encoding="utf-8")
    if "<!doctype html>" not in source.lower():
        raise SystemExit(f"{filename}: missing HTML doctype")
    parser = Check()
    parser.feed(source)
    parser.close()
    if not re.search(r"<title>.*?</title>", source, re.I | re.S):
        raise SystemExit(f"{filename}: missing title")
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", source, re.I | re.S)
    for i, js in enumerate(scripts):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as f:
            f.write(js)
            f.flush()
            result = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
            if result.returncode:
                raise SystemExit(f"{filename}: JavaScript syntax error in inline script {i+1}:\n{result.stderr}")
    print(f"PASS {filename}: HTML parsed, title present, {len(parser.ids)} unique IDs, {len(scripts)} inline script(s) syntax-checked")

if 'href="store.html"' not in Path("index.html").read_text(encoding="utf-8"):
    raise SystemExit("index.html does not link to store.html")
print("PASS home-to-store link")
