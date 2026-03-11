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