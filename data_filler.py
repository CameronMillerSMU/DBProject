from data_entry import *


''' Test Populate Functions ''' # do not need to use functions 
def populate_course_table(cursor, connection):
    dummy_courses = [
        ("CS0001", "Introduction to Computer Science", "Fundamental concepts of programming.", "CS"),
        ("EN0001", "Engineering Basics", "Introduction to engineering principles.", "EN"),
        ("BIO0001", "Introduction to Biology", "Basic concepts in biology.", "BIO"),
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
        ("CS0001", "Computer Science Program", "LO001"),
        ("EN0001", "Engineering Program", "LO002"),
        ("BIO0001", "Biology Program", "LO003"),
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
        ("CS", "Computer Science"),
        ("EN", "Engineering"),
        ("BIO", "Biology"),
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
        ("F001", "John Doe", "john.doe@example.com", "Full", "CS"),
        ("F002", "Jane Smith", "jane.smith@example.com", "Associate", "EN"),
        ("F003", "Bob Johnson", "bob.johnson@example.com", "Assistant", "BIO"),
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
        ("Computer Science Program", "F001", "CS"),
        ("Engineering Program", "F002", "EN"),
        ("Biology Program", "F003", "BIO"),
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
        ("CS0001", "Computer Science Program"),
        ("EN0001", "Engineering Program"),
        ("BIO0001", "Biology Program"),
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
        (1, "CS0001", "Fall", 2023, "F001", 30),
        (2, "EN0001", "Spring", 2023, "F002", 25),
        (3, "BIO0001", "Summer", 2023, "F003", 20),
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
        (1, "CS0001", "Computer Science Program", "LO001", "Exam", 25),
        (2, "EN0001", "Engineering Program", "LO002", "Project", 20),
        (3, "BIO0001", "Biology Program", "LO003", "Quiz", 15),
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


def driver():
    
    """CHANGE THIS TO RUN"""
    dbConn = create_connection("localhost", "root", "beepboop", "progDB")
    # print(dbConn)
    cursor = dbConn.cursor()
    create_database(cursor, "progDB")
    clear_database(cursor, dbConn, tables)
    
    create_tables_from_file(cursor, "test_schema.sql", dbConn)
    
    # populate_all_tables(cursor, dbConn)
    
    print(handle_department_entry(cursor, dbConn, "ABCD", "ABCD Department")) # good
    print(handle_faculty_entry(cursor, dbConn, "1111111", "Test Falc", "faltest@gmail.com", "ABCD", "Adjunct")) #good
    print(handle_program_entry(cursor, dbConn, "Test 2 Program", "1111111", "ABCD")) # good
    # print(handle_faculty_entry(cursor, dbConn, "1111113", "Test Falc 3", "faltest3@gmail.com", "ABCD", "boop")) #fail
    #handle_course_entry(cursor, dbConn, "CS1111", "Test Course", "hello this course is for dunces like you", "0000")
    print(handle_course_entry(cursor, dbConn, "ABCD0001", "Learning Abc's", "learn something", "ABCD"))
    print(handle_course_entry(cursor, dbConn, "ABCD3000", "Making Abc's", "making an alphabet", "ABCD"))
    print(handle_section_entry(cursor, dbConn, "ABCD0001", "Fall", 2023, "1111111", 20))
    print(handle_section_entry(cursor, dbConn, "ABCD3000", "Fall", 2023, "1111111", 20))
    print(handle_section_entry(cursor, dbConn, "ABCD0001", "Fall", 2023, "1111111", 10))
    print(handle_learningObjective_entry(cursor, dbConn, "LO1", "here is the decription"))
    print(handle_subObjective_entry(cursor, dbConn, "LO1", "here is the sub objective description"))
    print(handle_courseProgram_assignment(cursor, dbConn, "ABCD0001", "Test 2 Program"))
    print(handle_objCourse_assignment(cursor, dbConn, "ABCD0001",  "Test 2 Program", "LO1"))
    print(handle_sectionEval_entry(cursor, dbConn, "1", "ABCD0001", "Test 2 Program", "LO1", 20, "test"))

    #TODO: test handle_sectionEval_entry