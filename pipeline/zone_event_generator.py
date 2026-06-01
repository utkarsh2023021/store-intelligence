from event_builder import build_event


def create_zone_enter(
    visitor_id,
    zone,
    camera_id
):

    return build_event(
        store_id="Brigade_Bangalore",
        visitor_id=visitor_id,
        event_type="ZONE_ENTER",
        camera_id=camera_id,
        zone_id=zone
    )


def create_zone_exit(
    visitor_id,
    zone,
    camera_id,
    dwell_seconds
):

    return build_event(
        store_id="Brigade_Bangalore",
        visitor_id=visitor_id,
        event_type="ZONE_EXIT",
        camera_id=camera_id,
        zone_id=zone,
        metadata={
            "dwell_seconds":
            dwell_seconds
        }
    )