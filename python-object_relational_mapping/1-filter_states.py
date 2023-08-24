import sys
import MySQLdb


def list_states_with_n(username, password, database):
    """
     Fetches and lists all states with a name starting with N
     from the specified database.

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

    """
     Execute the query to fetch states starting with N
     By using LIKE to specify the name
    """
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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
     Get the MySQL username, password, and
     database name from command-line arguments
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """
        Call the function to list states
        starting with N(upper case)

    """
    list_states_with_n(username, password, database)
