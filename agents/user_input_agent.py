class UserInputAgent:
    def __init__(self):
        self.user_preferences = {}

    def get_user_input(self):
        # Placeholder for user input logic
        self.user_preferences = {
            "tasks": [
                {"task": "Exercise", "priority": 1, "duration": 60},
                {"task": "Work on project", "priority": 2, "duration": 180},
                {"task": "Meet with friends", "priority": 3, "duration": 120},
                {"task": "Read a book", "priority": 4, "duration": 30},
            ],
            "day_start_time": "08:00",
            "day_end_time": "20:00"
        }
        print("User Preferences:", self.user_preferences)
        return self.user_preferences
