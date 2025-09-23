import streamlit as st
import yfinance as yf
import pandas as pd

@st.cache_data(show_spinner=False)
def load_prices(tickers, period="1y"):
    df = yf.download(tickers, period=period, auto_adjust=True, progress=False)
    prices = df["Close"]
    if isinstance(prices, pd.Series):
        prices = prices.to_frame(name=tickers[0])
    return prices.dropna(how="all")