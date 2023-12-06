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

# CHECKS 
def check_dept_exists(dept_code):
    try:
        com = "SELECT * FROM Department WHERE DepartmentCode = '%s'" % (dept_code) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Department does not exist. Please check department code.")
        return False
    except Error as e:
        print(f"Error executing Department Select: {e}")

def check_fal_exists(fal_id):
    try:
        com = "SELECT * FROM Faculty WHERE FacultyID = '%s'" % (fal_id) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Faculty member does not exist. Please check faculty id")
        return False
    except Error as e:
        print(f"Error executing Faculty Select: {e}")

def check_course_exists(course_id):
    try:
        com = "SELECT * FROM Course WHERE CourseID = '%s'" % (course_id) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Course does not exist. Please check Course ID")
        return False
    except Error as e:
        print(f"Error executing Course Select: {e}")

# ENTER DATA INTO TABLES
def enter_course_data(cursor, connector, course_id, course_title, c_description, dept_code):
    # check if the dept exists - if not, return error
    if not check_dept_exists(dept_code):
        return False
    
    try:
        #insert data into Course table
        cursor.execute("INSERT INTO Course (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES (?,?,?,?)",
                   course_id, course_title, c_description, dept_code)
        # commit changes to the database 
        connector.commit()
        return True
    except Error as e:
        print(f"Error inserting course data: {e}")

def enter_section_data(cursor, connector, section_id, course_id, semester, year, f_id, students_enrolled):
    #check if the course and faculty member exist 
    if not check_course_exists(course_id):
        return False 
    if not check_fal_exists(f_id):
        return False

    try:
        #insert data into Sections table
        cursor.execute("INSERT INTO CourseSections (SectionID, CourseID, SemesterName, CourseYear, FacultyID, StudentsEnrolled) VALUES (?,?,?,?,?,?)",
                       section_id, course_id, semester, year, f_id, students_enrolled)
        # commit changes to the database 
        connector.commit()
        return True
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



 