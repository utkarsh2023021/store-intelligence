import {
  useState
} from "react";

import {
  uploadVideo
} from "../services/videoService";

export default function VideoUpload() {

  const [cameras,setCameras] =
    useState([
      "CAM1",
      "CAM2",
      "CAM3",
      "CAM4",
      "CAM5"
    ]);

  const [files,setFiles] =
    useState({});

  const nextCameraId =
    () => {

      const usedNumbers =
        cameras
          .map(camera =>
            camera.match(/^CAM(\d+)$/)
          )
          .filter(Boolean)
          .map(match =>
            Number(match[1])
          );

      const nextNumber =
        usedNumbers.length > 0
          ? Math.max(...usedNumbers) + 1
          : cameras.length + 1;

      return `CAM${nextNumber}`;
    };

  const addCamera =
    () => {

      setCameras(prev => [

        ...prev,

        nextCameraId()
      ]);
    };

  const handleChange = (
    camera,
    file
  ) => {

    setFiles(prev => ({

      ...prev,

      [camera]: file
    }));
  };

  const uploadAll =
    async () => {

      for (
        const camera
        in files
      ) {

        if (!files[camera]) {
          continue;
        }

        await uploadVideo(

          camera,

          files[camera]
        );
      }

      alert(
        "Videos Uploaded"
      );
    };

  return (

    <div
      style={{
        padding:40
      }}
    >

      <h1>
        Upload CCTV Videos
      </h1>

      {

        cameras.map(

          camera => (

            <div
              key={camera}
              style={{
                marginBottom:20
              }}
            >

              <label>

                {camera}

              </label>

              <input

                type="file"

                accept=".mp4"

                onChange={
                  e =>
                    handleChange(
                      camera,
                      e.target.files[0]
                    )
                }
              />

            </div>
          )
        )
      }

      <button
        type="button"
        onClick={addCamera}
        aria-label="Add camera video"
        title="Add camera video"
        style={{
          marginRight:12,
          width:36,
          height:36,
          fontSize:24,
          lineHeight:"24px"
        }}
      >

        +

      </button>

      <button
        onClick={uploadAll}
      >

        Upload All

      </button>

    </div>
  );
}
