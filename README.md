# candle-importer-script

This script is designed to assist traders and data analysts who need continuous access to fresh market candles in their database for backtesting. It fetches market candles for any given exchange, symbols, and starting date, and does so indefinitely to ensure your database is always up-to-date.

## Features

- **Multiple Symbols**: Users can specify as many trading pairs (symbols) as they want.
- **Customizable Starting Date**: You can choose any starting date for fetching the candles.
- **Automatic Retry**: The script automatically retries in case of a network failure.
- **Selective Fetch**: It only fetches candles that are not already present in the database, skipping the ones that are. 
- **24-hour Sleep**: Once all the candles for the specified symbols have been fetched, the script sleeps for 24 hours before fetching again.

## How it Works

1. **Initialization**: Define the `exchange`, `symbols`, and `start_date`.
    ```python
    exchange = "Binance Perpetual Futures"
    symbols = ['BTC-USDT', 'ETH-USDT']
    start_date = "2018-06-01"
    ```

2. **Fetching Function**: Uses the `fetch_candles` function to fetch candles.
    ```python
    def fetch_candles(exchange, symbol, start_date):
        # ... (fetching logic)
    ```

3. **Error Handling**: If a network issue occurs, the function will print an error message and return `False`.
    ```python
    except requests.exceptions.ConnectionError:
        print("Network is down. Retrying in 5 minutes.")
        return False
    ```

4. **Continuous Operation**: The script runs indefinitely.
    ```python
    while True:
        # ... (fetching loop)
    ```

5. **Retries**: If fetching fails, it will wait for 5 seconds before retrying.

6. **24-Hour Sleep**: Once the candles for all symbols are fetched, the script will sleep for 24 hours before it runs again.
    ```python
    print("Completed fetching candles for all symbols. Sleeping for 24 hours.")
    time.sleep(86400)  # Sleep for 24 hours
    ```

## Use Case

Ideal for traders and analysts who:

- Need up-to-date candles for backtesting.
- Do not want to manually import candles using the GUI dashboard.
- Need a resilient solution that can handle network failures.

## Dependencies

- **Jesse**: This is the only required dependency for running this script. [Jesse Documentation](https://docs.jesse.trade)

  *The script uses Jesse's research module. You can find more details [here](https://docs.jesse.trade/docs/research/).*

## How to Run

1. **Include in Jesse Project**: Make sure to include this file within your existing Jesse project.
2. **.env File**: A valid `.env` file should be present within your project folder, containing database information and other necessary configurations.
3. [Install Jesse](https://docs.jesse.trade/docs/getting-started/) if you haven't already.
4. Run the script.

```bash
python your_script_name.py
```

## Customization

Feel free to modify this script as you see fit for your specific use-case. 