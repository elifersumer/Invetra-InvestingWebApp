from flask import Flask, jsonify
from flask_cors import CORS
from yahoofinancials import YahooFinancials
from datetime import date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

api_key= 'b6b90c304ec78fa2c95ce348d5d2447a'
def bollingerbands(aapl_symbol):
    stockprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{aapl_symbol}?timeseries=365&apikey={api_key}")
    stockprices = stockprices.json()

    stockprices = stockprices['historical'][-150:]
    
    stockprices = pd.DataFrame.from_dict(stockprices)
    stockprices = stockprices.set_index('date')
    stockprices['MA20'] = stockprices['close'].rolling(window=20).mean()
    stockprices['20dSTD'] = stockprices['close'].rolling(window=20).std() 

    stockprices['Upper'] = stockprices['MA20'] + (stockprices['20dSTD'] * 2)
    stockprices['Lower'] = stockprices['MA20'] - (stockprices['20dSTD'] * 2)
    
    stockprices[['close','MA20','Upper','Lower']].plot(figsize=(10,4))
    plt.grid(True)
    plt.title(aapl_symbol + ' Bollinger Bands')
    plt.axis('tight')
    plt.ylabel('Price')
    plt.savefig('C:/Users/elifersumer/Projects/Invetra-InvestingWebApp-1/invetra/static/apple.png', bbox_inches='tight')
    
bollingerbands('AAPL')
    

aapl_symbol = 'AAPL'

end_time = date.today()
start_time = end_time - timedelta(days=365)

end = end_time.strftime('%Y-%m-%d')
start = start_time.strftime('%Y-%m-%d')

json_prices_aapl = YahooFinancials(aapl_symbol).get_historical_price_data(start, end, 'daily')

prices_aapl = pd.DataFrame(json_prices_aapl[aapl_symbol]['prices'])[['formatted_date','close']]

prices_aapl.sort_index(ascending=False, inplace=True)

prices_aapl['returns'] = (np.log(prices_aapl.close / prices_aapl.close.shift(-1)))

daily_std_aapl = np.std(prices_aapl.returns)

std_aapl = daily_std_aapl*252**0.5

fig_aapl, ax_aapl = plt.subplots(1, 1, figsize=(7,5))

n, bins, patches = ax_aapl.hist(prices_aapl.returns.values , bins=50, alpha=0.65, color='#070E4D')

ax_aapl.set_xlabel('Log Return of Stock Price')
ax_aapl.set_ylabel('Frequency of Log Return')
ax_aapl.set_title('1Y Time Period Historical Volatility for '+aapl_symbol)

x_corr_aapl = ax_aapl.get_xlim()
y_corr_aapl = ax_aapl.get_ylim()

header = y_corr_aapl[1]/5
y_corr_aapl = (y_corr_aapl[0], y_corr_aapl[1] + 1)
ax_aapl.set_ylim(y_corr_aapl[0], y_corr_aapl[1])

x = x_corr_aapl[0] + (x_corr_aapl[1]-x_corr_aapl[0])/30
y = y_corr_aapl[1] + (y_corr_aapl[1]-y_corr_aapl[0])/15

x = x_corr_aapl[0] + (x_corr_aapl[1]+x_corr_aapl[0])/15
y -= (y_corr_aapl[1]-y_corr_aapl[0])/20

img_name_aapl= 'aapl_vol.png'

fig_aapl.tight_layout()
fig_aapl.savefig("C:/Users/elifersumer/Projects/Invetra-InvestingWebApp-1/invetra/assets/aapl_vol.png")



tsla_symbol = 'TSLA'

json_prices_tsla = YahooFinancials(tsla_symbol).get_historical_price_data(start, end, 'daily')

prices_tsla = pd.DataFrame(json_prices_tsla[tsla_symbol]['prices'])[['formatted_date','close']]

prices_tsla.sort_index(ascending=False, inplace=True)

prices_tsla['returns'] = (np.log(prices_tsla.close / prices_tsla.close.shift(-1)))

daily_std_tsla = np.std(prices_tsla.returns)

std_tsla = daily_std_tsla*252**0.5

fig_tsla, ax_tsla = plt.subplots(1, 1, figsize=(7,5))

n_tsla, bins_tsla, patches_tsla = ax_tsla.hist(prices_tsla.returns.values , bins=50, alpha=0.65, color='#070E4D')

ax_tsla.set_xlabel('Log Return of Stock Price')
ax_tsla.set_ylabel('Frequency of Log Return')
ax_tsla.set_title('1Y Time Period Historical Volatility for '+tsla_symbol)

x_corr_tsla = ax_tsla.get_xlim()
y_corr_tsla = ax_tsla.get_ylim()

header_tsla = y_corr_tsla[1]/5
y_corr_tsla = (y_corr_tsla[0], y_corr_tsla[1] + 1)
ax_tsla.set_ylim(y_corr_tsla[0], y_corr_tsla[1])

x = x_corr_tsla[0] + (x_corr_tsla[1]-x_corr_tsla[0])/30
y = y_corr_tsla[1] + (y_corr_tsla[1]-y_corr_tsla[0])/15

x = x_corr_tsla[0] + (x_corr_tsla[1]+x_corr_tsla[0])/15
y -= (y_corr_tsla[1]-y_corr_tsla[0])/20

img_name_tsla = "tsla_vol.png"

fig_tsla.tight_layout()
fig_tsla.savefig("C:/Users/elifersumer/Projects/Invetra-InvestingWebApp-1/invetra/assets/tsla_vol.png")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
  data = {}

  data['data'] = {
    "tsla":{"volatility":daily_std_tsla, "image":img_name_tsla},
    "aapl":{"volatility":daily_std_aapl, "image":img_name_aapl}
    }
  return jsonify(data)

if __name__ == '__main__':
  app.run(debug=True)