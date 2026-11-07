from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Alex", {"preferred_time": "morning"})

pet1 = Pet("Bella", "Dog")
pet2 = Pet("Milo", "Cat")

owner.add_pet(pet1)
owner.add_pet(pet2)

task1 = Task(
    title="Morning walk",
    description="Walk Bella around the neighborhood",
    time="08:00",
    duration=30,
    priority="High",
    frequency="Daily",
)
task2 = Task(
    title="Feed cat",
    description="Serve breakfast to Milo",
    time="07:30",
    duration=10,
    priority="High",
    frequency="Daily",
)
task3 = Task(
    title="Brush fur",
    description="Brush Bella's coat",
    time="18:00",
    duration=20,
    priority="Medium",
    frequency="Daily",
)

pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)

scheduler = Scheduler()
all_tasks = owner.get_all_tasks()
ordered_tasks = scheduler.sort_tasks(all_tasks)

print("Today's schedule:")
for task in ordered_tasks:
    print(f"{task.time} - {task.title} ({task.description})")
