# Coinmarketcap API Data Pull
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
from alpha_vantage.cryptocurrencies import CryptoCurrencies

#https://medium.com/coinmonks/predicting-cryptocurrency-markets-with-machine-learning-474a2f4f5da3

#pip install alpha_vantage

def crypto_data_gen():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '0ca60949-1e35-4a77-80a6-2fc1525ab2a5',
  }



  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  cc = CryptoCurrencies(key='3QGJ0HJ5S0G4B7H4', output_format='pandas')

  BTC, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')# Note: This previous line is repeated for each coin that you want to pull, updating the name and symbol as necessary# Indexed each dataset 
  BTC = BTC.assign(ticker='BTC').sort_index()
  # Develop .csv file for each coin dataset
  BTC.to_csv('BTC.csv', encoding='utf-8')
  # Restructure the Data
  df_merge = pd.concat([BTC])
  df_merge.sort_index()

  # Drop Duplicate Columns
  df_merge = df_merge.drop(columns=['1b. open (USD)',
                                    '2b. high (USD)',
                                    '3b. low (USD)',
                                    '4b. close (USD)'])

  # Rename Columns
  df_merge.columns = ['open', 'high', 'low', 'close', 'volume', 'marketcap', 'ticker']


