from agents.user_input_agent import UserInputAgent
from agents.priority_agent import PriorityAgent
from agents.task_agent import TaskAgent
from agents.schedule_agent import ScheduleAgent
from agents.review_agent import ReviewAgent
from texttable import Texttable

def print_schedule(schedule):
    if not schedule:
        print("Schedule is empty.")
        return
    
    # Determine maximum lengths for each column to ensure proper alignment
    max_task_length = max(len(task['task']) for task in schedule) + 2  # Add some padding
    max_start_time_length = max(len(task['start_time']) for task in schedule) + 2
    max_end_time_length = max(len(task['end_time']) for task in schedule) + 2
    max_response_length = max(len(task.get('response', '')) for task in schedule) + 2

    # Print header
    print("Final Schedule:")
    print(f"+{'-'*(max_task_length+2)}+{'-'*(max_start_time_length+2)}+{'-'*(max_end_time_length+2)}+{'-'*(max_response_length+2)}+")
    print(f"| {'Task':<{max_task_length}}| {'Start Time':<{max_start_time_length}}| {'End Time':<{max_end_time_length}}| {'Suggestion by AI':<{max_response_length}}|")
    print(f"+{'-'*(max_task_length+2)}+{'-'*(max_start_time_length+2)}+{'-'*(max_end_time_length+2)}+{'-'*(max_response_length+2)}+")

    # Print each task row
    for task in schedule:
        task_name = task['task']
        start_time = task['start_time']
        end_time = task['end_time']
        response = task.get('response', '')

        print(f"| {task_name:<{max_task_length}}| {start_time:<{max_start_time_length}}| {end_time:<{max_end_time_length}}| {response:<{max_response_length}}|")
    
    # Print footer
    print(f"+{'-'*(max_task_length+2)}+{'-'*(max_start_time_length+2)}+{'-'*(max_end_time_length+2)}+{'-'*(max_response_length+2)}+")


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
