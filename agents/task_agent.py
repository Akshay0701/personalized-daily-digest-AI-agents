from tavily import TavilyClient

class TaskAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.tavily_client = TavilyClient(api_key=self.api_key)

    def validate_tasks(self, tasks):
        validated_tasks = []
        for task in tasks:
            print(f"Validating task: {task['task']}")
            response = self.tavily_client.qna_search(query=f"Validate task: {task['task']}", search_depth="basic")
            if response:
                print(f"Task validated: {task['task']}")
                validated_tasks.append(task)
            else:
                print(f"Task validation failed: {task['task']}")
        return validated_tasks
