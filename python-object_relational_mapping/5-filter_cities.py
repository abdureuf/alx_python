import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a specific state from the specified database.
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

    # Create the SQL query to select cities of the specified state and order by id
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    if rows:
        city_names = ', '.join(row[0] for row in rows)
        print(city_names)

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

    # Call the function to list cities of the specified state
    list_cities_by_state(username, password, database, state_name)
