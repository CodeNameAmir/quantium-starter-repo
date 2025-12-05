# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

app = Dash()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "all_sales.csv")
df = pd.read_csv(csv_path)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "all_sales.csv")
df = pd.read_csv(csv_path)

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Soul Foods Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales Amount"
    }
)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
