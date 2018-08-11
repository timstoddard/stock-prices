# simple class to hold stock data
class ChartBar:
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
    print('  >> High:            ' + str(self.High))
    print('  >> EndDate:         ' + str(self.EndDate))
    print('  >> StartDate:       ' + str(self.StartDate))
    print('  >> Trades:          ' + str(self.Trades))
    print('  >> VWAP:            ' + str(self.VWAP))
    print('  >> Volume:          ' + str(self.Volume))
    print('  >> Currency:        ' + str(self.Currency))
    print('  >> UTCOffset:       ' + str(self.UTCOffset))
    print('  >> Session:         ' + str(self.Session))
    print('  >> TWAP:            ' + str(self.TWAP))
    print('  >> Low:             ' + str(self.Low))
    print('  >> StartTime:       ' + str(self.StartTime))
    print('  >> Close:           ' + str(self.Close))
    print('  >> EndTime:         ' + str(self.EndTime))
    print('  >> Open:            ' + str(self.Open))
    print('  >> AdjustmentRatio: ' + str(self.AdjustmentRatio))
