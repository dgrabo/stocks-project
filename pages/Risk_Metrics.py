import streamlit as st
import pandas as pd
from lib.data import load_prices
from lib.metrics import ann_return, ann_vol, sharpe, max_drawdown, total_return

st.title("Risk Metrics")

tickers = st.text_input("Tickers: ", placeholder="AAPL, MSFT, TSLA")
tickers = [t.strip().upper() for t in tickers.split(",") if t.strip()]
period = st.selectbox("Period for the last: ", ["1y","5y","10y"], index=0)

if tickers:
    prices = load_prices(tickers, period)
    rets = prices.pct_change().dropna()
    rows = []
    for c in prices.columns:
        r = rets[c]
        rows.append({
            "Ticker": c,
            "Total return": round(total_return(r),3),
            "Ann.Return": round(ann_return(r),3),
            "Ann.Vol": round(ann_vol(r),3),
            "Sharpe": round(sharpe(r),3),
            "MaxDD": round(max_drawdown(r),3)

        })
    st.dataframe(pd.DataFrame(rows).set_index("Ticker"))
else:
    st.info("Search for at least one ticker.")

with st.container():
    st.write("Total return -> overall gain or loss of an asset or portfolio over the full period, measured from the first price to the last price")
    st.write("Annual return (arithmetic) -> expected yearly return of an asset or portfolio, extrapolated from the average daily returns (assuming ~252 trading days in a year)")
    st.write("Annual volatility -> the standard deviation of daily returns scaled to a yearly measure, representing the asset’s risk or variability")
    st.write("Sharpe ratio -> the risk-adjusted return, showing how much excess return an asset provides per unit of risk compared to a risk-free rate")
    st.write("Max drawdown -> the largest observed peak-to-trough decline in cumulative returns, measuring the worst potential loss from a high point")