# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
import requests
from bs4 import BeautifulSoup
URL = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(URL)
html = r.text
soup = BeautifulSoup(html, features="html.parser")
article = list(soup.find_all('p'))

with open('article.txt', 'w') as f:
    for section in article:
        f.write("\n" + section.text)
    f.close()
