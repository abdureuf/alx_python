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
    print(f"Employee Name: {employee_name.ljust(18)}\nTo Do Count: {total_tasks}\n")

    # Print completed tasks
    print(f"Task 1 in output: {done_tasks[0]['title']}")
    for i in range(1, num_done_tasks):
        print(f"Task {i+1} in output: {done_tasks[i]['title']}")

    # Print formatting information
    print(f"\nThe first line formatting: {'OK' if len(f'Employee Name: {employee_name.ljust(18)}') == 26 else 'NOT OK'}")
    print(f"The task 1 formatting: {'OK' if len(f'Task 1 in output: {done_tasks[0]['title']}') == 26 else 'NOT OK'}")
    for i in range(1, num_done_tasks):
        task_num = i + 1
        print(f"The task {task_num} formatting: {'OK' if len(f'Task {task_num} in output: {done_tasks[i]['title']}') == 26 else 'NOT OK'}")

# Example usage
employee_id = 1
get_employee_todo_progress(employee_id)
