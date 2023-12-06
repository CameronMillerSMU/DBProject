import mysql.connector as sql
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = sql.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL server successful!")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_tables_from_file(cursor, filename, connection):
    try:
        with open(filename, 'r') as file:
            sql_script = file.read()

        for result in cursor.execute(sql_script, multi=True):
            pass
        print("Tables created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_sample_data(cursor, connection):
    try:
        # Insert sample data into the tables
        # You can customize these INSERT statements with your own data
        cursor.execute("INSERT INTO Department (DepartmentCode, DepartmentName) VALUES ('COMP', 'Computer Science')")
        cursor.execute("INSERT INTO Faculty (FacultyID, FacultyName, FacultyEmail, FacultyRank, DepartmentCode) VALUES ('F101', 'John Doe', 'john@example.com', 'Professor', 'COMP')")
        cursor.execute("INSERT INTO Course (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES ('CSCI101', 'Introduction to CS', 'Introductory course', 'COMP')")
        cursor.execute("INSERT INTO CourseSections (CourseID, SemesterName, CourseYear, FacultyID, StudentsEnrolled) VALUES ('CSCI101', 'Fall', 2023, 'F101', 30)")

        connection.commit()
        print("Sample data inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    host = "localhost"
    user = "root"
    password = "123456"
    database_name = "progDB"

    # Create a connection and a cursor
    connection = create_connection(host, user, password)
    cursor = connection.cursor()

    # Create the database
    create_database(cursor, database_name)

    # Connect to the created database
    connection = create_connection(host, user, password, database_name)
    cursor = connection.cursor()

    # Execute the SQL script to create tables
    create_tables_from_file(cursor, "test_schema.sql", connection)

    # Insert sample data
    insert_sample_data(cursor, connection)

    # Clean up: Close the connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
import mysql.connector as sql
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = sql.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL server successful!")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_tables_from_file(cursor, filename, connection):
    try:
        with open(filename, 'r') as file:
            sql_script = file.read()

        for result in cursor.execute(sql_script, multi=True):
            pass
        print("Tables created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_sample_data(cursor, connection):
    try:
        # Insert sample data into the tables
        # You can customize these INSERT statements with your own data
        cursor.execute("INSERT INTO Department (DepartmentCode, DepartmentName) VALUES ('COMP', 'Computer Science')")
        cursor.execute("INSERT INTO Faculty (FacultyID, FacultyName, FacultyEmail, FacultyRank, DepartmentCode) VALUES ('F101', 'John Doe', 'john@example.com', 'Professor', 'COMP')")
        cursor.execute("INSERT INTO Course (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES ('CSCI101', 'Introduction to CS', 'Introductory course', 'COMP')")
        cursor.execute("INSERT INTO CourseSections (CourseID, SemesterName, CourseYear, FacultyID, StudentsEnrolled) VALUES ('CSCI101', 'Fall', 2023, 'F101', 30)")

        connection.commit()
        print("Sample data inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    host = "localhost"
    user = "root"
    password = "123456"
    database_name = "progDB"

    # Create a connection and a cursor
    connection = create_connection(host, user, password)
    cursor = connection.cursor()

    # Create the database
    create_database(cursor, database_name)

    # Connect to the created database
    connection = create_connection(host, user, password, database_name)
    cursor = connection.cursor()

    # Execute the SQL script to create tables
    create_tables_from_file(cursor, "test_schema.sql", connection)

    # Insert sample data
    insert_sample_data(cursor, connection)

    # Clean up: Close the connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
