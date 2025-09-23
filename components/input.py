import streamlit as st

def sidebar_controls():
    with st.sidebar:
        period = st.selectbox("Period", ["6mo","1y","5y","10y"], index=1)
        normalize = st.checkbox("Normalize to 100", value=True)
        return period, normalize
    
    