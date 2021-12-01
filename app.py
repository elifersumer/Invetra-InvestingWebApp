from flask import Flask, jsonify
from flask_cors import CORS
from yahoofinancials import YahooFinancials
from datetime import date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

aapl_symbol = 'AAPL'

end_time = date.today()
start_time = end_time - timedelta(days=65)

end = end_time.strftime('%Y-%m-%d')
start = start_time.strftime('%Y-%m-%d')

json_prices_aapl = YahooFinancials(aapl_symbol).get_historical_price_data(start, end, 'daily')

prices_aapl = pd.DataFrame(json_prices_aapl[aapl_symbol]['prices'])[['formatted_date','close']]

prices_aapl.sort_index(ascending=False, inplace=True)

prices_aapl['returns'] = (np.log(prices_aapl.close / prices_aapl.close.shift(-1)))

daily_std_aapl = np.std(prices_aapl.returns)

std_aapl = daily_std_aapl*252**0.5

fig_aapl, ax_aapl = plt.subplots(1, 1, figsize=(7,5))

n, bins, patches = ax_aapl.hist(prices_aapl.returns.values , bins=50, alpha=0.65, color='blue')

ax_aapl.set_xlabel('log return of stock price')
ax_aapl.set_ylabel('frequency of log return')
ax_aapl.set_title('Historical volatility for '+aapl_symbol)

x_corr_aapl = ax_aapl.get_xlim()
y_corr_aapl = ax_aapl.get_ylim()

header = y_corr_aapl[1]/5
y_corr_aapl = (y_corr_aapl[0], y_corr_aapl[1] + 1)
ax_aapl.set_ylim(y_corr_aapl[0], y_corr_aapl[1])

x = x_corr_aapl[0] + (x_corr_aapl[1]-x_corr_aapl[0])/30
y = y_corr_aapl[1] + (y_corr_aapl[1]-y_corr_aapl[0])/15

ax_aapl.text(x, y, 'Annualized Volatility: ' + str(daily_std_aapl)+ '%', fontsize=8, fontweight='bold')

x = x_corr_aapl[0] + (x_corr_aapl[1]+x_corr_aapl[0])/15
y -= (y_corr_aapl[1]-y_corr_aapl[0])/20

img_name_aapl= 'aapl_vol.png'

fig_aapl.tight_layout()
fig_aapl.savefig("C:/Users/elife/OneDrive/Masaüstü/invetra/invetra/assets/aapl_vol.png")



usd_symbol = 'USD'

json_prices_usd = YahooFinancials(usd_symbol).get_historical_price_data(start, end, 'daily')

prices_usd = pd.DataFrame(json_prices_usd[usd_symbol]['prices'])[['formatted_date','close']]

prices_usd.sort_index(ascending=False, inplace=True)

prices_usd['returns'] = (np.log(prices_usd.close / prices_usd.close.shift(-1)))

daily_std_usd = np.std(prices_usd.returns)

std_usd = daily_std_usd*252**0.5

fig_usd, ax_usd = plt.subplots(1, 1, figsize=(7,5))

n_usd, bins_usd, patches_usd = ax_usd.hist(prices_usd.returns.values , bins=50, alpha=0.65, color='blue')

ax_usd.set_xlabel('log return of stock price')
ax_usd.set_ylabel('frequency of log return')
ax_usd.set_title('Historical volatility for '+aapl_symbol)

x_corr_usd = ax_usd.get_xlim()
y_corr_usd = ax_usd.get_ylim()

header_usd = y_corr_usd[1]/5
y_corr_usd = (y_corr_usd[0], y_corr_usd[1] + 1)
ax_usd.set_ylim(y_corr_usd[0], y_corr_usd[1])

x_usd = x_corr_usd[0] + (x_corr_usd[1]-x_corr_usd[0])/30
y_usd = y_corr_usd[1] + (y_corr_usd[1]-y_corr_usd[0])/15

ax_usd.text(x, y, 'Annualized Volatility: ' + str(daily_std_usd)+ '%', fontsize=8, fontweight='bold')

x_usd = x_corr_usd[0] + (x_corr_usd[1]+x_corr_usd[0])/15
y_usd -= (y_corr_usd[1]-y_corr_usd[0])/20

img_name_usd= 'usd_vol.png'

fig_usd.tight_layout()
fig_usd.savefig('C:/Users/elife/OneDrive/Masaüstü/invetra/invetra/assets/usd_vol.png')

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
  data = {}

  data['data'] = {
    "usd":{"volatility":daily_std_usd, "image":img_name_usd},
    "aapl":{"volatility":daily_std_aapl, "image":img_name_aapl}
    }
  return jsonify(data)

if __name__ == '__main__':
  app.run(debug=True)
