# %%

import pyfolio as pf
import pandas as pd
import matplotlib.pyplot as plt

bitcoin_strategy_backtest = pd.read_csv('bitcoin_strategy_backtest.csv', index_col=0, parse_dates=True)
returns = bitcoin_strategy_backtest['returns']
print(returns.head())
#pf.create_returns_tear_sheet(returns)
#plt.show()
# %%
import json
bitcoin_strategy_backtest['positions'] = bitcoin_strategy_backtest['positions'].apply(lambda x: x.replace("'", '"'))
bitcoin_strategy_backtest['transactions'] = bitcoin_strategy_backtest['transactions'].apply(lambda x: x.replace("'", '"'))

positions = bitcoin_strategy_backtest[['positions', 'ending_cash']]
position_data = json.loads(positions.iloc[1, 0])

symbol = position_data[0]['symbol']
positions_edited = pd.DataFrame(0, index = positions.index, columns = [[symbol, 'cash']])
for index, row in positions.iterrows():
    position_data = json.loads(row['positions'])

    if position_data:
        positions_edited.loc[index, symbol] = position_data[0]['amount']   
    positions_edited.loc[index, 'cash'] = int(row['ending_cash'])
print(positions_edited.head()) 
# %%
transactions = bitcoin_strategy_backtest[['transactions']]
transactions_edited = pd.DataFrame(0, index = transactions.index, columns = [['txn_volume', 'txn_shares']])
for index, row in transactions.iterrows():
    transactions_data = json.loads(row['transactions'])

    if transactions_data:
        transactions_edited.loc[index, 'txn_volume'] = transactions_data[0]['transaction_money']   
        transactions_edited.loc[index, 'txn_shares'] = transactions_data[0]['amount']   
#print(returns.head())
#print(positions.head())
print(transactions.head())
# %%
