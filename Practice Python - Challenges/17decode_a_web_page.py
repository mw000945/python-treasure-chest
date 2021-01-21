# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
import requests
from bs4 import BeautifulSoup

URL = 'https://www.nytimes.com/'
r = requests.get(URL)
html = r.text

soup = BeautifulSoup(html, features="html.parser")
articles = list(soup.find_all('article'))
for article in articles:
    print("\n" + article.text)
