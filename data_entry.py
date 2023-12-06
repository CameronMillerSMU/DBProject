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

# TODO: do checks for data entry - Courses, Sections, LearningObjectives

#

def enter_course_data(cursor, connector, c_id, c_title, c_description, dept_code):
    try:
        #insert data into Courses table
        cursor.execute("INSERT INTO Courses (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES (?,?,?,?)",
                   c_id, c_title, c_description, dept_code)
        # commit changes to the database 
        connector.commit()
    except Error as e:
        print(f"Error inserting course data: {e}")

def enter_section_data(cursor, connector, s_id, c_id, semester_id, f_id, students_enrolled):
    try:
        #insert data into Sections table
        cursor.execute("INSERT INTO CourseSections (SectionID, CourseID, SemesterID, FacultyID, StudentsEnrolled) VALUES (?,?,?,?,?)",
                       s_id, c_id, semester_id, f_id, students_enrolled)
        # commit changes to the database 
        connector.commit()
    except Error as e:
        print(f"Error inserting Course Section data: {e}")

def enter_learningObjectives_data(cursor, connector, prog_name, obj_code):
    try:
        #insert data into Learning Objectives table
        cursor.execute("INSERT INTO LearningObjectives (ProgramName, ObjectiveCode) VALUES (?,?)",
                       prog_name, obj_code)
        # commit changes to the database 
        connector.commit()
    except Error as e:
        print(f"Error inserting Learning Objectives data: {e}")
 