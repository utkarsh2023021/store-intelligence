import subprocess
import sys

from pathlib import Path

ROOT = (
    Path(__file__)
    .resolve()
    .parents[3]
)

PIPELINE_SCRIPT = (
    ROOT /
    "pipeline" /
    "run_all_cameras.py"
)

PIPELINE_DIR = ROOT / "pipeline"

sys.path.insert(
    0,
    str(PIPELINE_DIR)
)

from progress_manager import get_progress


def start_pipeline():

    subprocess.Popen(

        [
            sys.executable,
            str(
                PIPELINE_SCRIPT
            )
        ],
        cwd=str(PIPELINE_DIR)

    )

    return {

        "message":
        "processing started"
    }


def get_status():

    return get_progress()
