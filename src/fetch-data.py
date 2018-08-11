import requests
from pymongo import MongoClient
from Bar import ChartBar

# connect to db
client = MongoClient('localhost', 27017)

# set up sample db and table
db = client['test_database']
table = db['stock_data']

# returns the json data returned by the given url
def get_JSON_from_url(url):
  r = requests.get(url=url)
  return r.json()

# constructs the query string used for the api call
def get_query_string():
  tokenUrl = 'https://www.investopedia.com/markets/api/token/xignite/encrypted'
  token = get_JSON_from_url(tokenUrl)['token']

  queryStringList = [
    'IdentifierType=Symbol',
    'Identifier=AAPL',
    'StartTime=8%2F9%2F2018+9%3A30+AM',
    'EndTime=8%2F9%2F2018+4%3A00+PM',
    'AdjustmentMethod=All',
    'IncludeExtended=False',
    'Precision=Minutes',
    'Period=1',
    '_token=' + token,
    '_token_userid=46384'
  ]
  return '&'.join(queryStringList)

apiUrl = 'https://globalquotes.xignite.com/v3/xGlobalQuotes.json/GetChartBars?' + get_query_string()
apiData = get_JSON_from_url(apiUrl)
chart_bars = apiData['ChartBars']

# format the data (in progress)
for n in range(0, len(chart_bars)):
  b = chart_bars[n]

  # insert this chart-bar in the db
  id = table.insert_one(b).inserted_id
  print('inserted data: ', id, b)

  # create new chart-bar object (we may not actually need this)
  bar = ChartBar(
    b['High'],
    b['EndDate'],
    b['StartDate'],
    b['Trades'],
    b['VWAP'],
    b['Volume'],
    b['Currency'],
    b['UTCOffset'],
    b['Session'],
    b['TWAP'],
    b['Low'],
    b['StartTime'],
    b['Close'],
    b['EndTime'],
    b['Open'],
    b['AdjustmentRatio'])

# print all the inserted items
for item in table.find({}):
  print(item)

# clear the table
table.delete_many({})
