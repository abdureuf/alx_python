import csv
import requests
import sys

def user_info(id):
    """
    Retrieve and display the user information.
    """
    # Get user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data['username']

    # Get user's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Prepare CSV filename
    filename = f"{id}.csv"

    # Write TODO list to CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            completed = todo["completed"]
            title = todo["title"]
            writer.writerow([id, username, completed, title])

    print("Number of tasks in CSV: OK")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    user_info(user_id)