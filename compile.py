from jinja2 import Template
from markdown import markdown
import os
import codecs

d = os.getcwd()

with open(os.path.join(d, "templates/index.html"), "r") as f:
    page = f.read()

markdown_contents = {}
for filename in os.listdir(d):
    p = os.path.join(d, filename)
    if filename.endswith(".md") and os.path.isfile(p):
        with codecs.open(p, encoding="utf-8") as f:
            markdown_contents[filename[0:-3]] = markdown(f.read()).encode("ascii", "xmlcharrefreplace")

template = Template(page)
with open("index.html", "w") as f:
    f.write(template.render(**markdown_contents))
