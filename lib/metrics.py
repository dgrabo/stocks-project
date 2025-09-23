import numpy as np

def ann_return(returns): 
    return returns.mean() * 252

def ann_vol(returns):
    return returns.std() * np.sqrt(252)

def sharpe(returns, rf=0.0):
    mu, sigma = ann_return(returns), ann_vol(returns)
    return (mu - rf)/sigma if sigma>0 else float("nan")

def mac_drawdown(returns):
    import pandas as pd
    cum = (1 + returns.fillna(0)).cumprod()
    dd = (cum / cum.cummax()) - 1
    return dd.min()