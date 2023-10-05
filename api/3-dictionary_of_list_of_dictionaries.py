import requests
import json

# Fetch employee details
employee_response = requests.get("https://jsonplaceholder.typicode.com/users")
employee_data = employee_response.json()

# Fetch TODO list for all employees
todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos_data = todos_response.json()

# Prepare data for JSON export
export_data = {}

for employee in employee_data:
    employee_id = str(employee.get("id"))
    employee_name = employee.get("username")
    export_data[employee_id] = []

    for task in todos_data:
        if task.get("userId") == employee_id:
            export_data[employee_id].append(
                {
                    "username": employee_name,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
            )

# Export data to JSON file
filename = "todo_all_employees.json"
with open(filename, mode="w") as file:
    json.dump(export_data, file)

print(f"Data exported to {filename} successfully.")