class ReviewAgent:
    def review_schedule(self, schedule):
        """
        Review a given schedule and add a reviewed task at the end.

        Args:
        - schedule (list of dicts): List containing dictionaries representing tasks in the schedule.
                                    Each dictionary should have keys 'task', 'start_time', and 'end_time'.

        Returns:
        - reviewed_schedule (list of dicts): Updated schedule with a 'Reviewed' task added at the end.
        """
        reviewed_schedule = []
        for task in schedule:
            # Example review logic: Adjusting times and adding notes
            reviewed_task = {
                'task': task['task'],
                'start_time': self.adjust_time(task['start_time']),
                'end_time': self.adjust_time(task['end_time']),
                'notes': self.add_notes(task['task'])
            }
            reviewed_schedule.append(reviewed_task)
        
        # Add a reviewed task at the end
        reviewed_schedule.append({"task": "Reviewed", "start_time": "", "end_time": "", "notes": ""})
        
        return reviewed_schedule
    
    def adjust_time(self, time):
        # Assuming time format is 'HH:MM'
        if time:
            hours, minutes = time.split(':')
            new_minutes = int(minutes) + 30
            new_hours = int(hours) + new_minutes // 60
            new_minutes = new_minutes % 60
            adjusted_time = f"{new_hours:02}:{new_minutes:02}"
            return adjusted_time
        else:
            return ""
    
    def add_notes(self, task):
        if task == 'Exercise':
            return "Remember to stretch properly."
        elif task == 'Work on project':
            return "Focus on completing the design phase."
        elif task == 'Meet with friends':
            return "Discuss upcoming plans."
        elif task == 'Read a book':
            return "Finish chapter 3."
        else:
            return ""
