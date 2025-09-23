import plotly.express as px

def line_prices(df, title):
    return px.line(df, title=title)

def heatmap_corr(corr):
    return px.imshow(corr, text_auto=True, title="Correlation", zmin= -1, zmax = 1, color_continuous_scale="RdBu_r")