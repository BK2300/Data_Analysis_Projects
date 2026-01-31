# This tab is for the basic EDA functions with plotly

import plotly.express as px
import pandas as pd


def hist_show_spread(df: pd.Dataframe):
# This function is a simple histogram, showing the dpread between "TV-shows" and "Movies"
    df = px.data.tips()
    fig = px.histogram(df, x="day")
    fig.show()

def













