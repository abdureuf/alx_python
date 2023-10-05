import sys
import requests
import csv

def gather_data(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("username")

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Export data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            task_id = task.get("id")
            task_title = task.get("title")
            task_completed = task.get("completed")
            writer.writerow([employee_id, employee_name, task_completed, task_title])

    print(f"Data exported to {filename} successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)