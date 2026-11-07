from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    title: str
    description: str
    time: str
    duration: int
    priority: str
    frequency: str
    completed: bool = False
    next_due_date: str | None = None

    def mark_complete(self):
        """Mark this task as complete and create the next recurring occurrence when needed."""
        self.completed = True

        frequency = str(self.frequency).strip().lower()
        if frequency in {"once", "one-time", "one time", "single", "non-recurring"}:
            return None

        if frequency not in {"daily", "weekly"}:
            return None

        delta_days = 1 if frequency == "daily" else 7
        next_date = date.today() + timedelta(days=delta_days)
        next_task = Task(
            title=self.title,
            description=self.description,
            time=self.time,
            duration=self.duration,
            priority=self.priority,
            frequency=self.frequency,
            completed=False,
            next_due_date=next_date.isoformat(),
        )

        pet = getattr(self, "pet", None)
        if pet is not None and isinstance(pet, Pet):
            next_task.pet = pet
            duplicate_exists = any(
                existing is not self
                and existing.title == next_task.title
                and existing.description == next_task.description
                and existing.time == next_task.time
                and existing.duration == next_task.duration
                and existing.priority == next_task.priority
                and existing.frequency == next_task.frequency
                and existing.completed is False
                for existing in pet.tasks
            )
            if not duplicate_exists:
                pet.tasks.append(next_task)

        return next_task


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task):
        """Add a Task object to this pet's task list."""
        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task")
        task.pet = self
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

    def _time_to_minutes(self, time_value):
        """Convert an HH:MM time string into total minutes since midnight for reliable sorting and comparisons."""
        if not isinstance(time_value, str):
            raise TypeError("time value must be a string in HH:MM format")

        try:
            hours, minutes = time_value.split(":" )
        except ValueError as exc:
            raise ValueError("time value must be in HH:MM format") from exc

        if not hours or not minutes:
            raise ValueError("time value must be in HH:MM format")

        hours = int(hours)
        minutes = int(minutes)

        if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
            raise ValueError("time value must be within a valid 24-hour clock")

        return hours * 60 + minutes

    def sort_tasks(self, tasks):
        """Return tasks ordered from earliest scheduled start time to latest using the HH:MM conversion helper."""
        if tasks is None:
            raise TypeError("tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("tasks must be a list of Task objects")

        for task in tasks:
            if not isinstance(task, Task):
                raise TypeError("all tasks must be Task instances")
            if not isinstance(task.time, str):
                raise TypeError("task time must be a string")

        return sorted(tasks, key=lambda task: self._time_to_minutes(task.time))

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

    def filter_by_status(self, tasks, completed):
        """Return only the tasks whose completed flag matches the supplied boolean value."""
        if tasks is None:
            raise TypeError("tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("tasks must be a list of Task objects")
        if not isinstance(completed, bool):
            raise TypeError("completed must be a boolean value")

        return [task for task in tasks if isinstance(task, Task) and task.completed is completed]

    def filter_by_pet(self, owner_or_pets, pet_name):
        """Return all tasks for the pet whose name matches pet_name, using an Owner or a list of Pet objects."""
        if not isinstance(pet_name, str):
            raise TypeError("pet_name must be a string")

        if isinstance(owner_or_pets, Owner):
            pets = owner_or_pets.pets
        elif isinstance(owner_or_pets, list):
            if not all(isinstance(pet, Pet) for pet in owner_or_pets):
                raise TypeError("owner_or_pets must contain only Pet objects")
            pets = owner_or_pets
        else:
            raise TypeError("owner_or_pets must be an Owner or a list of Pet objects")

        for pet in pets:
            if pet.name == pet_name:
                return list(pet.tasks)

        return []

    def detect_conflicts(self, tasks):
        """Check for tasks that share the same start time and return a warning message when a conflict is found."""
        if tasks is None:
            raise TypeError("tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("tasks must be a list of Task objects")

        grouped = {}
        for task in tasks:
            if not isinstance(task, Task):
                raise TypeError("all tasks must be Task instances")
            if not isinstance(task.time, str):
                raise TypeError("task time must be a string")

            time_minutes = self._time_to_minutes(task.time)
            pet_name = getattr(getattr(task, "pet", None), "name", "Unknown")
            grouped.setdefault(time_minutes, []).append({"task": task, "pet_name": pet_name})

        warnings = []
        for time_minutes, entries in sorted(grouped.items()):
            if len(entries) < 2:
                continue

            pet_names = sorted({entry["pet_name"] for entry in entries})
            task_names = [entry["task"].title for entry in entries]
            hour = time_minutes // 60
            minute = time_minutes % 60
            formatted_time = f"{hour:02d}:{minute:02d}"
            pet_text = ", ".join(pet_names)
            task_text = ", ".join(task_names)
            warnings.append(
                f"Scheduling conflict at {formatted_time}: {pet_text} have tasks scheduled at the same time ({task_text})."
            )

        if not warnings:
            return None

        return "Warning: " + " ".join(warnings)

    def explain_plan(self, tasks):
        """Explain the scheduling decisions for the selected tasks."""
        pass