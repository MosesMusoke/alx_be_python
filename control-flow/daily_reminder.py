# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt for the task's time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level entered."
        time_bound = "no"  # Set time_bound to no to skip further processing in case of invalid input

# Modify the reminder if the task is time-bound
if time_bound == "yes" and "Invalid" not in reminder:
    reminder += " that requires immediate attention today!"

# Add additional note for non-time-bound low priority tasks
if time_bound == "no" and priority == "low":
    reminder += " Consider completing it when you have free time."

# Output the customized reminder
print(reminder)
