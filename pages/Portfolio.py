import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

from lib.data import load_prices
from lib.metrics import ann_return, ann_vol, sharpe, max_drawdown
from lib.plots import line_prices
from components.input import sidebar_controls

st.title("Portfolio")

period, _ = sidebar_controls()
with st.sidebar:
    benchmark = st.text_input("Benchmark ticker", placeholder="SPY").strip().upper()
    rf_rate = st.number_input("Risk-free (annual)", value=0.0, step=0.005, help="Used for Sharpe ratio")

tickers_str = st.text_input("Tickers (comma): ", placeholder="AAPL, MSFT, TSLA")
tickers = [t.strip().upper() for t in tickers_str.split() if t.strip()]

if not tickers:
    st.info("Enter at least one ticker.")
    st.stop()

prices = load_prices(tickers, period)
prices = prices.dropna(axis=1, how="all")

if prices.empty:
    st.error("No price data returned for the given tickers/period.")
    st.stop()

st.subheader("Weights")
