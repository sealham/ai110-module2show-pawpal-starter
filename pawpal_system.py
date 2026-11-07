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
        """Mark this task as complete."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a Task object to this pet's task list."""
        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task")
        self.tasks.append(task)


class Owner:
    def __init__(self, name, preferences):
        """Initialize an owner with a name, preferences, and pet list."""
        self.name = name
        self.preferences = preferences
        self.pets = []

    def add_pet(self, pet):
        """Add a Pet object to this owner's collection."""
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet")
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return a flattened list of all tasks for all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            if not isinstance(pet, Pet):
                continue
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    def generate_daily_plan(self, owner, available_time):
        """Generate a daily plan for the owner within the available time."""
        pass

    def sort_tasks(self, tasks):
        """Return a list of tasks sorted by their scheduled time."""
        if tasks is None:
            raise TypeError("tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("tasks must be a list of Task objects")

        for task in tasks:
            if not isinstance(task, Task):
                raise TypeError("all tasks must be Task instances")
            if not isinstance(task.time, str):
                raise TypeError("task time must be a string")

        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks(self, tasks, available_time):
        """Return tasks whose combined duration fits within the available time."""
        if tasks is None:
            raise TypeError("tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("tasks must be a list of Task objects")
        if not isinstance(available_time, (int, float)):
            raise TypeError("available_time must be a number")
        if available_time < 0:
            raise ValueError("available_time cannot be negative")

        valid_tasks = []
        total_duration = 0

        for task in tasks:
            if not isinstance(task, Task):
                raise TypeError("all tasks must be Task instances")
            if not isinstance(task.duration, (int, float)):
                raise TypeError("task duration must be a number")
            if task.duration < 0:
                raise ValueError("task duration cannot be negative")

            if total_duration + task.duration <= available_time:
                valid_tasks.append(task)
                total_duration += task.duration

        return valid_tasks

    def explain_plan(self, tasks):
        """Explain the scheduling decisions for the selected tasks."""
        pass