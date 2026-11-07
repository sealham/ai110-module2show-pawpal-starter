# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Sample Output

```text
Today's schedule:
07:30 - Feed cat (Serve breakfast to Milo)
08:00 - Morning walk (Walk Bella around the neighborhood)
18:00 - Brush fur (Brush Bella's coat)
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_tasks()` | Sorts tasks chronologically by converting each task's `time` value from `HH:MM` into minutes since midnight. This keeps the schedule in a reliable time order without depending on raw string sorting. |
| Filtering | `Scheduler.filter_by_status()`, `Scheduler.filter_by_pet()` | `filter_by_status()` returns only completed or incomplete tasks depending on the boolean passed in. `filter_by_pet()` returns the tasks for a specific pet by name, using the pet-to-task relationship already stored in the data model. Example: `filter_by_status(tasks, False)` shows only open tasks; `filter_by_pet(owner, "Bella")` returns Bella's tasks. |
| Conflict handling | `Scheduler.detect_conflicts()` | Checks all tasks for identical scheduled start times and returns a warning message rather than raising an exception. It includes the affected pet names and task titles in the message, so it catches conflicts within the same pet and across different pets. |
| Recurring tasks | `Task.mark_complete()` | When a task is marked complete and its `frequency` is `Daily` or `Weekly`, a new task is created for the next day or next week while keeping the original task completed. The next occurrence keeps the same title, description, time, duration, priority, and frequency, and is automatically added to the owning pet's `tasks` list if it does not already exist. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
