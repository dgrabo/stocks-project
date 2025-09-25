import streamlit as st
import pandas as pd
from lib.data import load_prices
from lib.plots import line_prices
from components.input import sidebar_controls

st.title("Prices")

period, normalize = sidebar_controls()
tickers = st.text_input("TIcker (comma):", placeholder="AAPL, MSFT, TSLA")
tickers = [t.strip().upper() for t in tickers.split(",") if t.strip()]

if tickers:
        prices = load_prices(tickers, period)

        if prices is None or prices.empty:
            st.error("No price data returned for given tickers/period.")
            st.stop()

        if normalize:
            try:
                base = prices.ffill().bfill().iloc[0]
                prices = prices.divide(base) * 100
            except IndexError:
                st.error("Not enough data to normalize (dataset is empty).")
                st.stop()    
            except Exception as e:
                st.error(f"Normalization error: {e}")
                st.stop()
        
        st.plotly_chart(line_prices(prices, f"Prices({period})" + (" [norm=100]" if normalize else "")),
                        use_container_width=True)
        st.dataframe(prices.tail())

else:
    st.info("Empty input")