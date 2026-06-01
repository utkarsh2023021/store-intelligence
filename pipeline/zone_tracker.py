class ZoneTracker:

    def __init__(self):

        self.current_zone = {}

        self.zone_frames = {}

    def update(
        self,
        visitor_id,
        zone
    ):

        old_zone = self.current_zone.get(
            visitor_id
        )

        if old_zone == zone:

            return None

        self.current_zone[
            visitor_id
        ] = zone

        return (
            old_zone,
            zone
        )