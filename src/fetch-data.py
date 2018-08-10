# simple class to hold stock data
class Bar:
  def __init__(self, High, EndDate, StartDate, Trades, VWAP, Volume, Currency, UTCOffset, Session, TWAP, Low, StartTime, Close, EndTime, Open, AdjustmentRatio):
    self.High = High
    self.EndDate = EndDate
    self.StartDate = StartDate
    self.Trades = Trades
    self.VWAP = VWAP
    self.Volume = Volume
    self.Currency = Currency
    self.UTCOffset = UTCOffset
    self.Session = Session
    self.TWAP = TWAP
    self.Low = Low
    self.StartTime = StartTime
    self.Close = Close
    self.EndTime = EndTime
    self.Open = Open
    self.AdjustmentRatio = AdjustmentRatio
  
  def print_data(self):
    print '  >> High:            ' + str(self.High)
    print '  >> EndDate:         ' + str(self.EndDate)
    print '  >> StartDate:       ' + str(self.StartDate)
    print '  >> Trades:          ' + str(self.Trades)
    print '  >> VWAP:            ' + str(self.VWAP)
    print '  >> Volume:          ' + str(self.Volume)
    print '  >> Currency:        ' + str(self.Currency)
    print '  >> UTCOffset:       ' + str(self.UTCOffset)
    print '  >> Session:         ' + str(self.Session)
    print '  >> TWAP:            ' + str(self.TWAP)
    print '  >> Low:             ' + str(self.Low)
    print '  >> StartTime:       ' + str(self.StartTime)
    print '  >> Close:           ' + str(self.Close)
    print '  >> EndTime:         ' + str(self.EndTime)
    print '  >> Open:            ' + str(self.Open)
    print '  >> AdjustmentRatio: ' + str(self.AdjustmentRatio)

# get the data from the api hehe
import urllib2
import json
# NOTE: LINKS WILL EXPIRE, IF NO DATA IS RETURNED GET A NEW ONE
url = "https://globalquotes.xignite.com/v3/xGlobalQuotes.json/GetChartBars?IdentifierType=Symbol&Identifier=AAPL&StartTime=8%2F9%2F2018+9%3A30+AM&EndTime=8%2F9%2F2018+4%3A00+PM&AdjustmentMethod=All&IncludeExtended=False&Precision=Minutes&Period=1&_token=15B2186D55CB1AEFD12E7C2C2DE9CBB9110DFB516C5307188C5E44131653A7F1F21A023037A60A789E068C4C53E3AFE7F25A08BC&_token_userid=46384"
req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
chart_bars = json['ChartBars']

# format the data (in progress)
for n in range(0, len(chart_bars)):
  b = chart_bars[n]
  # create bar object
  bar = Bar(
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

  # semi fancy printing
  print 'BAR ' + str(n)
  bar.print_data()
  print '\n'