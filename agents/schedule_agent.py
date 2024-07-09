from datetime import datetime, timedelta

class ScheduleAgent:
    def create_schedule(self, tasks, day_start_time, day_end_time):
        schedule = []
        current_time = datetime.strptime(day_start_time, "%H:%M")
        end_time = datetime.strptime(day_end_time, "%H:%M")

        for task in tasks:
            if current_time + timedelta(minutes=task["duration"]) <= end_time:
                schedule.append({
                    "task": task["task"],
                    "start_time": current_time.strftime("%H:%M"),
                    "end_time": (current_time + timedelta(minutes=task["duration"])).strftime("%H:%M")
                })
                current_time += timedelta(minutes=task["duration"])
            else:
                break

        return schedule
