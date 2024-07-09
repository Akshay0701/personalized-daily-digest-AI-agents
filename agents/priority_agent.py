class PriorityAgent:
    def prioritize_tasks(self, tasks):
        # Sort tasks based on priority
        return sorted(tasks, key=lambda x: x["priority"])
