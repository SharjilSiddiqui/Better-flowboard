import { api } from "../../api/client";

export const getTasks = async () => {
  const response = await api.get("/tasks");
  return response.data;
};

export const createTask = async (data: {
  title: string;
  description?: string;
  priority: string;
}) => {
  const response = await api.post("/tasks", data);
  return response.data;
};

export const transitionTask = async (taskId: string, to_status: string) => {
  const response = await api.post(`/tasks/${taskId}/transition`, { to_status });

  return response.data;
};

export const deleteTask = async (taskId: string) => {
  const response = await api.delete(`/tasks/${taskId}`);

  return response.data;
};
