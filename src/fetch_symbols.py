import requests
from bs4 import BeautifulSoup

def get_texts(url, texts):
  # grab the first page of the list
  page = requests.get(url)

  # initialize beautiful soup
  soup = BeautifulSoup(page.text, 'html.parser')

  # get the text of an item
  def get_text(item):
    return item.find('a').get_text()

  # get the text in the link elements
  list_wrapper = soup.find(class_='inner all-symbols-content')
  if (list_wrapper == None):
    return False
  list_ = list_wrapper.find('ul')
  items = list_.find_all('li')
  items = map(get_text, items)
  for i in items:
    texts.append(i)
  print('finished scraping ' + url)

def get_all_symbols():
  texts = []

  # get the first page
  get_texts('https://www.investopedia.com/markets/stocks', texts)
  counter = 1
  data = True
  while (data != False):
    # get all the following pages
    data = get_texts('https://www.investopedia.com/markets/stocks/?page=' + str(counter), texts)
    counter += 1

  return texts

def write_symbols_to_file():
  # get all the symbols
  symbols = get_all_symbols()

  # write symbols to a file
  f = open('stock_symbols.txt', 'w')
  f.write('\n'.join(symbols))
