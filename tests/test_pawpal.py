import pytest

from pawpal_system import Owner, Pet, Scheduler, Task


@pytest.fixture
def sample_task():
    return Task(
        title="Morning walk",
        description="Walk the dog",
        time="08:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )


def test_task_mark_complete_updates_completion_status(sample_task):
    assert sample_task.completed is False

    sample_task.mark_complete()

    assert sample_task.completed is True


def test_pet_add_task_adds_task_to_list(sample_task):
    pet = Pet(name="Bella", species="Dog")

    pet.add_task(sample_task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is sample_task


def test_owner_add_pet_adds_pet_to_owner(sample_task):
    owner = Owner(name="Alex", preferences={"preferred_time": "morning"})
    pet = Pet(name="Bella", species="Dog")

    owner.add_pet(pet)

    assert len(owner.pets) == 1
    assert owner.pets[0] is pet


def test_owner_get_all_tasks_returns_combined_list():
    owner = Owner(name="Alex", preferences={"preferred_time": "morning"})
    dog = Pet(name="Bella", species="Dog")
    cat = Pet(name="Milo", species="Cat")

    walk = Task(
        title="Morning walk",
        description="Walk Bella",
        time="08:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )
    feed = Task(
        title="Feed cat",
        description="Serve breakfast",
        time="07:30",
        duration=10,
        priority="High",
        frequency="Daily",
    )

    dog.add_task(walk)
    cat.add_task(feed)
    owner.add_pet(dog)
    owner.add_pet(cat)

    tasks = owner.get_all_tasks()

    assert tasks == [walk, feed]


def test_daily_task_mark_complete_creates_and_adds_next_occurrence():
    pet = Pet(name="Bella", species="Dog")
    task = Task(
        title="Morning walk",
        description="Walk Bella",
        time="08:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )
    pet.add_task(task)

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task in pet.tasks
    assert len([item for item in pet.tasks if item.title == task.title and item.completed is False]) == 1


def test_weekly_task_mark_complete_creates_and_adds_next_occurrence():
    pet = Pet(name="Bella", species="Dog")
    task = Task(
        title="Vet visit",
        description="Check-up",
        time="10:00",
        duration=45,
        priority="Medium",
        frequency="Weekly",
    )
    pet.add_task(task)

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task in pet.tasks
    assert next_task.frequency == "Weekly"


def test_one_time_task_mark_complete_does_not_create_next_occurrence():
    pet = Pet(name="Bella", species="Dog")
    task = Task(
        title="Grooming",
        description="Brush coat",
        time="15:00",
        duration=20,
        priority="Low",
        frequency="Once",
    )
    pet.add_task(task)

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is None
    assert len(pet.tasks) == 1


def test_original_task_stays_completed_after_recurring_task_creation():
    pet = Pet(name="Milo", species="Cat")
    task = Task(
        title="Feed cat",
        description="Serve breakfast",
        time="07:30",
        duration=10,
        priority="High",
        frequency="Daily",
    )
    pet.add_task(task)

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task is not task
    assert any(existing is task and existing.completed is True for existing in pet.tasks)


def test_detect_conflicts_same_pet_returns_warning():
    pet = Pet(name="Bella", species="Dog")
    task_a = Task(
        title="Morning walk",
        description="Walk Bella",
        time="08:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )
    task_b = Task(
        title="Brush fur",
        description="Brush Bella",
        time="08:00",
        duration=20,
        priority="Medium",
        frequency="Daily",
    )
    pet.add_task(task_a)
    pet.add_task(task_b)

    warning = Scheduler().detect_conflicts(pet.tasks)

    assert warning is not None
    assert "Bella" in warning
    assert "08:00" in warning


def test_detect_conflicts_different_pets_returns_warning():
    bella = Pet(name="Bella", species="Dog")
    milo = Pet(name="Milo", species="Cat")
    task_a = Task(
        title="Morning walk",
        description="Walk Bella",
        time="09:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )
    task_b = Task(
        title="Feed cat",
        description="Feed Milo",
        time="09:00",
        duration=10,
        priority="High",
        frequency="Daily",
    )
    bella.add_task(task_a)
    milo.add_task(task_b)

    warning = Scheduler().detect_conflicts([task_a, task_b])

    assert warning is not None
    assert "Bella" in warning and "Milo" in warning
    assert "09:00" in warning


def test_detect_conflicts_no_conflict_returns_none():
    pet = Pet(name="Bella", species="Dog")
    task_a = Task(
        title="Morning walk",
        description="Walk Bella",
        time="08:00",
        duration=30,
        priority="High",
        frequency="Daily",
    )
    task_b = Task(
        title="Feed dinner",
        description="Dinner for Bella",
        time="09:00",
        duration=15,
        priority="Medium",
        frequency="Daily",
    )
    pet.add_task(task_a)
    pet.add_task(task_b)

    warning = Scheduler().detect_conflicts(pet.tasks)

    assert warning is None
