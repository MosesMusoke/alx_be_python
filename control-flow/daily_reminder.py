# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize reminder message
reminder = ""

# Process the task based on priority and time sensitivity
if priority == "high":
    reminder = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    reminder = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    print("Invalid priority level entered.")
    exit()  # Exit the program if an invalid priority level is entered

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)
