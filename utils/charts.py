from dash import dcc
import plotly.graph_objs as go

def temperature_chart(df):
    return dcc.Graph(
        figure={
            'data': [go.Scatter(x=df['Time'], y=df["Temperature (°C)"], mode='lines',
                                name='Temperature (°C)', line=dict(color='#212A31', width=2))],
            'layout': go.Layout(title='Temperature Forecast', xaxis={'title': 'Time'},
                                yaxis={'title': 'Temperature (°C)'}, paper_bgcolor='#f9f9f9',
                                plot_bgcolor='#f9f9f9', xaxis_tickangle=-45,
                                title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
        }
    )

def humidity_chart(df):
    return dcc.Graph(
        figure={
            'data': [go.Scatter(x=df['Time'], y=df["Humidity (%)"], mode='lines',
                                name='Humidity (%)', line=dict(color='#ff7f0e', width=2))],
            'layout': go.Layout(title='Humidity Forecast', xaxis={'title': 'Time'},
                                yaxis={'title': 'Humidity'}, paper_bgcolor='#f9f9f9',
                                plot_bgcolor='#f9f9f9', xaxis_tickangle=-45,
                                title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
        }
    )

def wind_chart(df):
    return dcc.Graph(
        figure={
            'data': [go.Scatter(x=df['Time'], y=df["Wind Speed (m/s)"], mode='lines',
                                name='Wind Speed (m/s)', line=dict(color='#2ca02c', width=2))],
            'layout': go.Layout(title='Wind Speed Forecast', xaxis={'title': 'Time'},
                                yaxis={'title': 'Wind Speed'}, paper_bgcolor='#f9f9f9',
                                plot_bgcolor='#f9f9f9', xaxis_tickangle=-45,
                                title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
        }
    )
