import { useMutation, useQueryClient } from "@tanstack/react-query";

import { transitionTask } from "./taskApi";

import type { Task, TaskStatus } from "../../types/task";

const nextTransitions: Record<TaskStatus, TaskStatus[]> = {
  TODO: ["IN_PROGRESS", "CANCELLED"],

  IN_PROGRESS: ["IN_REVIEW", "CANCELLED"],

  IN_REVIEW: ["DONE", "IN_PROGRESS"],

  DONE: [],

  CANCELLED: [],
};

export const TaskCard = ({ task }: { task: Task }) => {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: ({ taskId, status }: { taskId: string; status: string }) =>
      transitionTask(taskId, status),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["tasks"],
      });
    },
  });

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
      <div className="flex items-start justify-between">
        <div>
          <h3 className="text-xl font-semibold">{task.title}</h3>

          <p className="text-slate-400 mt-2">{task.description}</p>
        </div>

        <div className="flex gap-2">
          <span className="bg-slate-800 px-3 py-1 rounded-full text-sm">
            {task.priority}
          </span>

          <span className="bg-blue-600 px-3 py-1 rounded-full text-sm">
            {task.status}
          </span>
        </div>
      </div>

      <div className="flex gap-2 mt-6 flex-wrap">
        {nextTransitions[task.status]?.map((status) => (
          <button
            key={status}
            onClick={() =>
              mutation.mutate({
                taskId: task.id,
                status,
              })
            }
            className="bg-slate-800 hover:bg-slate-700 transition px-4 py-2 rounded-lg text-sm"
          >
            Move to {status}
          </button>
        ))}
      </div>
    </div>
  );
};
