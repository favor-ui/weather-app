from dash import dcc, html

layout = html.Div([
    html.Div(
        className="banner",
        children=[
            html.H1("Real-Time Weather Dashboard", style={'textAlign': 'center', 'color': '#ffffff'}),
            html.P("Get real-time weather updates and visualize temperature, humidity, and wind speed trends by city.",
                   style={'textAlign': 'center', 'color': '#ffffff'})
        ],
        style={
            'backgroundColor': '#212A31',
            'padding': '10px'
        }
    ),
    html.Div(
        className="user-input",
        children=[
            html.Div([
                html.Label("Enter City Name", style={'fontWeight': 'bold'}),
                dcc.Input(id='city-name', type='text', value='San Francisco', style={'width': '100%'}),
            ], style={'margin-bottom': '20px'}),
            html.Div([
                html.Label("Select forecast duration (hours)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='forecast-duration', min=12, max=48, value=24, step=12,
                           marks={12: '12h', 24: '24h', 36: '36h', 48: '48h'},
                           tooltip={'always_visible': True, 'placement': 'bottom'})
            ], style={'margin-bottom': '20px'}),
            html.Div([
                html.Label("Choose weather parameters to display:", style={'fontWeight': 'bold'}),
                dcc.Checklist(id='parameter-options',
                              options=[
                                  {'label': "Temperature (°C)", 'value': "Temperature (°C)"},
                                  {'label': "Humidity (%)", 'value': "Humidity (%)"},
                                  {'label': "Wind Speed (m/s)", 'value': "Wind Speed (m/s)"}
                              ],
                              value=["Temperature (°C)", "Humidity (%)"],
                              inputStyle={'margin-right': '5px', 'margin-left': '10px'})
            ], style={'margin-bottom': '20px'}),
            html.Button('Get Weather Data', id='get-weather-data', n_clicks=0,
                        style={'backgroundColor': '#212A31', 'color': '#ffffff', 'fontWeight': 'bold', 'border': 'none', 'padding': '10px 20px', 'cursor': 'pointer'})
        ],
        style={
            'backgroundColor': '#f9f9f9',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0px 0px 15px rgba(0, 0, 0, 0.1)'
        }
    ),
    html.Div(id='current-weather-summary', style={'margin-top': '20px'}),
    html.Div(id='temperature-graph', style={'margin-top': '20px'}),
    html.Div(id='humidity-graph', style={'margin-top': '20px'}),
    html.Div(id='wind-speed-graph', style={'margin-top': '20px'})
], style={'maxWidth': '800px', 'margin': '0 auto'})
