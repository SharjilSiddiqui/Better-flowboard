import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import { createTask } from "./taskApi";
import { createTaskSchema } from "../../schemas/taskSchema";

//
type FormData = {
  title: string;
  description: string;
  priority: string;
};

export const CreateTaskForm = () => {
  const queryClient = useQueryClient();

  const { register, handleSubmit, reset } = useForm<FormData>();

  const mutation = useMutation({
    mutationFn: createTask,

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["tasks"],
      });

      reset();
    },
  });

  const onSubmit = (data: FormData) => {
    const validatedData = createTaskSchema.parse(data);

    mutation.mutate(validatedData);
  };

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
      <h2 className="text-xl font-semibold mb-4">
        {mutation.isPending ? "Creating..." : "Create Task"}
      </h2>

      <form onSubmit={handleSubmit(onSubmit)} className="grid gap-4">
        <input
          {...register("title")}
          placeholder="Task title"
          className="bg-slate-800 border border-slate-700 rounded-lg px-4 py-3"
        />

        <textarea
          {...register("description")}
          placeholder="Task description"
          className="bg-slate-800 border border-slate-700 rounded-lg px-4 py-3"
        />

        <select
          {...register("priority")}
          className="bg-slate-800 border border-slate-700 rounded-lg px-4 py-3"
        >
          <option value="LOW">LOW</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="HIGH">HIGH</option>
        </select>

        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-500 transition rounded-lg py-3 font-medium"
        >
          Create Task
        </button>
      </form>
      {mutation.isError && (
        <div className="text-red-400 text-sm">Failed to create task</div>
      )}
    </div>
  );
};
