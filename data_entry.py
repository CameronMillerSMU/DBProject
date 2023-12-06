from project import *
import re

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

def check_program_exists(prog_name):
    try:
        com = "SELECT * FROM Program WHERE ProgramName = '%s'" % (prog_name) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Program does not exist. Please check program name")
        return False
    except Error as e:
        print(f"Error executing Program Select: {e}")

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

def check_learningObjective_exists(obj_code):
    try:
        com = "SELECT * FROM LearningObjective WHERE ObjectiveCode = '%s'" % (obj_code) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Learning objective does not exist. Please check Objective ID")
        return False
    except Error as e:
        print(f"Error executing Learning Objective Select: {e}")


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
        return False

def enter_section_data(cursor, connector, course_id, semester, year, f_id, students_enrolled):
    #check if the course and faculty member exist 
    if not check_course_exists(course_id):
        return False 
    if not check_fal_exists(f_id):
        return False

    try:
        #insert data into Sections table
        cursor.execute("INSERT INTO CourseSections (CourseID, SemesterName, CourseYear, FacultyID, StudentsEnrolled) VALUES (?,?,?,?,?)",
                       course_id, semester, year, f_id, students_enrolled)
        # commit changes to the database 
        connector.commit()
        return True
    except Error as e:
        print(f"Error inserting Course Section data: {e}")
        return False

def enter_learningObjective_data(cursor, connector, obj_code, obj_description):
    try:
        #insert data into Learning Objectives table
        cursor.execute("INSERT INTO LearningObjectives (ObjectiveCode, ObjectiveDescription) VALUES (?,?)",
                       obj_code, obj_description)
        # commit changes to the database 
        connector.commit()
        return True
    except Error as e:
        print(f"Error inserting Learning Objectives data: {e}")
        return False

def enter_subObjective_data(cursor, connector, subObj_code, obj_code, subObj_description):
    # check that the learning objective exists
    if not check_learningObjective_exists(obj_code):
        return False
    
    try:
        #insert data into Learning Objective table
        cursor.execute("INSERT INTO LearningObjectives (SubObjectiveCode, SubObjectiveDescription, ObjectiveCode) VALUES (?,?,?)",
                       subObj_code, obj_code, subObj_description)
        # commit changes to the database 
        connector.commit()
        return True
    except Error as e:
        print(f"Error inserting Learning Objectives data: {e}")
        return False

# def enter_courseProgram_data(cursor, connector, course_id, prog_name):
#     # check if course and program exists
#     if not check_course_exists(course_id):
#         return False
#     if not check_program_exists(prog_name):
#         return False
    
#     try:
#         #insert data into CourseEval table
#         cursor.execute("INSERT INTO ProgramCourse (CourseID, ProgramName) VALUES (?,?)",
#                        course_id, prog_name)
#         # commit changes to the database 
#         connector.commit()
#         return True
#     except Error as e:
#         print(f"Error inserting Learning Objectives data: {e}")
#         return False


# Functions to Handle User Input
def handle_course_entry(cursor, connector, course_id, course_title, c_description, dept_code):
    if enter_course_data(cursor, connector, str(course_id), str(course_title), str(c_description), str(dept_code)):
        return "Course data entered successfully."
    else: 
        return "Error entering course data. Please try again."
    
def handle_section_entry(cursor, connector, course_id, semester, year, f_id, students_enrolled):
    if enter_section_data(cursor, connector, str(course_id), str(semester), year, str(f_id), int(students_enrolled)):
        return "Section data entered successfully."
    else: 
        return "Error entering section data. Please try again."

def handle_learningObjective_entry(cursor, connector, obj_code, obj_description):
    if enter_learningObjective_data(cursor, connector, str(obj_code), str(obj_description)):
        return "Learning Objective data entered successfully."
    else: 
        return "Error entering learning objective data. Please try again."

# creates the sub-objective code from the objective code  
def create_subObj_code(cursor, obj_code):
    com = "SELECT COUNT(*) FROM SubObjective WHERE ObjectiveCode = '%s'" % (obj_code)
    cursor.execute(com)

    num = cursor.fetchall()
    num = num[0][0]+1

    code = str(obj_code) + "." + str(num)
    return code

def handle_subObjective_entry(cursor, connector, obj_code, subObj_description):
    # create the sub-objective code 
    subObj_code = create_subObj_code(cursor, obj_code)

    if enter_subObjective_data(cursor, connector, str(subObj_code), str(obj_code), str(subObj_description)):
        return "Sub-objective data entered successfully."
    else: 
        return "Error entering Sub-objective data. Please try again."
    
# def handle_courseProgram_entry(cursor, connector, course_id, prog_name):
#     if enter_courseProgram_data(cursor, connector, str(course_id), str(prog_name)):
#         return "Course was assigned to program successfully."
#     else: 
#         return "Error assigning course to program. Please try again."