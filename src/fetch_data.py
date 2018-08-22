import requests
from pymongo import MongoClient
from urllib.parse import quote_plus
from datetime import datetime
from fetch_symbols import write_symbols_to_file

# connect to db
client = MongoClient('localhost', 27017)

# returns the json data returned by the given url
def get_json_from_url(url):
  r = requests.get(url=url)
  return r.json()

# constructs the query string used for the api call
def get_query_string(identifier, start_time, end_time):
  TOKEN_URL = 'https://www.investopedia.com/markets/api/token/xignite/encrypted'
  token = get_json_from_url(TOKEN_URL)['token']

  query_string_list = [
    'IdentifierType=Symbol',
    'Identifier=' + identifier,
    'StartTime=' + quote_plus(start_time),
    'EndTime=' + quote_plus(end_time),
    'AdjustmentMethod=All',
    'IncludeExtended=False',
    'Precision=Hours',
    'Period=24',
    '_token=' + token,
    '_token_userid=46384'
  ]
  return '&'.join(query_string_list)

# returns the date and time formatted for the api call
def get_formatted_datetime(month, day, year):
  return '{:d}/{:d}/{:d} 9:30AM'.format(month, day, year)

def fill_database(identifier):
  # define constants
  API_BASE_URL = 'https://globalquotes.xignite.com/v3/xGlobalQuotes.json/GetChartBars?'

  # set up sample db and table
  db = client['stock_data']
  table = db[identifier]

  # clear the table
  table.delete_many({})

  # get the current time
  now = datetime.now()

  # define start and end dates
  end_month = now.month
  end_year = now.year
  start_month = end_month
  start_year = end_year
  start_date = get_formatted_datetime(start_month, 1, start_year)
  end_date = get_formatted_datetime(end_month, now.day, end_year)

  # define a variable to hold the api data
  chart_bars = True

  while (chart_bars != None):
    # decrement the start/end dates by 1 month
    end_month = start_month
    end_year = start_year
    start_month = end_month - 1
    if (start_month < 1):
      start_month = 12
      start_year = end_year - 1
    start_date = get_formatted_datetime(start_month, 1, start_year)
    end_date = get_formatted_datetime(end_month, 1, end_year)

    # fetch data from the api
    api_url = API_BASE_URL + get_query_string(identifier, start_date, end_date)
    api_data = get_json_from_url(api_url)
    chart_bars = api_data['ChartBars']
    if (chart_bars == None):
      break

    # insert the data in the db
    for chart_bar in chart_bars:
      id = table.insert_one(chart_bar).inserted_id
      print('inserted data: ', id, chart_bar)

def run():
  # get all the stock symbols
  try:
    f = open('stock_symbols.txt', 'r')
  except:
    write_symbols_to_file()
    f = open('stock_symbols.txt', 'r')

  # fill database
  stock_symbols = f.read().split('\n')
  for symbol in stock_symbols:
    fill_database(symbol)

run()
