import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots


data = pd.read_csv('./COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv', sep=',')

china = data.query("Region == 'China'").iloc[:, 4:]
other = data.query("Region != 'China'").iloc[:, 4:]
dates = data.columns.values[4:]

china_total = china.sum();
other_total = other.sum();


fig = make_subplots(rows=2, cols=1)

fig.add_trace(go.Scatter(x=dates, y=china_total, mode='lines', name='china'), row=1, col=1)
fig.add_trace(go.Scatter(x=dates, y=other_total, mode='lines', name='outside china'),row=2, col=1)
plotly.offline.plot(fig, filename='plot.html')
