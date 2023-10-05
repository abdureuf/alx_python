import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee details
employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = employee_response.json()
employee_name = employee_data.get("name")

# Fetch TODO list for the employee
todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos_data = todos_response.json()

# Calculate completed tasks
completed_tasks = [task for task in todos_data if task.get("completed")]

# Export data to CSV file
filename = f"{employee_id}.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for task in completed_tasks:
        writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

print(f"Data exported to {filename} successfully.")