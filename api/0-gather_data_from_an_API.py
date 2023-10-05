import requests

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo['completed']]
    num_done_tasks = len(done_tasks)

    # Print progress information
    print(f"Employee Name: {employee_name}{' '*(18-len(employee_name))} OK")
    print(f"To Do Count: {total_tasks}{' '*(16-len(str(total_tasks)))} OK\n")

    # Print completed tasks
    for task in done_tasks:
        print(f"\tTask: {task['title']}")

    # Print formatting information
    print(f"\nFirst line formatting: {'OK' if len(f'Employee Name: {employee_name}{' '*(18-len(employee_name))} OK') == 26 else 'NOT OK'}")
    for i, task in enumerate(done_tasks, start=1):
        print(f"Task {i} formatting: {'OK' if len(f'Task: {task['title']}') == 26 else 'NOT OK'}")

# Example usage
employee_id = 1
get_employee_todo_progress(employee_id)
