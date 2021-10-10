from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest
class Test(unittest.TestCase):
   bs = None
   def setUpClass():
      url = 'https://coinmarketcap.com/currencies/bitcoin/news/'
      Test.bs = BeautifulSoup(urlopen(url), 'html.parser')
   def test_titleText(self):
      pageTitle = Test.bs.find('h1').get_text()
      self.assertEqual('Python', pageTitle);
   def test_contentExists(self):
      content = Test.bs.find('div',{'id':'mw-content-text'})
      self.assertIsNotNone(content)
if __name__ == '__main__':
   unittest.main()