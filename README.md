# StoreIQ - AI Powered Retail Intelligence Platform

## Overview

StoreIQ transforms raw CCTV footage into actionable retail analytics.

The platform processes multi-camera store footage and generates visitor-level events, zone analytics, dwell metrics, and business intelligence dashboards.

The system combines computer vision, event-driven architecture, and a user-friendly calibration workflow to provide insights into customer behavior inside retail stores.

---

## Features

### Visitor Detection and Tracking

* YOLOv8 based person detection
* Multi-frame tracking
* Entry and exit detection
* Visitor event generation

### Zone Analytics

* Polygon-based zone calibration
* Zone enter events
* Zone exit events
* Dwell time calculation

### Dashboard

* Store metrics
* Zone traffic analytics
* Visitor funnel analytics
* Processing status monitoring

### Calibration System

* Camera-specific calibration
* Polygon drawing interface
* Zone editing
* Zone deletion

### Analytics Pipeline

* Multi-camera processing
* Event generation
* Event storage
* Aggregated metrics

---

## Architecture

```text
CCTV Videos
      |
      v
YOLO Detection
      |
      v
Visitor Tracking
      |
      v
Zone Assignment
      |
      v
Event Generation
      |
      v
Analytics API
      |
      v
React Dashboard
```

---

## Tech Stack

### Backend

* FastAPI
* SQLite
* OpenCV
* YOLOv8
* NumPy

### Frontend

* React
* Axios
* React Router

### Analytics

* Event-driven architecture
* Polygon zone calibration
* Dwell analytics

---

## Installation

### Clone Repository

```bash
git clone <repo-url>
cd store-intelligence
```

### Run With Docker

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:8000/docs
```

---

## Workflow

1. Upload CCTV videos
2. Calibrate camera zones
3. Run analytics
4. View dashboard metrics

---

## Testing

Run tests:

```bash
pytest
```

Expected output:

```text
3 passed
```

---

## Future Improvements

* Cross-camera re-identification
* Real-time streaming analytics
* PostgreSQL support
* Kafka event streaming
* Automatic heatmap generation

---

## Output
Detection pipeline outputs:
- pipeline/zone_events.json       Or
- data/output/events.jsonl        Or
- Frontend Dashboard

## Author

Built as part of the Purplle Store Intelligence Challenge.


