# Web Scrapping tool for Cryptocurrencies
Arysbay Dastan (SE-2004)

# Installation
Selenium
```bash
pip install -U selenium
```

Beautifulsoup
```bash
pip install beautifulsoup4
```

To make geckodriver available to the entire system, open the terminal application and run the following command:
```bash
brew install geckodrive
```

# Usage examples

```bash
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie
```
# Example












Running the unit tests

Beautiful Soup supports unit test discovery from the project root directory:

$ nosetests

$ python3 -m unittest discover -s bs4



