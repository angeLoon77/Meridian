from config import PERIOD, MARGIN, DROP_LIMIT
from data import get_history
from analysis import calculate_average, calculate_percentage, get_status

def analyze_ticker(ticker):
    history = get_history(ticker, PERIOD)
    average, last_price = calculate_average(history)
    percentage = calculate_percentage(average, last_price)
    status = get_status(percentage, MARGIN, DROP_LIMIT)
    return {
        "ticker": ticker,
        "average": round(float(average), 2),
        "last_price": round(float(last_price), 2),
        "percentage": round(float(percentage), 2),
        "status": status,
    }

if __name__ == "__main__":
    print(analyze_ticker("MXRF11.SA"))