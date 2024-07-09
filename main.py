from agents.user_input_agent import UserInputAgent
from agents.priority_agent import PriorityAgent
from agents.task_agent import TaskAgent
from agents.schedule_agent import ScheduleAgent
from agents.review_agent import ReviewAgent
from texttable import Texttable

def print_schedule(schedule):
    table = Texttable()
    table.add_row(["Task", "Start Time", "End Time"])
    for task in schedule:
        table.add_row([task["task"], task["start_time"], task["end_time"]])
    print(table.draw())

def main():
    # Initialize agents
    user_input_agent = UserInputAgent()
    priority_agent = PriorityAgent()
    task_agent = TaskAgent(api_key="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")
    schedule_agent = ScheduleAgent()
    review_agent = ReviewAgent()

    # Workflow
    preferences = user_input_agent.get_user_input()
    prioritized_tasks = priority_agent.prioritize_tasks(preferences["tasks"])
    print("Prioritized Tasks:", prioritized_tasks)
    
    validated_tasks = task_agent.validate_tasks(prioritized_tasks)
    print("Validated Tasks:", validated_tasks)
    
    schedule = schedule_agent.create_schedule(validated_tasks, preferences["day_start_time"], preferences["day_end_time"])
    print("Schedule:")
    print_schedule(schedule)
    
    final_schedule = review_agent.review_schedule(schedule)
    print("Final Schedule:")
    print_schedule(final_schedule)

if __name__ == "__main__":
    main()
