from project import *

db_conn = create_connection("localhost", "root", "beepboop", "DBprog")
cursor = db_conn.cursor()
create_database(cursor, "DBprog")

#todo: create the tables from file 
def execute_scripts_from_file(filename):
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()

    # get commands 
    sql_commands = sql_file.split(';')

    # execute comamnds in file
    for command in sql_commands:
        try:
            cursor.execute(command)
        except Error as e:
            print(f"The error '{e}' occurred")

execute_scripts_from_file("test_schema.sql")

# TODO: data entry for Courses, Sections & Learning objectives / sub-objectives

def enter_course_data(cursor, db_conn, c_id, c_title, c_description, dp_code):
    try:
        #insert data into Courses table
        cursor.execute("INSERT INTO COURSES (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES (?,?,?,?)",
                   c_id, c_title, c_description, dp_code)
        # commit changes to the database 
        db_conn.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def enter_section_data(cursor, db_conn):
    try:
        #insert data into Sections table
        cursor.execute("")
        # commit changes to the database 
        db_conn.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def enter_learningObjectives_data(cursor, db_conn):
    try:
        #insert data into Learning Objectives table
        cursor.execute("")
        # commit changes to the database 
        db_conn.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
 