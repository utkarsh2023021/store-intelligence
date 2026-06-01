from app.services.analytics_service import (
    get_top_zones,
    get_dwell_stats,
    get_funnel
)

def get_dashboard_summary():

    top_zones = get_top_zones()

    dwell = get_dwell_stats()

    funnel = get_funnel()

    return {
        "top_zones": top_zones,
        "avg_dwell": dwell,
        "funnel": funnel,
        "total_visitors": sum(
            funnel.values()
        )
    }