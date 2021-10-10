import requests
from bs4 import BeautifulSoup
from selenium import webdriver
coin = input()
url = 'https://coinmarketcap.com/currencies/'+ str(coin) + "/news/" 

driver = webdriver.Firefox()
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page,'html.parser')


filteredNews = []
allNews = []
allNews = soup.findAll('div', class_='sc-16r8icm-0 jKrmxw container')

# print(allNews)

for news_item in allNews:
    if news_item.find('p', class_='sc-1eb5slv-0 svowul-3 ddtKCV') is not None:
        filteredNews.append(news_item.text)

for filteredParagraphs in filteredNews:
    print(f"{filteredParagraphs = }")




