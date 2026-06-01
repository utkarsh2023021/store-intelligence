class DwellDetector:

    def __init__(self, fps):

        self.fps = fps

        self.enter_frame = {}

    def enter(
        self,
        visitor_id,
        zone,
        frame_no
    ):

        self.enter_frame[
            (
                visitor_id,
                zone
            )
        ] = frame_no

    def exit(
        self,
        visitor_id,
        zone,
        frame_no
    ):

        key = (
            visitor_id,
            zone
        )

        if key not in self.enter_frame:
            return 0

        start_frame = self.enter_frame[key]

        del self.enter_frame[key]

        return round(
            (
                frame_no -
                start_frame
            )
            /
            self.fps
        )