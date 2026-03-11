from web3 import Web3
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BlockchainListener:
    def __init__(self):
        provider_uri = os.getenv('WEB3_PROVIDER_URI')
        if not provider_uri:
            raise Exception("WEB3_PROVIDER_URI environment variable not set")
        self.web3 = Web3(Web3.HTTPProvider(provider_uri))
        if not self.web3.isConnected():
            raise Exception("Failed to connect to blockchain")

    def get_latest_block(self):
        """Get the latest block number."""
        try:
            return self.web3.eth.block_number
        except Exception as e:
            logger.error(f"Error getting latest block: {e}")
            return None

    def get_balance(self, address):
        """Get the balance of an address."""
        try:
            balance = self.web3.eth.get_balance(address)
            return self.web3.fromWei(balance, 'ether')
        except Exception as e:
            logger.error(f"Error getting balance: {e}")
            return None

    def listen_for_events(self, contract_address, abi, event_name, callback):
        """Listen for events from a contract."""
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        event_filter = contract.events[event_name].createFilter(fromBlock='latest')
        while True:
            for event in event_filter.get_new_entries():
                callback(event)
            time.sleep(2)