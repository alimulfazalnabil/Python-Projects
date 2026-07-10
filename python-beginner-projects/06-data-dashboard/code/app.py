import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 150, 120, 200, 180],
    'Profit': [20, 35, 25, 50, 40]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Data Dashboard"),
    html.Hr(),
    html.Div([
        html.Div([dcc.Graph(id='sales-chart')], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([dcc.Graph(id='profit-chart')], style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        html.Label("Select Month Range:"),
        dcc.RangeSlider(0, 4, 1, value=[0, 4], id='month-slider')
    ], style={'marginTop': '30px'})
])

@app.callback(
    [Output('sales-chart', 'figure'), Output('profit-chart', 'figure')],
    [Input('month-slider', 'value')]
)
def update_charts(selected_range):
    filtered_df = df.iloc[selected_range[0]:selected_range[1]+1]
    sales_fig = px.bar(filtered_df, x='Month', y='Sales', title='Monthly Sales')
    profit_fig = px.line(filtered_df, x='Month', y='Profit', title='Monthly Profit')
    return sales_fig, profit_fig

if __name__ == '__main__':
    app.run_server(debug=True)
