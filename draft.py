import plotly.express
from data.download import download_data

data = download_data('BBAS3.SA')

data['SMA'] = data['Close'].rolling(window=9).mean()
data['LMA'] = data['Close'].rolling(window=72).mean()


plotly.express.line(
    data.reset_index(),
    x = 'Date', 
    y = ['Close', 'SMA', 'LMA'], 
    title = 'BBAS3',
    labels = {'Close': 'Fechamento', 'Date': 'Data'},
    color_discrete_map= {'Close': 'black', 'SMA': 'red', 'LMA': 'blue'}
)

