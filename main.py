from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Alex", {"preferred_time": "morning"})
pet1 = Pet("Bella", "Dog")
pet2 = Pet("Milo", "Cat")
owner.add_pet(pet1)
owner.add_pet(pet2)

# Deliberately unsorted tasks
walk = Task(
    title="Morning walk",
    description="Walk Bella around the neighborhood",
    time="08:00",
    duration=30,
    priority="High",
    frequency="Daily",
)
feed = Task(
    title="Feed cat",
    description="Serve breakfast to Milo",
    time="07:30",
    duration=10,
    priority="High",
    frequency="Daily",
)
brush = Task(
    title="Brush fur",
    description="Brush Bella's coat",
    time="18:00",
    duration=20,
    priority="Medium",
    frequency="Daily",
)
play = Task(
    title="Play fetch",
    description="Play with Bella in the yard",
    time="09:00",
    duration=25,
    priority="Medium",
    frequency="Weekly",
)
vet = Task(
    title="Vet appointment",
    description="Annual wellness check",
    time="09:00",
    duration=40,
    priority="High",
    frequency="Weekly",
)

dog_tasks = [walk, brush, play]
cat_tasks = [feed]

for task in dog_tasks:
    pet1.add_task(task)
for task in cat_tasks:
    pet2.add_task(task)

pet1.add_task(vet)

scheduler = Scheduler()
all_tasks = owner.get_all_tasks()

print("Sorted tasks by time:")
for task in scheduler.sort_tasks(all_tasks):
    print(f"{task.time} - {task.title} ({task.pet.name})")

print("\nIncomplete tasks:")
for task in scheduler.filter_by_status(all_tasks, False):
    print(f"{task.time} - {task.title} ({task.pet.name})")

print("\nBella's tasks:")
for task in scheduler.filter_by_pet(owner, "Bella"):
    print(f"{task.time} - {task.title}")

conflict_warning = scheduler.detect_conflicts(all_tasks)
print("\nConflict check:")
if conflict_warning:
    print(conflict_warning)
else:
    print("No scheduling conflicts detected.")

completed_daily = pet1.tasks[0]
print("\nMarking a daily task complete:")
next_task = completed_daily.mark_complete()
print(f"Original completed: {completed_daily.completed}")
print(f"Next occurrence added: {next_task.title} at {next_task.time} for {next_task.pet.name}")
print(f"Pet task count: {len(pet1.tasks)}")
