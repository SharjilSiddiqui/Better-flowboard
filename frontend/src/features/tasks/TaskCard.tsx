import { useMutation, useQueryClient } from "@tanstack/react-query";

import { transitionTask, deleteTask } from "./taskApi";

type Task = {
  id: string;
  title: string;
  status: string;
  priority: string;
};

type Props = {
  task: Task;
};

export const TaskCard = ({ task }: Props) => {
  const queryClient = useQueryClient();

  const transitionMutation = useMutation({
    mutationFn: (newStatus: string) => transitionTask(task.id, newStatus),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["tasks"],
      });
    },
  });

  const deleteMutation = useMutation({
    mutationFn: () => deleteTask(task.id),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["tasks"],
      });
    },
  });

  const getNextStatuses = () => {
    switch (task.status) {
      case "TODO":
        return ["IN_PROGRESS", "CANCELLED"];

      case "IN_PROGRESS":
        return ["DONE", "CANCELLED"];

      default:
        return [];
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-semibold text-white">{task.title}</h2>

        <div className="flex gap-2">
          <span className="px-4 py-1 rounded-full bg-slate-800 text-white text-sm">
            {task.priority}
          </span>

          <span className="px-4 py-1 rounded-full bg-indigo-600 text-white text-sm">
            {task.status}
          </span>
        </div>
      </div>

      <div className="flex flex-wrap gap-3">
        {getNextStatuses().map((status) => (
          <button
            key={status}
            onClick={() => transitionMutation.mutate(status)}
            className="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white transition"
          >
            Move to {status}
          </button>
        ))}

        <button
          onClick={() => deleteMutation.mutate()}
          className="px-4 py-2 rounded-lg bg-red-600 hover:bg-red-700 text-white transition"
        >
          Delete Task
        </button>
      </div>
    </div>
  );
};
