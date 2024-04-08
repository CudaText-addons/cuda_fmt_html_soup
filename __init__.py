import sys
import os
sys.path.append(os.path.dirname(__file__))
from bs4 import BeautifulSoup
from bs4.formatter import Formatter
import cudatext as app
from cuda_fmt.fmtconfig import ed_fmt 

def do_format(text):
    soup = BeautifulSoup(text, 'html.parser')
    lang = Formatter.XML if 'XML' in ed_fmt.get_prop(app.PROP_LEXER_FILE) else Formatter.HTML
    indent = ed_fmt.get_prop(app.PROP_TAB_SIZE)*' ' if ed_fmt.get_prop(app.PROP_TAB_SPACES) else '\t'
    fmt = Formatter(
        language=lang,
        indent=indent
        )
    return soup.prettify(formatter=fmt)
