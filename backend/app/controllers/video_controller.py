from pathlib import Path

from fastapi import UploadFile


ROOT = Path(__file__).resolve().parents[2]

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