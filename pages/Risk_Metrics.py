import streamlit as st
import pandas as pd
from lib.data import load_prices
from lib.metrics import ann_return, ann_vol, sharpe, mac_drawdown

st.title("Risk Metrics")