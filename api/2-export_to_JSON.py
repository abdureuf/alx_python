import requests
import sys
import json

if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Fetch employee details
employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = employee_response.json()
employee_name = employee_data.get("username")

# Fetch TODO list for the employee
todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos_data = todos_response.json()

# Prepare data for JSON export
export_data = {employee_id: []}

for task in todos_data:
    export_data[employee_id].append(
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
    )

# Export data to JSON file
filename = f"{employee_id}.json"
with open(filename, mode="w") as file:
    json.dump(export_data, file)

print(f"Data exported to {filename} successfully.")