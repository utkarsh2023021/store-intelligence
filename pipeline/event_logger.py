class EventLogger:

    def __init__(self):
        self.counts = {}

    def log(self, event_type):

        if event_type not in self.counts:
            self.counts[event_type] = 0

        self.counts[event_type] += 1

    def summary(self):

        return self.counts