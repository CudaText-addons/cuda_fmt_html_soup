from bs4 import BeautifulSoup

def do_format(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.prettify(formatter=None)
