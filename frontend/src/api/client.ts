import axios from "axios";

export const api = axios.create({
  baseURL: "https://better-flowboard.onrender.com/api",
});
