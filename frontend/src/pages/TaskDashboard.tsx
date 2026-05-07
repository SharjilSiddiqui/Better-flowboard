import { CreateTaskForm } from "../features/tasks/CreateTaskForm";
import { TaskList } from "../features/tasks/TaskList";

export const TaskDashboard = () => {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <div className="mb-8">
          <h1 className="text-4xl font-bold">FlowBoard</h1>

          <p className="text-slate-400 mt-2">
            Workflow-based task management system
          </p>
        </div>

        <div className="grid gap-6">
          <CreateTaskForm />
          <TaskList />
        </div>
      </div>
    </div>
  );
};
