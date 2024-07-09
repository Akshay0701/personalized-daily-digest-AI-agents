# Personalized Daily Schedule

## Overview
This project creates a personalized daily schedule including tasks based on user input priorities and tasks.

## Installation
```bash
git clone https://github.com/yourusername/personalized-daily-schedule.git
cd personalized-daily-schedule
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

Certainly! Here's how you can structure your `README.md` file to include all the necessary information about your project, including an overview, steps taken, output examples, and a conclusion:

markdown
# Personalized Daily Digest

This project generates a daily schedule based on user input tasks, prioritizes them, validates their feasibility, and creates a finalized schedule using AI agents and the Tavily API.

## Steps Taken

1. **User Input**: Gathered user preferences including tasks, priorities, and daily schedule timings.
2. **Task Prioritization**: Used a Priority Agent to prioritize tasks based on user-defined priorities.
3. **Task Validation**: Validated each task using a Task Agent integrated with the Tavily API for task feasibility.
4. **Schedule Creation**: Created a daily schedule using a Schedule Agent considering start and end times provided by the user.
5. **Schedule Review**: Reviewed and finalized the schedule using a Review Agent.

## Output

```
User Preferences: {'tasks': [{'task': 'Exercise', 'priority': 1, 'duration': 60}, {'task': 'Work on project', 'priority': 2, 'duration': 180}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120}, {'task': 'Read a book', 'priority': 4, 'duration': 30}], 'day_start_time': '08:00', 'day_end_time': '20:00'}

Prioritized Tasks: [{'task': 'Exercise', 'priority': 1, 'duration': 60}, {'task': 'Work on project', 'priority': 2, 'duration': 180}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120}, {'task': 'Read a book', 'priority': 4, 'duration': 30}]

Validating task: Exercise
Task validated: Exercise
Validating task: Work on project
Task validated: Work on project
Validating task: Meet with friends
Task validated: Meet with friends
Validating task: Read a book
Task validated: Read a book

Validated Tasks: [{'task': 'Exercise', 'priority': 1, 'duration': 60}, {'task': 'Work on project', 'priority': 2, 'duration': 180}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120}, {'task': 'Read a book', 'priority': 4, 'duration': 30}]

Schedule:
+-------------------+------------+----------+
| Task              | Start Time | End Time |
+-------------------+------------+----------+
| Exercise          | 08:00      | 09:00    |
+-------------------+------------+----------+
| Work on project   | 09:00      | 12:00    |
+-------------------+------------+----------+
| Meet with friends | 12:00      | 14:00    |
+-------------------+------------+----------+
| Read a book       | 14:00      | 14:30    |
+-------------------+------------+----------+

Final Schedule:
+-------------------+------------+----------+
| Task              | Start Time | End Time |
+-------------------+------------+----------+
| Exercise          | 08:00      | 09:00    |
+-------------------+------------+----------+
| Work on project   | 09:00      | 12:00    |
+-------------------+------------+----------+
| Meet with friends | 12:00      | 14:00    |
+-------------------+------------+----------+
| Read a book       | 14:00      | 14:30    |
+-------------------+------------+----------+
| Reviewed          |            |          |
+-------------------+------------+----------+
```

## Conclusion

This project successfully creates a daily schedule based on user input tasks, ensuring task feasibility and prioritization. The use of AI agents and the Tavily API enhances the schedule creation process by validating tasks and providing relevant information.
