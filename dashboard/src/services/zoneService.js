import axios from "axios";

const API =
  "http://localhost:8000";

export const createZone = (
  payload
) => {

  return axios.post(
    `${API}/zones/`,
    payload
  );
};

export const getCameraZones = (
  cameraId
) => {

  return axios.get(
    `${API}/zones/${cameraId}`
  );
};

export const getAllZones =
  () => {

    return axios.get(
      `${API}/zones`
    );
  };


  export const deleteZone = (
  zoneId
) => {

  return axios.delete(
    `${API}/zones/${zoneId}`
  );
};

export const updateZone = (
  zoneId,
  payload
) => {

  return axios.put(
    `${API}/zones/${zoneId}`,
    payload
  );
};
  