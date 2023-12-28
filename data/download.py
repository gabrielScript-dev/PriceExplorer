import yfinance
import pandas

def download_data(ticker: str) -> pandas.DataFrame:
    data = yfinance.download(ticker)

    return data