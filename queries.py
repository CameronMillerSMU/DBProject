import mysql.connector as sql
from mysql.connector import Error

def create_connection(host, user, password, database):
    try:
        connection = sql.connect(host=host, user=user, password=password, database=database)
        print("Connected to the database")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Replace these values with your actual database credentials
host = "your_host"
user = "your_user"
password = "your_password"
database = "your_database"


# Queries

def get_program_info(cursor, program_name):
    try:
        # Get program information
        cursor.execute("SELECT * FROM Programs WHERE ProgramName = %s", (program_name,))
        program_data = cursor.fetchone()
        if not program_data:
            print("No program found")
            return

        program_name, coordinator_id, coordinator_name, coordinator_email = program_data
        print(f"Program Name: {program_name}")
        print(f"Coordinator ID: {coordinator_id}")
        print(f"Coordinator Name: {coordinator_name}")
        print(f"Coordinator Email: {coordinator_email}")

        # Get program objectives
        cursor.execute("SELECT ObjectiveCode FROM ProgramObjectives WHERE ProgramName = %s", (program_name,))
        objectives_data = cursor.fetchall()
        if not objectives_data:
            print("No objectives found for this program")
            return

        print("Objectives:")
        for objective in objectives_data:
            objective_code = objective[0]
            print(f"  - {objective_code}")

    except Error as e:
        print("Invalid input or error:", e)



# Connect to the database
connection = create_connection(host, user, password, database)

# Create a cursor
cursor = connection.cursor()

# Get program information
get_program_info(cursor, "Computer Science")

# Close the connection
connection.close()
