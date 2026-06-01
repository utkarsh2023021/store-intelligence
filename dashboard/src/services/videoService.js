import axios from "axios";

const API =
  "http://localhost:8000";

export const uploadVideo =
  (
    cameraId,
    file
  ) => {

    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    return axios.post(

      `${API}/videos/upload/${cameraId}`,

      formData,

      {
        headers: {
          "Content-Type":
            "multipart/form-data"
        }
      }
    );
  };