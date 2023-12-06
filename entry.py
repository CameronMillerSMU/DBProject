from project import *
import csv
import mysql.connector as sql
from mysql.connector import Error
import re

"""CHANGE THIS TO RUN"""
# dbConn = create_connection("localhost", "root", "beepboop", "progDB")
# cursor = dbConn.cursor()
# create_database(cursor, "progDB")

'''General Database Functions'''

tables = ["Program", "Department", "Faculty", "Course", "Section", 
          "LearningObjective", "SubObjective", "CourseEval",
          "SectionEval", "ProgramObjective", "ProgramCourse"]

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


# clear_database(cursor, dbConn, tables)
# create_tables_from_file(cursor, "test_schema.sql", dbConn)

'''Input Handling Helper Functions'''
def verify_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    match = re.match(email_pattern, email)
    return bool(match)

def check_dept_code(dept_code):
    dept_pattern = re.compile(r'^[a-zA-Z]{4}$')
    match = re.match(dept_pattern, dept_code)
    return bool(match)

def check_course_id(c_id):
    id_pattern = re.compile(r'^[a-zA-Z]{4}[0-9]{4}$')
    match = re.match(id_pattern, c_id)
    return bool(match)


'''Database Entry Helper Functions'''

def check_dept_exists(cursor, dept_code):
    try:
        com = "SELECT * FROM Department WHERE DepartmentCode = '%s'" % (dept_code) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Department does not exist. Please check department code.")
        return False
    except Error as e:
        print(f"Error executing Department Select: {e}")
        
        
def check_fal_exists(cursor, fal_id):
    try:
        com = "SELECT * FROM Faculty WHERE FacultyID = '%s'" % (fal_id) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Faculty member does not exist. Please check faculty id")
        return False
    except Error as e:
        print(f"Error executing Faculty Select: {e}")
        return False
        
def check_program_exists(cursor, prog_name):
    try:
        com = "SELECT * FROM Program WHERE ProgramName = '%s'" % (prog_name) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Program does not exist. Please check program name")
        return False
    except Error as e:
        print(f"Error executing Program Select: {e}")
        return False

def check_course_exists(cursor, course_id):
    try:
        com = "SELECT * FROM Course WHERE CourseID = '%s'" % (course_id) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Course does not exist. Please check Course ID")
        return False
    except Error as e:
        print(f"Error executing Course Select: {e}")

def check_learningObjective_exists(cursor, obj_code):
    try:
        com = "SELECT * FROM LearningObjective WHERE ObjectiveCode = '%s'" % (obj_code) 
        cursor.execute(com)
        
        if cursor.fetchall():
            return True
        
        print("Learning objective does not exist. Please check Objective ID")
        return False
    except Error as e:
        print(f"Error executing Learning Objective Select: {e}")

# creates the sub-objective code from the objective code  
def create_subObj_code(cursor, obj_code):
    com = "SELECT COUNT(*) FROM SubObjective WHERE ObjectiveCode = '%s'" % (obj_code)
    cursor.execute(com)

    num = cursor.fetchall()
    num = num[0][0]+1

    code = str(obj_code) + "." + str(num)
    return code

'''Database Entry Functions'''

def enter_program_info(cursor, connection, prog_name, pc_id, dept_code):
    '''Check to see if program coordinator exists, if not add them to the faculty table'''
    
    #check if department exists, if not, return error 
    if not check_dept_exists(dept_code):
        return False
    
    if not check_fal_exists(pc_id):
        return False
    
    try:
        # Insert data into the Programs table
        sqlcom = "INSERT INTO Program \
        (ProgramName, ProgramCoordinatorID, DepartmentCode) \
        VALUES (%s, %s, %s)"
        
        program_data = (prog_name, pc_id, dept_code)
        
        cursor.execute(sqlcom, program_data)
        # Commit the transaction
        connection.commit()

        print(f"Data for program '{prog_name}' successfully inserted into the Programs table.")
        return True
    except Error as e:
        print(f"Error inserting program data: {e}")
        return False
    

def enter_department_info(cursor, connection, dept_code, dept_name):
    try:
        # Insert data into the Departments table
        sqlcom = "INSERT INTO Department (DepartmentCode, DepartmentName) \
            VALUES (%s, %s)"
        dept_info = (dept_code, dept_name)
        cursor.execute(sqlcom, dept_info)

        # Commit the transaction
        connection.commit()

        print(f"Data for department '{dept_name}' successfully inserted into the Departments table.")
        return True
    except Error as e:
        print(f"Error inserting department data: {e}")
        return False

def enter_faculty_info(cursor, connection, fac_id, fac_name, fac_email, dept_code, fac_rank):    
    try:
        if not check_dept_exists(dept_code):
            return False
    
        # Insert data into the Faculty table
        sqlcom = "INSERT INTO Faculty (FacultyID, FacultyName, FacultyEmail, FacultyRank, DepartmentCode) \
        VALUES (%s, %s, %s, %s, %s)"
        faculty_data = (fac_id, fac_name, fac_email, fac_rank, dept_code)
        cursor.execute(sqlcom, faculty_data)

        # Commit the transaction
        connection.commit()

        print(f"Data for faculty '{fac_name}' successfully inserted into the Faculty table.")
        return True
    except Error as e:
        print(f"Error inserting faculty data: {e}")
        return False

def enter_course_info(cursor, connection, co_id, co_title, co_desc, dept_code):
    if not check_dept_exists(dept_code):
        return False
    
    try:
        # Insert data into the Courses table
        sqlcom = "INSERT INTO Course (CourseID, CourseTitle, CourseDescription, DepartmentCode) \
            VALUES (%s, %s, %s, %s)"
        course_data = (co_id, co_title, co_desc, dept_code)
        cursor.execute(sqlcom, course_data)

        # Commit the transaction
        connection.commit()

        print(f"Data for course '{co_title}' successfully inserted into the Courses table.")
        return True
    except Error as e:
        print(f"Error inserting course data: {e}")
        return False
    
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


'''Assign Course to Program'''
def assign_course_to_program(cursor, connector, course_id, prog_name):
    # check if course and program exists
    if not check_course_exists(course_id):
        return False
    if not check_program_exists(prog_name):
        return False

    try:
        #insert data into CourseEval table
        cursor.execute("INSERT INTO ProgramCourse (CourseID, ProgramName) VALUES (?,?)",
                       course_id, prog_name)
        # commit changes to the database 
        connector.commit()
        return True
    except Error as e:
        print(f"Error inserting Learning Objectives data: {e}")
        return False
    
'''Assigning learning (sub)objectives to (course, program) pairs (remember, a course can
be associated with multiple programs, and for each program, the objectives can be
different).'''
def assign_obj_to_course(cursor, connection, co_id, prog_name, obj_code):
    # check if course, program pair exists
    com = "SELECT * FROM ProgramCourse WHERE ProgramName = '%s' AND CourseID = '%s'" % (prog_name, co_id)
    cursor.execute(com)
    
    if cursor.fetchall(): 
        try:
            sqlcom = "INSERT INTO ProgramCourse (CourseID, ProgramName) \
                VALUES (%s, %s)"
            course_data = (co_id, prog_name)
            cursor.execute(sqlcom, course_data)

            # Commit the transaction
            connection.commit()
            return True
        except Error as e:
            print(f"Error inserting Program Course data: {e}")
            return False
    return False


'''Input Handling Functions'''

def handle_program_entry(cursor, connection, name, pc_id, dept_code):
    if not check_dept_code(dept_code):
        return "Error: Department Code not valid"
    
    if enter_program_info(cursor, connection, str(name), str(pc_id), str(dept_code)):
        return "Program Info Stored Successfully"
    else:
        return "There was an issue entering the information, please try again."
    
def handle_department_entry(cursor, connection, dept_code, dept_name):
    if not check_dept_code(dept_code):
        return "Error: Department Code not valid"
    
    if enter_department_info(cursor, connection, str(dept_code), str(dept_name)):
        return "Department Info Stored Successfully"
    else:
        return "There was an issue entering the information, please try again."
    
def handle_faculty_entry(cursor, connection, fac_id, fac_name, fac_email, dept_code, fac_rank = "Adjunct"):
    if not check_dept_code(dept_code):
        return "Departement Code not valid"
    
    if verify_email(fac_email):
        if enter_faculty_info(cursor, connection, fac_id, fac_name, fac_email, dept_code, fac_rank):
            return "Faculty Info Stored Successfully"
    else:
        return "Email is not valid. Please try again."

    
def handle_course_entry(cursor, connection, co_id, co_title, co_desc, dept_code):
    if not check_dept_code(dept_code) and check_course_id(co_id):
        return "Department Code or Course ID not valid"
    
    if enter_course_info(cursor, connection, str(co_id), str(co_title), str(co_desc), str(dept_code)):
        return "Course Info Stored Successfully"
    
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
    
def handle_subObjective_entry(cursor, connector, obj_code, subObj_description):
    # create the sub-objective code 
    subObj_code = create_subObj_code(cursor, obj_code)

    if enter_subObjective_data(cursor, connector, str(subObj_code), str(obj_code), str(subObj_description)):
        return "Sub-objective data entered successfully."
    else: 
        return "Error entering Sub-objective data. Please try again."
    

''' Populate Functions '''
def populate_course_table(cursor, connection):
    dummy_courses = [
        ("CS010001", "Introduction to Computer Science", "Fundamental concepts of programming.", "CS01"),
        ("EN010001", "Engineering Basics", "Introduction to engineering principles.", "EN01"),
        ("BO010001", "Introduction to Biology", "Basic concepts in biology.", "BO01"),
    ]

    try:
        sqlcom = "INSERT INTO Course (CourseID, CourseTitle, CourseDescription, DepartmentCode) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sqlcom, dummy_courses)
        connection.commit()

        print("Dummy data successfully inserted into the Course table.")
    except Error as e:
        print(f"Error inserting dummy data into the Course table: {e}")

def populate_course_eval_table(cursor, connection):
    dummy_course_evals = [
        ("CS010001", "Computer Science Program", "LO001"),
        ("EN010001", "Engineering Program", "LO002"),
        ("BO010001", "Biology Program", "LO003"),
    ]

    try:
        sqlcom = "INSERT INTO CourseEval (CourseID, ProgramName, ObjectiveCode) VALUES (%s, %s, %s)"
        cursor.executemany(sqlcom, dummy_course_evals)
        connection.commit()

        print("Dummy data successfully inserted into the CourseEval table.")
    except Error as e:
        print(f"Error inserting dummy data into the CourseEval table: {e}")


def populate_departments_table(cursor, connection):
    dummy_departments = [
        ("CS01", "Computer Science"),
        ("EN01", "Engineering"),
        ("BO01", "Biology"),
    ]

    try:
        sqlcom = "INSERT INTO Department (DepartmentCode, DepartmentName) VALUES (%s, %s)"
        cursor.executemany(sqlcom, dummy_departments)
        connection.commit()

        print("Dummy data successfully inserted into the Departments table.")
    except Error as e:
        print(f"Error inserting dummy data into the Departments table: {e}")

def populate_faculty_table(cursor, connection):
    dummy_faculty = [
        ("F001", "John Doe", "john.doe@example.com", "Full", "CS01"),
        ("F002", "Jane Smith", "jane.smith@example.com", "Associate", "EN01"),
        ("F003", "Bob Johnson", "bob.johnson@example.com", "Assistant", "BO01"),
    ]

    try:
        sqlcom = "INSERT INTO Faculty (FacultyID, FacultyName, FacultyEmail, FacultyRank, DepartmentCode) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(sqlcom, dummy_faculty)
        connection.commit()

        print("Dummy data successfully inserted into the Faculty table.")
    except Error as e:
        print(f"Error inserting dummy data into the Faculty table: {e}")

def populate_learning_objective_table(cursor, connection):
    dummy_learning_objectives = [
        ("LO001", "Understand fundamental programming concepts."),
        ("LO002", "Apply engineering principles to problem-solving."),
        ("LO003", "Comprehend basic biological concepts."),
    ]

    try:
        sqlcom = "INSERT INTO LearningObjective (ObjectiveCode, ObjectiveDescription) VALUES (%s, %s)"
        cursor.executemany(sqlcom, dummy_learning_objectives)
        connection.commit()

        print("Dummy data successfully inserted into the LearningObjective table.")
    except Error as e:
        print(f"Error inserting dummy data into the LearningObjective table: {e}")

def populate_program_table(cursor, connection):
    dummy_programs = [
        ("Computer Science Program", "F001", "CS01"),
        ("Engineering Program", "F002", "EN01"),
        ("Biology Program", "F003", "BO01"),
    ]

    try:
        sqlcom = "INSERT INTO Program (ProgramName, ProgramCoordinatorID, DepartmentCode) VALUES (%s, %s, %s)"
        cursor.executemany(sqlcom, dummy_programs)
        connection.commit()

        print("Dummy data successfully inserted into the Program table.")
    except Error as e:
        print(f"Error inserting dummy data into the Program table: {e}")

def populate_program_course_table(cursor, connection):
    dummy_program_courses = [
        ("CS010001", "Computer Science Program"),
        ("EN010001", "Engineering Program"),
        ("BO010001", "Biology Program"),
    ]

    try:
        sqlcom = "INSERT INTO ProgramCourse (CourseID, ProgramName) VALUES (%s, %s)"
        cursor.executemany(sqlcom, dummy_program_courses)
        connection.commit()

        print("Dummy data successfully inserted into the ProgramCourse table.")
    except Error as e:
        print(f"Error inserting dummy data into the ProgramCourse table: {e}")

def populate_program_objective_table(cursor, connection):
    dummy_program_objectives = [
        ("Computer Science Program", "LO001"),
        ("Engineering Program", "LO002"),
        ("Biology Program", "LO003"),
    ]

    try:
        sqlcom = "INSERT INTO ProgramObjective (ProgramName, ObjectiveCode) VALUES (%s, %s)"
        cursor.executemany(sqlcom, dummy_program_objectives)
        connection.commit()

        print("Dummy data successfully inserted into the ProgramObjective table.")
    except Error as e:
        print(f"Error inserting dummy data into the ProgramObjective table: {e}")

def populate_section_table(cursor, connection):
    dummy_sections = [
        (1, "CS010001", "Fall", 2023, "F001", 30),
        (2, "EN010001", "Spring", 2023, "F002", 25),
        (3, "BO010001", "Summer", 2023, "F003", 20),
    ]

    try:
        sqlcom = "INSERT INTO Section (SectionID, CourseID, SemesterName, CourseYear, FacultyID, StudentsEnrolled) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(sqlcom, dummy_sections)
        connection.commit()

        print("Dummy data successfully inserted into the Section table.")
    except Error as e:
        print(f"Error inserting dummy data into the Section table: {e}")

def populate_section_eval_table(cursor, connection):
    dummy_section_evals = [
        (1, "CS010001", "Computer Science Program", "LO001", "Exam", 25),
        (2, "EN010001", "Engineering Program", "LO002", "Project", 20),
        (3, "BO010001", "Biology Program", "LO003", "Quiz", 15),
    ]

    try:
        sqlcom = "INSERT INTO SectionEval (SectionID, CourseID, ProgramName, ObjectiveCode, EvalType, StudentsMetObj) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(sqlcom, dummy_section_evals)
        connection.commit()

        print("Dummy data successfully inserted into the SectionEval table.")
    except Error as e:
        print(f"Error inserting dummy data into the SectionEval table: {e}")

def populate_sub_objective_table(cursor, connection):
    dummy_sub_objectives = [
        ("LO001.1", "Write basic programs in a chosen programming language.", "LO001"),
        ("LO002.1", "Apply mathematical concepts to engineering problems.", "LO002"),
        ("LO003.1", "Understand the process of cellular respiration.", "LO003"),
    ]

    try:
        sqlcom = "INSERT INTO SubObjective (SubObjectiveCode, SubObjectiveDescription, ObjectiveCode) VALUES (%s, %s, %s)"
        cursor.executemany(sqlcom, dummy_sub_objectives)
        connection.commit()

        print("Dummy data successfully inserted into the SubObjective table.")
    except Error as e:
        print(f"Error inserting dummy data into the SubObjective table: {e}")

# needs to be in a specific order 
def populate_all_tables(cursor, connection):
    populate_departments_table(cursor, connection)
    populate_faculty_table(cursor, connection)
    populate_program_table(cursor, connection)
    populate_course_table(cursor, connection)
    populate_section_table(cursor, connection)
    populate_learning_objective_table(cursor, connection)
    populate_sub_objective_table(cursor, connection)
    populate_program_course_table(cursor, connection)
    populate_program_objective_table(cursor, connection)
    populate_course_eval_table(cursor, connection)
    populate_section_eval_table(cursor, connection)
