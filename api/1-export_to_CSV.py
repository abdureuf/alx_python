import csv
import requests
import sys



def export_employee_todo_to_csv(employee_id):
    """
    Export the employee's TODO list to a CSV file.
    """
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_username = employee_data['username']

    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Prepare CSV filename
    filename = f"{employee_id}.csv"

    # Write TODO list to CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos_data:
            task_completed = str(todo['completed'])
            task_title = todo['title']
            writer.writerow([employee_id, employee_username, task_completed, task_title])

    print(f"Data exported to {filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_to_csv(employee_id)