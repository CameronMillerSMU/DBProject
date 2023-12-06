from project import *

db_conn = create_connection("localhost", "root", "beepboop", "progDB")
cursor = db_conn.cursor()

create_database(cursor, "DBprog")

tables = ["Program", "Department", "Faculty", "Course", "Section", 
          "LearningObjective", "SubObjective", "CourseEval",
          "SectionEval", "ProgramObjective"]

def clear_database(cursor, connection, tableList):
    try:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table in tableList:
            sqlcom = "DROP TABLE IF EXISTS %s" % (table)
            cursor.execute(sqlcom)
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        print("Database cleared successfully")
    except Error as e:
        print(f"The error '{e} occurred'")
    connection.commit()

clear_database(cursor, db_conn, tables)

#create the tables from file 
def create_tables_from_file_m(cursor, filename, connection):
    try:
        with open(filename,'r') as file:
            sql_script = file.read()
            
        for result in cursor.execute(sql_script, multi=True):
            pass
    except Error as e:
        print(f"The error '{e} occurred'")
    
    connection.commit()

create_tables_from_file_m(cursor, "test_schema.sql", db_conn)

# TODO: do checks for data entry - Courses, Sections, LearningObjectives

# courses - checks 
#   - does the dept exist
#       - if so, continue 
#       - if not, error
# sections - checks 
#   - does the course and faculty member exist 
#       - if so, continue
#       - if not, error (course or faculty member does not exist
# learning objectives - no checks needed (check happen outside function in gui)
##

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

def enter_learningObjectives_data(cursor, connector, obj_code, obj_description):
    try:
        #insert data into Learning Objectives table
        cursor.execute("INSERT INTO LearningObjectives (ObjectiveCode, ObjectiveDescription) VALUES (?,?)",
                       obj_code, obj_description)
        # commit changes to the database 
        connector.commit()
    except Error as e:
        print(f"Error inserting Learning Objectives data: {e}")



 