import yfinance as yf

def get_history(ticker_name, history):
    ticker = yf.Ticker(ticker_name)
    result = ticker.history(period=history)
    if result.empty:
        raise ValueError(f"No Data Found for {ticker_name}")
    return result
