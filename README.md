# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## Original Project Objectives

The original assignment goals for this project were:

- Let a user enter basic owner + pet info
- Allow a user to add or edit tasks (duration + priority at minimum)
- Generate a fully constraint-based daily schedule/plan based on priorities and time availability
- Display the plan clearly and explain the reasoning when possible
- Include tests for the most important scheduling behaviors

These are the intended project goals, not a claim that all task-editing or full plan-generation behaviors are currently implemented in the final codebase.

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

## Features

### Streamlit UI

The Streamlit app in `app.py` lets a user:

- create an owner and assign a current pet
- enter a pet name and species
- add tasks with a title, duration, priority, and scheduled time
- view the current task list for the active pet
- generate a schedule view using the backend scheduler methods

### Backend scheduling logic

The backend in `pawpal_system.py` currently includes working scheduler behaviors for:

- chronological task sorting via `Scheduler.sort_tasks()`
- filtering incomplete or completed tasks via `Scheduler.filter_by_status()`
- filtering tasks by pet name via `Scheduler.filter_by_pet()`
- conflict detection via `Scheduler.detect_conflicts()`
- daily and weekly recurring tasks via `Task.mark_complete()`

The `generate_daily_plan()` method is still a stub and is not described as implemented.

## Sample Output

```text
Sorted tasks by time:
07:30 - Feed cat (Milo)
08:00 - Morning walk (Bella)
09:00 - Play fetch (Bella)
09:00 - Vet appointment (Bella)
18:00 - Brush fur (Bella)

Incomplete tasks:
08:00 - Morning walk (Bella)
18:00 - Brush fur (Bella)
09:00 - Play fetch (Bella)
09:00 - Vet appointment (Bella)
07:30 - Feed cat (Milo)

Bella's tasks:
08:00 - Morning walk
18:00 - Brush fur
09:00 - Play fetch
09:00 - Vet appointment

Conflict check:
Warning: Scheduling conflict at 09:00: Bella have tasks scheduled at the same time (Play fetch, Vet appointment).

Marking a daily task complete:
Original completed: True
Next occurrence added: Morning walk at 08:00 for Bella
Pet task count: 5
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
py -m pytest -q
```

Result:

```text
14 passed in 0.05s
```

The current suite verifies chronological task sorting, completion-status filtering, pet-based filtering, daily and weekly recurring task completion, one-time task behavior, same-pet and different-pet conflict detection, and the no-conflict case.

Confidence: ★★★★★ (5/5)

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_tasks()` | Orders tasks chronologically by converting `HH:MM` times to minutes since midnight. |
| Filtering | `Scheduler.filter_by_status()`, `Scheduler.filter_by_pet()` | Filters tasks by completion state or by pet name using the existing owner/pet/task relationships. |
| Conflict handling | `Scheduler.detect_conflicts()` | Detects tasks that share the same start time and returns a warning message with the affected pet names and task titles. |
| Recurring tasks | `Task.mark_complete()` | Creates the next `Daily` or `Weekly` task when a recurring task is completed and adds it to the owning pet's task list. |

## Demo Walkthrough

1. Open the Streamlit app and enter an owner name, such as "Alex".
2. Enter a pet name and species, such as "Bella" and "Dog", to create the active pet for the session.
3. Add tasks with a title, duration, priority, and scheduled time. For example, add a morning walk at `08:00`, a feeding task at `07:30`, and an evening grooming task at `18:00`.
4. Click the schedule button to view the current task list in chronological order. The app uses the backend scheduler to sort tasks by their `HH:MM` time.
5. Review the incomplete-task table to focus on tasks that still need to be completed, and review any warning message if two tasks share the same time.
6. Use the backend recurrence logic to mark a recurring task complete; daily or weekly tasks create the next occurrence automatically and attach it to the owning pet.

This walkthrough reflects the implemented Streamlit UI and backend scheduling behaviors, while keeping the unimplemented `generate_daily_plan()` method clearly out of scope.
