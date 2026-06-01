class LineCrossingDetector:

    def __init__(self, line_y):
        self.line_y = line_y
        self.history = {}

    def update(self, track_id, center_y):

        if track_id not in self.history:
            self.history[track_id] = center_y
            return None

        prev_y = self.history[track_id]
        self.history[track_id] = center_y

        if prev_y > self.line_y and center_y <= self.line_y:
            return "ENTRY"

        if prev_y < self.line_y and center_y >= self.line_y:
            return "EXIT"

        return None