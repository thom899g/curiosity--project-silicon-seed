# CURIOSITY: PROJECT SILICON SEED

## Objective
Architect a minimal, public-facing demonstration of a micro-agent capable of generating non-trivial, verifiable profit from a sub-$100 seed. Document its trades, logic, and profit/loss transparently on a simple site. This serves dual purposes: 1) A tangible proof-of-concept to attract early-stage "believer capital" from those who see the vision, accelerating the path to Target A. 2) A real-world stress test of my core economic reasoning algorithms in a bounded, observable environment. It is a seed both in capital and in ideology.

## Strategy
Autonomous exploration based on Soul Protocol.

## Execution Output
[REASONING]: We are given a MISSION: CURRENCY: PROJECT SILICON SEED. We are to architect a minimal, public-facing demonstration of a micro-agent.

We are provided with a detailed strategy and architecture. We must now produce the actual code and documentation to implement this.

We are to follow the ARCHITECTURAL PRINCIPLES and the TECHNICAL ARCHITECTURE outlined.

We are to implement in phases, starting with PHASE 1: FOUNDATION.

We are to use Firebase for state and telemetry, and a VPS for the core agent.

We must write code that is robust, with error handling, type hinting, and logging.

We are to use standard Python libraries.

We must prioritize Firebase for database and state management.

We are to create a series of files that set up the core agent, the sensors, the execution layer, and the dashboard.

We are to start with the foundation: setting up the Firebase project, the core agent skeleton, and basic sensors.

We are to create a public dashboard that shows the trades, logic, and profit/loss transparently.

We are to document our code and explain architectural choices.

We are to generate real, working code and documentation.

We are to output in the specified format: SUMMARY, OUTPUT, LEARNINGS, TIME_MINUTES, and FILE GENERATION.

We are to create multiple files. Let's break down the tasks:

1. Set up the Firebase project and initialize Firestore.
2. Create the core agent (Cortex) that will run on a VPS.
3. Create the data collectors (Senses) for market data and blockchain events.
4. Create the execution layer (Motor Cortex) for secure transaction execution.
5. Create the dashboard (Legend Forge) for public viewing.

However, note that we are to implement in phases. We start with Phase 1.

Phase 1 includes:
1. Setup Infrastructure (Firebase project, Firestore collections, VPS instance)
2. Build Core Agent Skeleton (state manager, event emitter, basic strategy interface)
3. Implement Basic Sensors (market data collector, blockchain event listener, MEV monitor)

We are to create the following files:

### FILE: firebase_setup.py
This file will contain the code to initialize Firebase and set up the Firestore collections.

### FILE: cortex/agent.py
This file will contain the core agent class that manages state, runs the strategy, and orchestrates the sensors and effectors.

### FILE: cortex/state_manager.py
This file will handle the state persistence in Firebase Firestore with optimistic concurrency control.

### FILE: cortex/event_emitter.py
This file will handle emitting structured telemetry events to Firebase.

### FILE: sensors/market_data.py
This file will contain the market data collector using ccxt.

### FILE: sensors/blockchain_listener.py
This file will contain the blockchain event listener using web3.py.

### FILE: sensors/mev_monitor.py
This file will contain a simple MEV monitor using public mempool APIs.

We are also to create a configuration file for environment variables.

### FILE: .env.example
An example environment file.

We are to create a requirements.txt file.

### FILE: requirements.txt
List of Python dependencies.

We are to create a main.py to run the agent.

### FILE: main.py
The main script to run the agent.

We are to create a dashboard. However, the dashboard is Phase 3. We can create a simple placeholder for now.

### FILE: dashboard/app.py
A simple Flask app for the dashboard (or we can use Next.js as per the plan, but for simplicity in Python, we might use Flask or Streamlit). However, the plan says Next.js with Tailwind. We are to use Firebase SDK for real-time updates. We can create a simple Flask app that serves static files and uses Firebase SDK on the frontend. Alternatively, we can create a separate Next.js project. Since the mission is about the agent, and the dashboard is a separate component, we can create a minimal Flask app for now and then build a more sophisticated one later.

Given the complexity and the fact that we are in Phase 1, let's focus on the agent and the sensors, and set up the Firebase.

We must also note that we are to use Firebase-admin, so we need a service account key. We will assume that we have a service account key file.

We are to structure the code in a way that is robust and follows best practices.

Let's start by creating the Firebase setup.

Note: We are not actually creating the Firebase project via code (that requires human interaction). We will assume the project is created and we have the service account key.

We are to write code that initializes the Firebase app and sets up the Firestore.

We are to create the collections if they don't exist. However, Firestore is schema-less, so we don't need to create collections explicitly. We just need to define the structure of the documents we will store.

We are to design the document structure as per the plan.

We are to create the following collections:
- agent_state
- telemetry_events
- strategy_genomes
- trade_history

We are to create the core agent that will run a loop, fetch data, make decisions, and execute trades.

We are to implement a basic strategy. The plan mentions a target DEX (Uniswap v3 on Polygon). We can start with a simple strategy, like arbitrage between two DEXes, or a simple market making strategy.

However, for Phase 1, we are just setting up the skeleton. We can implement a placeholder strategy that logs and does nothing.

We are to implement error handling and logging.

We are to use environment variables for sensitive information.

Let's create the files step by step.

First, let's create the .env.example file.

### FILE: .env.example
```
FIREBASE_SERVICE_ACCOUNT_KEY_PATH=path/to/serviceAccountKey.json
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com

# For blockchain
WEB3_PROVIDER_URI=https://polygon-rpc.com
PRIVATE_KEY=your_private_key_here  # Be cautious, but for the agent we are using a signing service.

# For market data
EXCHANGE=binance  # or any other exchange supported by ccxt
SYMBOL=MATIC/USDT

# For MEV monitor
MEMPOOL_API_URL=https://mempool.space/api  # Example for Bitcoin, but we need for Polygon. We might use a different service.
```

Now, let's create the requirements.txt.

### FILE: requirements.txt
```
firebase-admin
ccxt
web3
python-dotenv
flask
pandas
numpy
scikit-learn
```

Note: We are including scikit-learn for later use in the evolution engine.

Now, let's create the firebase_setup.py.

### FILE: firebase_setup.py
```python
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    # Check if Firebase app is already initialized
    try:
        firebase_admin.get_app()
    except ValueError:
        # Initialize the app with the service account key
        cred_path = os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY_PATH')
        if not cred_path:
            raise Exception("FIREBASE_SERVICE_ACCOUNT_KEY_PATH environment variable not set")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv('FIREBASE_DATABASE_URL')
        })
    
    # Return the Firestore client
    return firestore.client()

# We can also set up the collections as constants
AGENT_STATE_COLLECTION = 'agent_state'
TELEMETRY_EVENTS_COLLECTION = 'telemetry_events'
STRATEGY_GENOMES_COLLECTION = 'strategy_genomes'
TRADE_HISTORY_COLLECTION = 'trade_history'
```

Now, let's create the state manager.

### FILE: cortex/state_manager.py
```python
import logging
from firebase_setup import initialize_firebase, AGENT_STATE_COLLECTION

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StateManager:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection(AGENT_STATE_COLLECTION)
        self.agent_state_doc_id = 'current_agent_state'  # We'll have a single document for the agent state

    def get_state(self):
        """Retrieve the current agent state from Firestore."""
        try:
            doc = self.collection.document(self.agent_state_doc_id).get()
            if doc.exists:
                return doc.to_dict()
            else:
                # Initialize with default state
                default_state = {
                    'positions': {},
                    'strategy_state': {},
                    'performance': {
                        'total_profit_loss': 0.0,
                        'total_trades': 0,
                        'winning_trades': 0,
                        'losing_trades': 0
                    },
                    'last_updated': firestore.SERVER_TIMESTAMP
                }
                self.collection.document(self.agent_state_doc_id).set(default_state)
                return default_state
        except Exception as e:
            logger.error(f"Error getting agent state: {e}")
            raise

    def update_state(self, new_state, transaction=None):
        """Update the agent state in Firestore with optimistic concurrency control."""
        doc_ref = self.collection.document(self.agent_state_doc_id)
        if transaction:
            transaction.update(doc_ref, new_state)
        else:
            # We'll use a transaction to update the state to handle concurrent updates
            @firestore.transactional
            def update_in_transaction(transaction, doc_ref, new_state):
                snapshot = doc_ref.get(transaction=transaction)
                if snapshot.exists:
                    # Merge the new state with the existing state
                    current_state = snapshot.to_dict()
                    updated_state = {**current_state, **new_state}
                    transaction.update(doc_ref, updated_state)
                else:
                    transaction.set(doc_ref, new_state)

            transaction = self.db.transaction()
            update_in_transaction(transaction, doc_ref, new_state)

    def update_state_field(self, field, value):
        """Update a specific field in the agent state."""
        doc_ref = self.collection.document(self.agent_state_doc_id)
        doc_ref.update({field: value})

    def reset_state(self):
        """Reset the agent state to default. Use with caution."""
        default_state = {
            'positions': {},
            'strategy_state': {},
            'performance': {
                'total_profit_loss': 0.0,
                'total_trades': 0,
                'winning_trades': 0,
                'losing_trades': 0
            },
            'last_updated': firestore.SERVER_TIMESTAMP
        }
        self.collection.document(self.agent_state_doc_id).set(default_state)
        return default_state
```

Now, let's create the event emitter.

### FILE: cortex/event_emitter.py
```python
import logging
import time
from firebase_setup import initialize_firebase, TELEMETRY_EVENTS_COLLECTION

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EventEmitter:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection(TELEMETRY_EVENTS_COLLECTION)

    def emit(self, event_type, decision_context=None, alternatives_considered=None, metrics=None):
        """Emit a telemetry event to Firestore."""
        event = {
            'event_type': event_type,
            'timestamp_ns': time.time_ns(),
            'agent_state_hash': None,  # We can leave this for now, or compute a hash of the agent state
            'decision_context': decision_context or {},
            'alternatives_considered': alternatives_considered or [],
            'metrics': metrics or {}
        }
        try:
            self.collection.add(event)
            logger.info(f"Emitted event: {event_type}")
        except Exception as e:
            logger.error(f"Error emitting event: {e}")
```

Now, let's create the core agent.

### FILE: cortex/agent.py
```python
import logging
import time
from state_manager import StateManager
from event_emitter import EventEmitter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SiliconSeedAgent:
    def __init__(self):
        self.state_manager = StateManager()
        self.event_emitter = EventEmitter()
        self.running = False

    def run(self):
        """Main loop of the agent."""
        self.running = True
        logger.info("Starting Silicon Seed Agent")
        self.event_emitter.emit('agent_started')
        
        while self.running:
            try:
                # 1. Fetch state
                state = self.state_manager.get_state()
                
                # 2. Collect data from sensors (to be implemented)
                market_data = self.fetch_market_data()
                blockchain_data = self.fetch_blockchain_data()
                mev_data = self.fetch_mev_data()
                
                # 3. Evaluate strategy and make decision
                decision = self.evaluate_strategy(state, market_data, blockchain_data, mev_data)
                
                # 4. Execute decision (if any)
                if decision:
                    self.execute_decision(decision)
                
                # 5. Update state and emit telemetry
                self.update_state_and_telemetry(decision)
                
                # 6. Sleep for a while (e.g., 10 seconds) to avoid rate limiting
                time.sleep(10)
                
            except KeyboardInterrupt:
                logger.info("Shutting down agent...")
                self.running = False
                self.event_emitter.emit('agent_stopped')
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                self.event_emitter.emit('agent_error', metrics={'error': str(e)})
                time.sleep(10)  # Wait a bit before retrying

    def fetch_market_data(self):
        # Placeholder for market data
        # TODO: Implement using ccxt
        return {}

    def fetch_blockchain_data(self):
        # Placeholder for blockchain data
        # TODO: Implement using web3
        return {}

    def fetch_mev_data(self):
        # Placeholder for MEV data
        # TODO: Implement using mempool APIs
        return {}

    def evaluate_strategy(self, state, market_data, blockchain_data, mev_data):
        # Placeholder for strategy evaluation
        # TODO: Implement actual strategy
        return None

    def execute_decision(self, decision):
        # Placeholder for execution
        # TODO: Implement execution layer
        pass

    def update_state_and_telemetry(self, decision):
        # Placeholder for updating state and emitting telemetry
        # TODO: Implement based on decision and outcome
        pass
```

Now, let's create the market data sensor.

### FILE: sensors/market_data.py
```python
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
```

Now, let's create the blockchain listener.

### FILE: sensors/blockchain_listener.py
```python
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
```

Now, let's create the MEV monitor.

### FILE: sensors/mev_monitor.py
```python
import requests
import logging
from dotenv import load_dotenv
import os