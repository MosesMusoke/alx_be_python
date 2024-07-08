task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").strip().lower()

time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level entered."
        time_bound = "no" 

if time_bound == "yes" and "Invalid" not in reminder:
    reminder += " that requires immediate attention today!"

if time_bound == "no" and priority == "low":
    reminder += " Consider completing it when you have free time."

print(reminder)
