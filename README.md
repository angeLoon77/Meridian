# Meridian

Meridian helps decide **when to make a monthly investment contribution**. It compares a stock's current price with its average price over the last 3 months and returns a simple status: buy, wait, or too low.

It does not predict the market. It only shows whether the current price is cheap or expensive compared to its recent history.

Meridian is one more of my personal projects built to solve real, everyday problems, like [AudioGrab](#) and [Backbone](#). This one came from my own need to get the most out of my monthly investment contribution.

> **Disclaimer:** this is a personal learning project, not financial advice.

## How it works

1. Fetches the price history of a ticker (via `yfinance`).
2. Calculates the 3-month average of the closing price.
3. Calculates the difference between the current price and that average.
4. Returns a status based on a configurable margin:

| Difference vs. average | Status |
|---|---|
| Up to `MARGIN` above the average (or any amount below it) | buy |
| More than `MARGIN` above the average | wait |
| Below `DROP_LIMIT` | too low (a sharp drop, worth a closer look) |

## Tech stack

- Python 3
- [yfinance](https://github.com/ranaroussi/yfinance) for market data
- pandas for calculations
- Flask for the API

## Project structure

```
Meridian/
├── main.py        # Flask app and API routes
├── service.py     # analyze_ticker(): combines data + analysis
├── data.py        # get_history(): fetches price history
├── analysis.py    # average, percentage difference, status
├── config.py      # PERIOD, MARGIN, DROP_LIMIT, TICKERS
└── requirements.txt
```

Each file has a single responsibility: `analysis.py` only does calculations and knows nothing about where the data comes from or how it is displayed.

## Getting started

```bash
git clone <repository-url>
cd Meridian

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS

pip install -r requirements.txt
python main.py
```

The server starts at `http://127.0.0.1:5000`.

## API

### `GET /api/analysis/<ticker>`

Brazilian tickers need the `.SA` suffix (e.g. `MXRF11.SA`).

Example: `/api/analysis/MXRF11.SA`

```json
{
  "ticker": "MXRF11.SA",
  "average": 9.16,
  "last_price": 9.44,
  "percentage": 0.03,
  "status": "Too High, Wait a little bit"
}
```

`percentage` is a fraction (`0.03` = 3%).

If the ticker does not exist or has no data, the API returns `404`:

```json
{ "error": "No Data Found for XXXX99.SA" }
```

## Configuration

Edit `config.py`:

| Setting | Default | Meaning |
|---|---|---|
| `PERIOD` | `"3mo"` | History window used for the average |
| `MARGIN` | `0.02` | How far above the average still counts as a buy (2%) |
| `DROP_LIMIT` | `-0.10` | Drop below the average that triggers "too low" (-10%) |
| `TICKERS` | `{}` | Tickers to follow, as `{"TICKER.SA": "Name"}` |

## Roadmap

- [x] Data fetching with empty-data handling
- [x] Average, percentage and status calculation
- [x] Flask API with error handling
- [ ] Fixed status codes (`buy`, `wait`, `too_low`) for the front end
- [ ] Front end (HTML, CSS and JavaScript)
- [ ] Support for multiple tickers
- [ ] Backtest of the rule against historical data
- [ ] Suggestion for splitting the monthly contribution
- [ ] Automatic alerts (email or phone notifications) when the price is in the buy zone

## What I learned

- Separating responsibilities across modules
- Working with market data using yfinance and pandas
- Building a JSON API with Flask
