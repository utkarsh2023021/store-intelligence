from datetime import datetime

class SessionManager:

    def __init__(self):
        self.active = {}

    def should_emit(self, visitor_id, event_type):

        key = f"{visitor_id}_{event_type}"

        if key in self.active:
            return False

        self.active[key] = datetime.utcnow()

        return True