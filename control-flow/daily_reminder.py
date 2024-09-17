task = str(input("Enter your task:"))

priority = str(input("Priority (high, medium, low):"))

time_bound = str (input("Is it time-bound?(yes or no):"))


match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
             print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
             print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")