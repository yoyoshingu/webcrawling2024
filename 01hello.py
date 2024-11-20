def h():
    print("hello")


print(type(range(10)))

import urllib.request

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
print(html)
print(html.read())

# <http.client.HTTPResponse object at 0x00000286F01F2880>
# http.client.HttpResponse object format
# https://docs.python.org/3/library/http.client.html

# beautifulsoup 4 설치
# conda install bs4
import bs4
html_str = "<html><div></div></html>"
bsobj = bs4.BeautifulSoup(html_str, "html.parser")
print(type(bsobj))
print(bsobj)