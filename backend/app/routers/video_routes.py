from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.controllers.video_controller import (
    upload_video
)

router = APIRouter(
    prefix="/videos",
    tags=["videos"]
)


@router.post(
    "/upload/{camera_id}"
)
async def upload_video_route(
    camera_id: str,
    file: UploadFile = File(...)
):

    return await upload_video(
        camera_id,
        file
    )