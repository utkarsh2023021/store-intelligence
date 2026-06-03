from pathlib import Path
import re

from fastapi import (
    HTTPException,
    UploadFile
)


ROOT = Path(__file__).resolve().parents[3]

VIDEO_DIR = (
    ROOT /
    "data" /
    "videos"
)

VIDEO_DIR.mkdir(
    parents=True,
    exist_ok=True
)


async def upload_video(
    camera_id,
    file: UploadFile
):

    if not re.fullmatch(
        r"[A-Za-z0-9_-]+",
        camera_id
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid camera id"
        )

    filename = (
        f"{camera_id}.mp4"
    )

    filepath = (
        VIDEO_DIR /
        filename
    )

    content = (
        await file.read()
    )

    with open(
        filepath,
        "wb"
    ) as f:

        f.write(content)

    return {
        "message":
        "uploaded"
    }
