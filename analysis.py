def get_low_high(data1):
    maximum = data1["High"].max()
    minimum = data1["Low"].min()

    return maximum, minimum

def calculate_average(data1):
    closes = data1["Close"]
    average = closes.mean()
    last_price = closes.iloc[-1]

    return average, last_price

def calculate_percentage(average, last_price):
    percentage = (last_price - average) / average

    return percentage

def get_status(percentage, margin, DROP_LIMIT):
    if percentage <= DROP_LIMIT:
        return "too_low"
    elif percentage <= margin:
        return "buy"
    else:
        return "wait"

