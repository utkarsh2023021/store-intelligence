import axios from "axios";

const API =
  "http://localhost:8000";

export const startPipeline =
  () =>
    axios.post(
      `${API}/pipeline/start`
    );

export const getStatus =
  () =>
    axios.get(
      `${API}/pipeline/status`
    );