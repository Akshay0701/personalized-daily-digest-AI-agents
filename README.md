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
(venv) akshayjadhav@Akshays-Air personalized-daily-digest % python main.py
User Preferences: {'tasks': [{'task': 'Exercise', 'priority': 1, 'duration': 60}, {'task': 'Work on AI project', 'priority': 2, 'duration': 180}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120}, {'task': 'Reading a book', 'priority': 4, 'duration': 30}], 'day_start_time': '08:00', 'day_end_time': '20:00'}
Prioritized Tasks: [{'task': 'Exercise', 'priority': 1, 'duration': 60}, {'task': 'Work on AI project', 'priority': 2, 'duration': 180}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120}, {'task': 'Reading a book', 'priority': 4, 'duration': 30}]
Validating task: Exercise
Task validated: Exercise
Validating task: Work on AI project
Task validated: Work on AI project
Validating task: Meet with friends
Task validated: Meet with friends
Validating task: Reading a book
Task validated: Reading a book
Validated Tasks: [{'task': 'Exercise', 'priority': 1, 'duration': 60, 'response': 'Exercise for muscle building and strength.'}, {'task': 'Work on AI project', 'priority': 2, 'duration': 180, 'response': 'Researchers work on self-organizing neural networks for enhanced adaptability in AI projects.'}, {'task': 'Meet with friends', 'priority': 3, 'duration': 120, 'response': 'Connecting with friends boosts workplace happiness and combats loneliness, fostering better relationships and engagement.'}, {'task': 'Reading a book', 'priority': 4, 'duration': 30, 'response': 'AI can generate personalized short stories or chapters for reading while relaxing in bed.'}]
Schedule:
Final Schedule:
+----------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------+
| Task                | Start Time| End Time| Suggestion by AI                                                                                                           |
+----------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------+
| Exercise            | 08:00  | 09:00  | Exercise for muscle building and strength.                                                                                 |
| Work on AI project  | 09:00  | 12:00  | Researchers work on self-organizing neural networks for enhanced adaptability in AI projects.                              |
| Meet with friends   | 12:00  | 14:00  | Connecting with friends boosts workplace happiness and combats loneliness, fostering better relationships and engagement.  |
| Reading a book      | 14:00  | 14:30  | AI can generate personalized short stories or chapters for reading while relaxing in bed.                                  |
+----------------------+---------+---------+-----------------------------------------------------------------------------------------------------------------------------+
Final Schedule:
Final Schedule:
+----------------------+---------+---------+----+
| Task                | Start Time| End Time| Suggestion by AI|
+----------------------+---------+---------+----+
| Exercise            | 08:30  | 09:30  |   |
| Work on AI project  | 09:30  | 12:30  |   |
| Meet with friends   | 12:30  | 14:30  |   |
| Reading a book      | 14:30  | 15:00  |   |
| Reviewed            |        |        |   |
+----------------------+---------+---------+----+
```

## Conclusion

This project successfully creates a daily schedule based on user input tasks, ensuring task feasibility and prioritization. The use of AI agents and the Tavily API enhances the schedule creation process by validating tasks and providing relevant information.
