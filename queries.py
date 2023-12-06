import mysql.connector as sql
from mysql.connector import Error

# Queries
def get_department(cursor, department_name):
    try:
        cursor.execute("SELECT * FROM Departments WHERE DepartmentName = %s", (department_name,))
        department_data = cursor.fetchone()
        if not department_data:
            print("No department found")
            return

        department_name, department_head_id, department_head_name, department_head_email = department_data
        print(f"Department Name: {department_name}")
        print(f"Department Head ID: {department_head_id}")
        print(f"Department Head Name: {department_head_name}")
        print(f"Department Head Email: {department_head_email}")

    except Error as e:
        print("Invalid input or error:", e)


def get_faculty(cursor, factuly_id):
    try:
        cursor.execute("SELECT * FROM Faculty WHERE FacultyID = %s", (factuly_id,))
        faculty_data = cursor.fetchone()
        if not faculty_data:
            print("No faculty found")
            return

        faculty_id, faculty_name, faculty_email, faculty_office, faculty_phone, faculty_department = faculty_data
        print(f"Faculty ID: {faculty_id}")
        print(f"Faculty Name: {faculty_name}")
        print(f"Faculty Email: {faculty_email}")
        print(f"Faculty Office: {faculty_office}")
        print(f"Faculty Phone: {faculty_phone}")
        print(f"Faculty Department: {faculty_department}")

    except Error as e:
        print("Invalid input or error:", e)

def get_program(cursor, program_name):
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

def get_course(cursor, course_id):
    try:
        # Get course information
        cursor.execute("SELECT * FROM Courses WHERE CourseID = %s", (course_id,))
        course_data = cursor.fetchone()
        if not course_data:
            print("No course found")
            return

        course_id, course_title, course_description, department_code = course_data
        print(f"Course ID: {course_id}")
        print(f"Course Title: {course_title}")
        print(f"Course Description: {course_description}")
        print(f"Department Code: {department_code}")

        # Get course sections
        cursor.execute("SELECT * FROM CourseSections WHERE CourseID = %s", (course_id,))
        sections_data = cursor.fetchall()
        if not sections_data:
            print("No sections found for this course")
            return

        print("Sections:")
        for section in sections_data:
            section_id, semester_name, course_year, faculty_id, students_enrolled = section
            print(f"  - Section ID: {section_id}")
            print(f"    Semester Name: {semester_name}")
            print(f"    Course Year: {course_year}")
            print(f"    Faculty ID: {faculty_id}")
            print(f"    Students Enrolled: {students_enrolled}")

    except Error as e:
        print("Invalid input or error:", e)

def get_section(cursor, section_id, course_id):
    try:
        cursor.execute("SELECT * FROM CourseSections WHERE SectionID = %s AND CourseID = %s", (section_id, course_id))
        section_data = cursor.fetchone()
        if not section_data:
            print("No section found")
            return
        
        section_id, semester_name, course_year, faculty_id, students_enrolled = section_data
        print(f"Section ID: {section_id}")
        print(f"Semester Name: {semester_name}")
        print(f"Course Year: {course_year}")
        print(f"Faculty ID: {faculty_id}")
        print(f"Students Enrolled: {students_enrolled}")

    except Error as e:
        print("Invalid input or error:", e)

def get_learning_objective(cursor, objective_code):
    try:
        cursor.execute("SELECT * FROM LearningObjectives WHERE ObjectiveCode = %s", (objective_code,))
        objective_data = cursor.fetchone()
        if not objective_data:
            print("No objective found")
            return

        objective_code, objective_description = objective_data
        print(f"Objective Code: {objective_code}")
        print(f"Objective Description: {objective_description}")

    except Error as e:
        print("Invalid input or error:", e)

def get_sub_objective(cursor, sub_objective_code):
    try:
        cursor.execute("SELECT * FROM SubObjectives WHERE SubObjectiveCode = %s", (sub_objective_code,))
        sub_objective_data = cursor.fetchone()
        if not sub_objective_data:
            print("No sub-objective found")
            return

        sub_objective_code, sub_objective_description = sub_objective_data
        print(f"Sub-objective Code: {sub_objective_code}")
        print(f"Sub-objective Description: {sub_objective_description}")

    except Error as e:
        print("Invalid input or error:", e)

def get_program_course(cursor, program_name):
    try:
        cursor.execute("SELECT * FROM ProgramCourses WHERE ProgramName = %s", (program_name,))
        program_course_data = cursor.fetchall()
        if not program_course_data:
            print("No program courses found")
            return

        print("Program Courses:")
        for course in program_course_data:
            course_id, course_name = course
            print(f"  - Course ID: {course_id}")
            print(f"    Course Name: {course_name}")

    except Error as e:
        print("Invalid input or error:", e)

def get_program_objective(cursor, program_name):
    try:
        cursor.execute("SELECT * FROM ProgramObjectives WHERE ProgramName = %s", (program_name,))
        program_objective_data = cursor.fetchall()
        if not program_objective_data:
            print("No program objectives found")
            return

        print("Program Objectives:")
        for objective in program_objective_data:
            objective_code = objective[0]
            print(f"  - {objective_code}")

    except Error as e:
        print("Invalid input or error:", e)

def get_course_eval(cursor, course_id, program_name):
    try:
        cursor.execute("SELECT * FROM CourseEvaluations WHERE CourseID = %s AND ProgramName = %s", (course_id, program_name))
        course_eval_data = cursor.fetchall()
        if not course_eval_data:
            print("No course evaluations found")
            return

        print("Course Evaluations:")
        for eval in course_eval_data:
            eval_id, eval_description = eval
            print(f"  - Evaluation ID: {eval_id}")
            print(f"    Evaluation Description: {eval_description}")

    except Error as e:
        print("Invalid input or error:", e)
        
def get_section_eval(cursor, section_id, course_id, program_name):
    try:
        cursor.execute("SELECT * FROM SectionEvaluations WHERE SectionID = %s AND CourseID = %s AND ProgramName = %s", (section_id, course_id, program_name))
        section_eval_data = cursor.fetchall()
        if not section_eval_data:
            print("No section evaluations found")
            return

        print("Section Evaluations:")
        for eval in section_eval_data:
            eval_id, eval_description = eval
            print(f"  - Evaluation ID: {eval_id}")
            print(f"    Evaluation Description: {eval_description}")

    except Error as e:
        print("Invalid input or error:", e)
