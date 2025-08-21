from dash import dcc, html, Input, Output
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objs as go

from app_core import app
from services.geocoding import get_coordinates
from services.weather import get_weather_data

@app.callback(
    [Output('current-weather-summary', 'children'),
     Output('temperature-graph', 'children'),
     Output('humidity-graph', 'children'),
     Output('wind-speed-graph', 'children')],
    [Input('get-weather-data', 'n_clicks')],
    [Input('city-name', 'value'),
     Input('forecast-duration', 'value'),
     Input('parameter-options', 'value')]
)
def update_weather(n_clicks, city_name, forecast_duration, parameter_options):
    if n_clicks > 0:
        lat, lon = get_coordinates(city_name)
        if lat is not None and lon is not None:
            data = get_weather_data(lat, lon, forecast_duration)
            if data:
                times = [datetime.now() + timedelta(hours=i) for i in range(forecast_duration)]
                df = pd.DataFrame({"Time": times})

                current_summary = html.Div([
                    html.H3("Current Weather Summary", style={'textAlign': 'center', 'color': '#212A31'}),
                    html.Div([
                        html.Div([html.H4("✨ Temperature"), html.P(f"{data['current']['temperature_2m']} °C")],
                                 style={'textAlign': 'center','display': 'inline-block', 'margin-right': '20px', 'backgroundColor': '#f9f9f9', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)'}),
                        html.Div([html.H4("💧 Humidity"), html.P(f"{data['current']['relative_humidity_2m']} %")],
                                 style={'textAlign': 'center','display': 'inline-block', 'margin-right': '20px', 'backgroundColor': '#f9f9f9', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)'}),
                        html.Div([html.H4("🌬️ Wind Speed"), html.P(f"{data['current']['wind_speed_10m']} m/s")],
                                 style={'textAlign': 'center','display': 'inline-block', 'backgroundColor': '#f9f9f9', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)'})
                    ], style={'textAlign': 'center'})
                ])

                temperature_graph = html.Div()
                if "Temperature (°C)" in parameter_options:
                    df["Temperature (°C)"] = data['hourly']['temperature_2m'][:forecast_duration]
                    temperature_graph = dcc.Graph(
                        figure={
                            'data': [go.Scatter(x=df['Time'], y=df["Temperature (°C)"], mode='lines', name='Temperature (°C)', line=dict(color='#212A31', width=2))],
                            'layout': go.Layout(title='Temperature Forecast', xaxis={'title': 'Time'}, yaxis={'title': 'Temperature (°C)'},
                                                paper_bgcolor='#f9f9f9', plot_bgcolor='#f9f9f9',
                                                xaxis_tickangle=-45, title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
                        }
                    )

                humidity_graph = html.Div()
                if "Humidity (%)" in parameter_options:
                    df["Humidity (%)"] = data['hourly']['relative_humidity_2m'][:forecast_duration]
                    humidity_graph = dcc.Graph(
                        figure={
                            'data': [go.Scatter(x=df['Time'], y=df["Humidity (%)"], mode='lines', name='Humidity (%)', line=dict(color='#ff7f0e', width=2))],
                            'layout': go.Layout(title='Humidity Forecast', xaxis={'title': 'Time'}, yaxis={'title': 'Humidity'},
                                                paper_bgcolor='#f9f9f9', plot_bgcolor='#f9f9f9',
                                                xaxis_tickangle=-45, title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
                        }
                    )

                wind_speed_graph = html.Div()
                if "Wind Speed (m/s)" in parameter_options:
                    df["Wind Speed (m/s)"] = data['hourly']['wind_speed_10m'][:forecast_duration]
                    wind_speed_graph = dcc.Graph(
                        figure={
                            'data': [go.Scatter(x=df['Time'], y=df["Wind Speed (m/s)"], mode='lines', name='Wind Speed (m/s)', line=dict(color='#2ca02c', width=2))],
                            'layout': go.Layout(title='Wind Speed Forecast', xaxis={'title': 'Time'}, yaxis={'title': 'Wind Speed'},
                                                paper_bgcolor='#f9f9f9', plot_bgcolor='#f9f9f9',
                                                xaxis_tickangle=-45, title_x=0.5, title_font={'size': 24, 'color': '#212A31'})
                        }
                    )

                return current_summary, temperature_graph, humidity_graph, wind_speed_graph
    return html.Div(), html.Div(), html.Div(), html.Div()
