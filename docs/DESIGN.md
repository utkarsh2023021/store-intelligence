# Store Intelligence System Design

## Overview

The objective of this project is to transform raw CCTV footage into business intelligence metrics that help retail stores understand customer behavior and conversion performance.

The system consists of four major layers:

1. Detection Layer
2. Event Generation Layer
3. Analytics API Layer
4. Dashboard Layer

The architecture was intentionally designed to be modular so that each component can be independently improved without impacting the rest of the pipeline.

---

## Detection Layer

The detection layer processes CCTV footage from multiple camera angles.

The implementation uses:

* YOLOv8 for person detection
* YOLO tracking IDs for visitor tracking
* Polygon-based zone assignment
* Entry line crossing detection

The system processes three camera types:

* Entry Camera
* Zone Camera
* Billing Camera

The Entry Camera is responsible for generating ENTRY and EXIT events.

Zone Cameras generate:

* ZONE_ENTER
* ZONE_EXIT
* Dwell analytics

Billing Cameras are used to estimate billing activity and conversion behavior.

---

## Event Generation Layer

Each detected action is converted into a structured event.

Examples include:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_EXIT

Each event contains:

* event_id
* visitor_id
* timestamp
* store_id
* camera_id
* zone_id

The event-driven design makes it possible to replay footage and regenerate analytics without modifying business logic.

---

## Analytics Layer

The Analytics Layer is implemented using FastAPI.

Responsibilities:

* Event ingestion
* Metrics computation
* Funnel computation
* Heatmap analytics
* Anomaly detection
* Health monitoring

SQLite was chosen for simplicity and portability.

All analytics endpoints operate on stored events rather than directly on video data.

This separation improves maintainability and scalability.

---

## Dashboard Layer

A React dashboard provides:

* Zone calibration
* Analytics execution
* Real-time processing status
* Metrics visualization

The calibration interface allows business users to define store zones without modifying code.

---

## AI-Assisted Decisions

AI tools were extensively used during development for brainstorming architecture, API design, event schema design, and implementation approaches.

However, several AI-generated approaches were intentionally rejected after practical testing.

### Example 1 — Automatic Zone Generation

AI suggested automatically dividing camera views into equal-width zones.

During testing this produced highly inaccurate zone assignments because CCTV cameras were positioned at different angles and product shelves were not aligned uniformly.

A manual calibration interface was implemented instead.

This allows a business user to draw exact polygon boundaries directly on camera screenshots.

### Example 2 — Automatic Camera Boundary Detection

AI suggested detecting shelves and product displays automatically using computer vision.

The approach was inconsistent across different lighting conditions and camera perspectives.

Manual calibration proved significantly more reliable.

### Example 3 — Zone Assignment

AI initially suggested rectangular bounding regions.

Polygon-based zones were chosen instead because retail layouts rarely fit rectangular shapes.

The polygon approach produced much more accurate results.

---

## Scalability Considerations

For a production deployment:

* SQLite can be replaced with PostgreSQL.
* Event storage can be moved to Kafka.
* Tracking can be upgraded to ByteTrack or DeepSORT.
* Re-identification models can be introduced for cross-camera identity resolution.

The current implementation prioritizes correctness, transparency, and ease of deployment.

---

## Conclusion

The final architecture focuses on practical retail analytics rather than maximizing model complexity.

The primary goal was to produce reliable business metrics from real CCTV footage while maintaining simplicity and explainability.
