import axios from "axios";

const API = "http://localhost:8000";

export const getDashboard = () =>
  axios.get(
    `${API}/dashboard/summary`
  );

export const getTopZones = () =>
  axios.get(
    `${API}/analytics/top-zones`
  );

export const getDwell = () =>
  axios.get(
    `${API}/analytics/dwell`
  );

export const getFunnel = () =>
  axios.get(
    `${API}/analytics/funnel`
  );