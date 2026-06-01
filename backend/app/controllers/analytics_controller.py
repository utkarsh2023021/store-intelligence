from app.services.analytics_service import (
    get_top_zones,
    get_dwell_stats,
    get_funnel
)


def top_zones_controller():

    return get_top_zones()


def dwell_controller():

    return get_dwell_stats()


def funnel_controller():

    return get_funnel()