from frarb import FundingRateArbitrage
import pandas as pd

fr = FundingRateArbitrage()

# fetch all perp funding rate on binance
fr_binance = fr.fetch_all_funding_rate(exchange='binance')

# get commission on binance with futures, maker
cm_binance = fr.get_commission(exchange='binance', trade='futures', taker=False)

fr = FundingRateArbitrage()

# figure funding rate history
fr.fetch_funding_rate_history(exchange='binance', symbol='BTC/USDT:USDT')

# fr.figure_funding_rate_history(exchange='binance', symbol='BTC/USDT:USDT')

# result = fr.display_large_divergence_multi_exchange(display_num=5, sorted_by='divergence')
result = fr.display_one_by_one_multi_exchanges(display_num=5)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(result)
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

