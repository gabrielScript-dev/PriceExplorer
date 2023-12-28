import plotly.express
from data.download import download_data

def plot_line_i(ticker:str):

    data = download_data(ticker)
    data['SMA'] = data['Close'].rolling(window=9).mean()
    data['LMA'] = data['Close'].rolling(window=72).mean()

    fig = plotly.express.line(
        data.reset_index(),
        x = 'Date', 
        y = ['Close', 'SMA', 'LMA'], 
        title = 'BBAS3',
        labels = {'Close': 'Fechamento', 'Date': 'Data'},
        color_discrete_map= {'Close': 'black', 'SMA': 'red', 'LMA': 'blue'}
    )   

    from plot.interactive import plot_line_i

    plot_line_i('CPLE3.SA')