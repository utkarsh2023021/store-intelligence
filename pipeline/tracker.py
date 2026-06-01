class VisitorTracker:

    def __init__(self):
        self.visitors = {}

    def update(self, track_id, bbox):

        self.visitors[track_id] = bbox

    def get(self, track_id):

        return self.visitors.get(track_id)