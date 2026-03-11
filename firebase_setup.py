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