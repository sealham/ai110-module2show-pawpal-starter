import pytest

from pawpal_system import Owner, Pet, Task


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
