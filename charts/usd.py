import plotly
import plotly.express as px
import numpy as np
import pandas as pd
import yfinance as yf
import warnings

import cufflinks as cf
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode
import matplotlib.pyplot as plt
cf.go_offline()
init_notebook_mode() 
TICKER = "USD"

df = yf.download(TICKER, 
                 start="2021-09-01", 
                 end="2021-11-23")

df["Close"].plot(title=f"{TICKER}'s stock price")
qf = cf.QuantFig(df, title="Apple's stock price in 2021", name='AAPL')
qf.iplot()

fig = go.Figure(data=
    [go.Candlestick(x=df.index,
                    open=df["Open"],
                    high=df["High"],
                    low=df["Low"],
                    close=df["Close"])]
)

fig.update_layout(
    title=f"{TICKER}'s adjusted stock price",
    yaxis_title="Price ($)"
)
fig.show()
plotly.offline.plot(fig,filename='positives.html',config={'displayModeBar': False})


