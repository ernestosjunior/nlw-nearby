import axios from "axios";

export const api = axios.create({
  baseURL: "https://3ca3-186-194-88-174.ngrok-free.app",
  timeout: 700,
});
