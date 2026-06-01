import {
  useState
} from "react";

import {
  uploadVideo
} from "../services/videoService";

export default function VideoUpload() {

  const [files,setFiles] =
    useState({});

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

        [
          "CAM1",
          "CAM2",
          "CAM3",
          "CAM4",
          "CAM5"
        ].map(

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
        onClick={uploadAll}
      >

        Upload All

      </button>

    </div>
  );
}