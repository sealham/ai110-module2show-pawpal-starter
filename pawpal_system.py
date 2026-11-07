from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        pass


class Owner:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.pets = []

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def generate_daily_plan(self, owner, available_time):
        pass

    def sort_tasks(self, tasks):
        pass

    def filter_tasks(self, tasks, available_time):
        pass

    def explain_plan(self, tasks):
        pass