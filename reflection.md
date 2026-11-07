# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
My initial UML design consists of four main classes: Owner, Pet, Task, and Scheduler. The goal is to give each class a specific responsibility so the application can organize pet care information and generate daily schedules.

- **Owner:** Stores the owner's basic information and manages their pets.

- **Pet:** Stores information about each pet and keeps track of its care tasks.

- **Task:** Represents an individual pet care activity, including its description, time, frequency, duration, priority, and completion status.

- **Scheduler:** Retrieves tasks from the owner's pets and organizes them into a daily plan based on constraints such as time, priority, and preferences.

**b. Design changes**

The initial design was mostly preserved because the core responsibilities of Owner, Pet, Task, and Scheduler still matched the system's goals. However, I added a scheduled `time` attribute to the Task class so each task could be placed into a daily schedule in chronological order. This was necessary because the scheduler needs to know when a task should occur in addition to its description, priority, and duration, allowing it to organize activities more realistically and avoid conflicting or poorly sequenced care routines.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers several aspects of each task, including its scheduled time, duration, completion status, and pet ownership. However, these factors are used by different methods rather than one complete scheduling algorithm. For example, `sort_tasks()` organizes tasks chronologically, `filter_by_status()` separates completed and incomplete tasks, `filter_by_pet()` retrieves tasks for a specific pet, and `filter_tasks()` selects tasks that fit within an available time limit. Task priority and frequency are also stored, but they are not currently used to generate or optimize a complete daily schedule.

**b. Tradeoffs**

One tradeoff in our scheduler is that it detects conflicts only when tasks share the exact same start time, rather than when two tasks overlap in duration. This keeps the logic simple and easy to read, which is helpful in a prototype where the main goal is to flag obvious scheduling problems early. It also makes the warning messages clearer and easier to explain to the user. The limitation is that two tasks with different start times could still overlap in practice, so this approach does not catch every possible conflict, only the most direct ones.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools during this project for design brainstorming, implementation support, debugging, and documentation cleanup. The most effective AI coding assistant features were code generation, refactoring suggestions, and quick test-generation support, especially when I asked for edge cases involving recurring tasks, duplicate task creation, and conflict detection. The most helpful prompts were those that compared class responsibilities, suggested Python dataclass patterns, and reviewed whether the UML and implementation still matched. I also found it useful to keep separate chat sessions for different phases—design, implementation, testing, and documentation—so each discussion stayed focused and easier to review later.

**b. Judgment and verification**

One AI suggestion I did not accept as-is was to treat scheduling conflicts as hard errors instead of warnings. I decided to keep conflicts as warnings because this allows users to be notified of scheduling issues without preventing them from continuing to use the application. I verified this behavior by reviewing `detect_conflicts()` and the related tests in `tests/test_pawpal.py`, which confirm that the method returns a warning string when tasks share the same start time and `None` when no conflict exists. This helped me understand the importance of reviewing AI suggestions and making design decisions based on the project's actual requirements.
---

## 4. Testing and Verification

**a. What you tested**

I tested the core scheduling behaviors that matter most for this project: task completion, pet task assignment, owner task aggregation, time-based sorting, completion-status filtering, pet filtering, recurring daily and weekly behavior, one-time task behavior, and conflict detection. I also checked the no-conflict case to confirm that the scheduler returns `None` rather than a false warning. These tests were important because the scheduler is driven by time, pet ownership, and completion state, so a mistake in any one of those areas would affect the plan.

**b. Confidence**

I am confident in the current scheduler behavior for the scope of this project because the test suite covers the essential logic and the implementation stays aligned with the project requirements. If I had more time, I would test more edge cases, especially overlapping task durations that do not share the same start time, invalid time strings, and more complex recurring schedules across multiple pets. I would also want to validate a more complete `generate_daily_plan()` implementation once that method is expanded beyond the current stub.

---

## 5. Reflection

**a. What went well**

I am most satisfied with how the project stayed organized around clear responsibilities: Owner manages pets, Pet manages tasks, Task manages completion and recurrence, and Scheduler handles ordering and filtering. The recurring-task and conflict-detection logic also worked well once the class relationships were clarified, and the test suite gave quick feedback during implementation.

**b. What you would improve**

If I had another iteration, I would make the daily scheduling plan itself more complete by expanding `generate_daily_plan()` beyond its current stub and adding a clearer rule set for priority, duration, and task selection. I would also improve the conflict-detection logic to handle overlapping durations, not just identical start times, and I would continue refining the UI so the schedule is easier to read and explain.

**c. Key takeaway**

One important lesson from this project is that good system design depends on clear boundaries and verification. As the lead architect, I had to define the core responsibilities, review AI-generated suggestions critically, and verify that the final implementation still matched the design and tests. The classes were easier to maintain when each one had a specific responsibility, and AI was most valuable when I used it to explore ideas and test assumptions while still reviewing and validating the final output myself.
