from entry import create_connection, create_tables_from_file

# Database connection parameters
host = "localhost"
user = "root"
password = "databases2023"
database_name = "projectDB"

# Create a connection to the database
db_connection = create_connection(host, user, password, database_name)

# Create tables if they don't exist
create_tables_from_file(db_connection.cursor(), "test_schema.sql", db_connection)

# Example data for testing
department_data = [
    ("CS01", "Computer Science"),
    ("ENG01", "Engineering"),
    # Add more departments as needed
]

faculty_data = [
    ("F001", "John Doe", "john.doe@example.com", "CS01", "Professor"),
    ("F002", "Jane Smith", "jane.smith@example.com", "ENG01", "Associate Professor"),
    # Add more faculty members as needed
]

program_data = [
    ("Computer Science Program", "F001", "CS01"),
    ("Engineering Program", "F002", "ENG01"),
    # Add more programs as needed
]

# Insert data into the database
for dept_code, dept_name in department_data:
    handle_department_entry(db_connection.cursor(), db_connection, dept_code, dept_name)

for fac_id, fac_name, fac_email, dept_code, fac_rank in faculty_data:
    handle_faculty_entry(db_connection.cursor(), db_connection, fac_id, fac_name, fac_email, dept_code, fac_rank)

for prog_name, pc_id, dept_code in program_data:
    handle_program_entry(db_connection.cursor(), db_connection, prog_name, pc_id, dept_code)

# Commit changes to the database
db_connection.commit()

# Close the database connection
db_connection.close()

print("Database populated successfully.")