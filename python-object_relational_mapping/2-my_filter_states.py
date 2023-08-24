import sys
import MySQLdb


def search_states(username, password, database, state_name):
    """
    Searches the states table for matching state names and displays the results.
    """
    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the SQL query with the user input using format
    query = """
          SELECT * 
          FROM states 
          WHERE name = '{}' 
          ORDER BY id ASC
    """.format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == '__main__':
    """
     Get the MySQL username, password, database name, and
     state name from command-line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to search and display matching states
    search_states(username, password, database, state_name)

    