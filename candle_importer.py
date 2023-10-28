from jesse.research import import_candles
import time
import requests

exchange = "Binance Perpetual Futures"
symbols = ['BTC-USDT', 'ETH-USDT']
start_date = "2018-06-01"


def fetch_candles(exchange, symbol, start_date):
    try:
        import_candles(exchange, symbol, start_date, show_progressbar=True)
        return True
    except requests.exceptions.ConnectionError:
        print("Network is down. Retrying in 5 minutes.")
        return False


# Run indefinitely
while True:
    for symbol in symbols:
        success = False
        while not success:
            success = fetch_candles(exchange, symbol, start_date)
            if not success:
                time.sleep(5)  # Wait for 5 Seconds before retrying

    print("Completed fetching candles for all symbols. Sleeping for 24 hours.")
    time.sleep(86400)  # Sleep for 24 hours
