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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

One tradeoff in our scheduler is that it detects conflicts only when tasks share the exact same start time, rather than when two tasks overlap in duration. This keeps the logic simple and easy to read, which is helpful in a prototype where the main goal is to flag obvious scheduling problems early. It also makes the warning messages clearer and easier to explain to the user. The limitation is that two tasks with different start times could still overlap in practice, so this approach does not catch every possible conflict, only the most direct ones.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
