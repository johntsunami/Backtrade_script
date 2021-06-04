import backtrader
import datetime
from strategy import TestStrategy

cerebro = backtrader.Cerebro()

cerebro.broker.set_cash(10000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

data = backtrader.feeds.YahooFinanceCSVData(
    dataname='JNJ_Daily.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2010, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2021, 12, 31),
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=1)

cerebro.run()

cerebro.plot()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
