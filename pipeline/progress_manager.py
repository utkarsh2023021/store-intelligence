import json
from pathlib import Path

PROGRESS_FILE = (
    Path(__file__).parent
    /
    "progress.json"
)


def update_progress(
    camera,
    progress,
    status
):

    with open(
        PROGRESS_FILE,
        "w"
    ) as f:

        json.dump(

            {
                "camera":
                    camera,

                "progress":
                    progress,

                "status":
                    status
            },

            f,

            indent=2
        )


def get_progress():

    if (
        not PROGRESS_FILE.exists()
        or PROGRESS_FILE.stat().st_size == 0
    ):

        return {

            "camera": None,

            "progress": 0,

            "status": "idle"
        }

    with open(
        PROGRESS_FILE
    ) as f:

        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {

                "camera": None,

                "progress": 0,

                "status": "idle"
            }
