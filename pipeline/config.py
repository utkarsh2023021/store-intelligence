STORE_ID = "Brigade_Bangalore"

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

VIDEO_DIR = ROOT / "data" / "videos"

CAMERAS = {
    path.stem: str(path.relative_to(ROOT))
    for path in sorted(VIDEO_DIR.glob("*.mp4"))
}
