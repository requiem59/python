import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--buscar', help = "Opción a buscar")
parser = parser.parse_args()

if parser.buscar:
    bus = mechanize.Browser()
    bus.set_handle_robots(False)
    bus.set_handle_equiv(False)
    bus.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0)')]
    bus.open("https://www.google.com")
    bus.select_form(nr=0)
    bus['q'] = parser.buscar
    bus.submit()
    b = BeautifulSoup(bus.response().read(), 'html5lib')
    
    for link in b.find_all('a'):
        print(link.get('href'))
    
else:
    print("No has dado una palabra a buscar.")
