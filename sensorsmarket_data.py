import ccxt
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketDataFetcher:
    def __init__(self):
        exchange_name = os.getenv('EXCHANGE', 'binance')
        symbol = os.getenv('SYMBOL', 'MATIC/USDT')
        self.exchange = getattr(ccxt, exchange_name)()
        self.symbol = symbol

    def fetch_ohlcv(self, timeframe='1m', limit=100):
        """Fetch OHLCV data from the exchange."""
        try:
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe, limit=limit)
            return ohlcv
        except Exception as e:
            logger.error(f"Error fetching OHLCV: {e}")
            return []

    def fetch_ticker(self):
        """Fetch ticker data for the symbol."""
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            return ticker
        except Exception as e:
            logger.error(f"Error fetching ticker: {e}")
            return None

    def fetch_order_book(self, limit=10):
        """Fetch order book for the symbol."""
        try:
            order_book = self.exchange.fetch_order_book(self.symbol, limit=limit)
            return order_book
        except Exception as e:
            logger.error(f"Error fetching order book: {e}")
            return None