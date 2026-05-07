import { useQuery } from "@tanstack/react-query";

import { getTasks } from "./taskApi";

import { TaskCard } from "./TaskCard";

export const TaskList = () => {
  const { data, isLoading } = useQuery({
    queryKey: ["tasks"],
    queryFn: getTasks,
    refetchInterval: 3000,
  });

  if (isLoading) {
    return <div>Loading tasks...</div>;
  }

  if (!data?.length) {
    return (
      <div className="bg-slate-900 rounded-2xl p-8 text-center text-slate-400 border border-slate-800">
        No tasks yet
      </div>
    );
  }

  return (
    <div className="grid gap-4">
      {data?.map((task: Task) => (
        <TaskCard key={task.id} task={task} />
      ))}
    </div>
  );
};
