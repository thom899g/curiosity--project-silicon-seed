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