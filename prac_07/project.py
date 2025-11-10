class Project:

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = completion_percentage


    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%"

    def __lt__(self,other):
        return self.priority < other.priority

    def is_completed(self):
        return self.percent_complete == 100

    def __repr__(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}"

