import plotly.express as px



def hist_show_spread():
    df = px.data.tips()
    # Here we use a column with categorical data
    fig = px.histogram(df, x="day")
    fig.show()















