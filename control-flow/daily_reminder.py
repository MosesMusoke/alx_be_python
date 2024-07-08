# Prompt for task and store it
  task = input("Enter your task: ")

  # Prompt for priority (high, medium, low) and store it
  while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ("high", "medium", "low"):
      break
    else:
      print("Invalid priority. Please enter high, medium, or low.")

  # Prompt for time sensitivity (yes or no) and store it
  while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ("yes", "no"):
      break
    else:
      print("Invalid input. Please enter yes or no.")

  # Process the task based on priority and time sensitivity
  Reminder = f"Reminder: '{task}' is a {priority} priority task. "

  match priority:
    case "high":
      Reminder += "Consider completing it today."
      if time_bound == "yes":
        Reminder += " It requires immediate attention!"
    case "medium":
      Reminder += "Keep it in mind for this week."
    case "low":
      Reminder += "Consider completing it when you have free time."

  # Print the reminder message
  print(Reminder)
