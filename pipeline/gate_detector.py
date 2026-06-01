class GateDetector:

    def __init__(self, p1, p2):

        self.x1, self.y1 = p1
        self.x2, self.y2 = p2

        self.history = {}

    def side(self, x, y):

        return (
            (self.x2 - self.x1) * (y - self.y1)
            -
            (self.y2 - self.y1) * (x - self.x1)
        )

    def update(self, track_id, cx, cy):

        current_side = self.side(cx, cy)

        if track_id not in self.history:

            self.history[track_id] = current_side

            return None

        previous_side = self.history[track_id]

        self.history[track_id] = current_side

        if previous_side > 0 and current_side <= 0:
            return "ENTRY"

        if previous_side < 0 and current_side >= 0:
            return "EXIT"

        return None