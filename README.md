# Web Scrapping tool for Cryptocurrencies
Arysbay Dastan (SE-2004)

# Installing
Selenium
```bash
pip install -U selenium
```
Alternately, you can download the source distribution from PyPI (e.g. selenium-4.0.0rc3.tar.gz), unarchive it, and run:
```bash
python setup.py install
```
Beautifulsoup
```bash
pip install beautifulsoup4
```

### Downloading geckodriver

The geckodriver executable can be downloaded [here](https://github.com/SeleniumHQ/selenium/blob/trunk/py/docs/source/index.rst)

#### Python3 venv

Download the geckodriver executable from the above link and extract it to env/bin/ to make it accessible to only the virtual environment.

In your python code, you will now be able to do the following:
```bash
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://stackoverflow.com/")
```

#### Linux

If you would like to make it available system wide, download the geckodriver executable from the above link and extract it to `/usr/bin/` (or anything inside of your $PATH)

#### Windows

Note: *this needs a windows user to test and confirm*

Download geckodriver from the above link and extract it to `C:\Windows\System32\` (or anything inside your Path environment variable).

#### Mac OS X


To make geckodriver available system wide, open up your Terminal App and perform the following command:
```bash
brew install geckodriver
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

```bash
# filter Anchor---> 
allNews = soup.findAll('div', class_='sc-16r8icm-0 eMxKgr container')
for news_item in allNews:
    if news_item.find('a', class_='sc-1eb5slv-0 sc-1308828-0 bwAAhr cmc-link') is not None:
        filteredNews.append(news_item.text)
for filteredParagraphs in filteredNews:
    print(f"{filteredParagraphs = }")
```


# Testing

to run the file "testSoup.py" you have to install urllib

```bash
python -m pip install urllib3
```

or 

``` bash
$ git clone git://github.com/urllib3/urllib3.git
$ python setup.py install
```

