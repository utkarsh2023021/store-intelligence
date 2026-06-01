# Engineering Choices and Trade-Offs

## Decision 1 — Detection Model

### Options Considered

1. YOLOv8
2. RT-DETR
3. MediaPipe
4. Custom OpenCV Pipeline

### AI Recommendation

AI suggested evaluating both YOLOv8 and RT-DETR.

### Final Choice

YOLOv8

### Reasoning

YOLOv8 provided:

* Fast inference
* Built-in tracking support
* Strong community support
* Easy integration

For this challenge, engineering speed and reliability were more important than marginal improvements in detection accuracy.

---

## Decision 2 — Zone Definition Strategy

### Options Considered

1. Automatic shelf detection
2. Equal-width camera partitions
3. Polygon-based manual calibration

### AI Recommendation

Initially, AI suggested automatically dividing camera views into fixed rectangular sections and later suggested using object detection to infer shelf boundaries.

### Problems Encountered

These approaches failed because:

* Cameras had different viewing angles.
* Product shelves were not aligned.
* Zone boundaries varied across stores.
* Small perspective shifts caused incorrect zone assignments.

### Final Choice

Polygon-based manual calibration.

### Reasoning

A dedicated calibration interface was created.

Business users can upload a camera screenshot and draw exact polygon boundaries.

Benefits:

* Works for every camera angle.
* No retraining required.
* Store-specific customization.
* Much higher accuracy.

This was the most significant design decision in the project.

---

## Decision 3 — Analytics Architecture

### Options Considered

1. Compute analytics directly from video
2. Compute analytics from events

### AI Recommendation

AI strongly suggested an event-driven architecture.

### Final Choice

Event-based architecture.

### Reasoning

Video processing is expensive.

Analytics queries should not require replaying CCTV footage.

The event-based design enables:

* Faster metrics computation
* Replayability
* Easier debugging
* Future streaming support

This architecture also aligns closely with production analytics systems.

---

## What AI Suggested But Was Rejected

Several AI-generated solutions were rejected after experimentation:

### Automatic Zone Detection

Rejected due to poor accuracy.

### Camera Auto-Calibration

Rejected due to varying camera perspectives.

### Fixed Rectangle Zones

Rejected because real retail layouts are irregular.

### Fully Automated Shelf Segmentation

Rejected because calibration became less accurate than a simple user-defined polygon workflow.

These experiences reinforced the importance of validating AI suggestions against real-world data instead of accepting them blindly.

---

## Final Reflection

AI accelerated implementation significantly, but the final system architecture was shaped by empirical testing on the provided CCTV footage.

The most successful decisions emerged when AI suggestions were combined with manual experimentation and business-context reasoning.
