import plotly.express
from data.download import download_data

def plot_line_i(ticker:str):

    data = download_data(ticker)

    fig = plotly.express.line(
        data.reset_index(),
        x = 'Date', y = 'Close', title = ticker,
        labels = {'Close': 'Fechamento', 'Date': 'Data'}
    )

    return fig