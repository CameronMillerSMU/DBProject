import mysql.connector as sql
from mysql.connector import Error
import re

# Queries
def get_department(cursor, department_code):
    try:
        cursor.execute("SELECT * FROM Department WHERE DepartmentCode = %s", (department_code,))
        department_data = cursor.fetchone()
        if not department_data:
            return None

        return department_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_faculty(cursor, faculty_id):
    try:
        cursor.execute("SELECT * FROM Faculty WHERE FacultyID = %s", (faculty_id,))
        faculty_data = cursor.fetchone()
        if not faculty_data:
            return None

        return faculty_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_program(cursor, program_name):
    try:
        cursor.execute("SELECT * FROM Program WHERE ProgramName = %s", (program_name,))
        program_data = cursor.fetchone()
        if not program_data:
            return None

        return program_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_section_eval_results(cursor, semester_name, program_name):
    try:
        cursor.execute("""
            SELECT se.SectionID, se.CourseID, se.ProgramName, se.ObjectiveCode, se.EvalType, se.StudentsMetObj
            FROM SectionEval se
            INNER JOIN Section s ON se.SectionID = s.SectionID AND se.CourseID = s.CourseID
            WHERE s.SemesterName = %s AND se.ProgramName = %s
        """, (semester_name, program_name))
        
        section_eval_results = cursor.fetchall()
        return section_eval_results

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_academic_year(cursor, academic_year):
    try:
        # if the value inserted doesn't match the format, show an error message
        if not re.match(r'\d{2}-\d{2}', academic_year):
            print("Invalid academic year format. Please use the format YY-YY")
            return "Invalid academic year format. Please use the format YY-YY"

        # Extract start and end years from the academic year format
        start_year, end_year = map(int, academic_year.split('-'))
        start_year += 2000
        end_year += 2000

        semesters = []
        for year in range(start_year, end_year + 1):
            semesters.append((year, 'Summer'))
            semesters.append((year, 'Fall'))
            if year < end_year:
                semesters.append((year, 'Spring'))

        academic_year_results = []

        for year, semester in semesters:
            # Construct the semester and year in the format present in the database
            semester_name = f"{semester} {year}"

            cursor.execute("""
                SELECT se.ObjectiveCode, se.EvalType, se.StudentsMetObj, pc.CourseID, pc.ProgramName, se.SectionID
                FROM SectionEval se
                LEFT JOIN ProgramCourse pc ON se.CourseID = pc.CourseID AND se.ProgramName = pc.ProgramName
                LEFT JOIN Section s ON se.SectionID = s.SectionID AND se.CourseID = s.CourseID
                WHERE s.SemesterName = %s
            """, (semester_name,))

            results = cursor.fetchall()
            academic_year_results.extend(results)

        return academic_year_results

    except Error as e:
        print("Invalid input or error:", e)
        return None




def get_course(cursor, course_id):
    try:
        cursor.execute("SELECT * FROM Course WHERE CourseID = %s", (course_id,))
        course_data = cursor.fetchone()
        if not course_data:
            return None

        return course_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_section(cursor, section_id, course_id):
    try:
        cursor.execute("SELECT * FROM Section WHERE SectionID = %s AND CourseID = %s", (section_id, course_id))
        section_data = cursor.fetchone()
        if not section_data:
            return None

        return section_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_learning_objective(cursor, objective_code):
    try:
        cursor.execute("SELECT * FROM LearningObjectives WHERE ObjectiveCode = %s", (objective_code,))
        objective_data = cursor.fetchone()
        return objective_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_sub_objective(cursor, sub_objective_code):
    try:
        cursor.execute("SELECT * FROM SubObjective WHERE SubObjectiveCode = %s", (sub_objective_code,))
        sub_objective_data = cursor.fetchone()
        return sub_objective_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_program_course(cursor, program_name):
    try:
        cursor.execute("SELECT * FROM ProgramCourse WHERE ProgramName = %s", (program_name,))
        program_course_data = cursor.fetchall()
        return program_course_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_program_objective(cursor, program_name):
    try:
        cursor.execute("SELECT * FROM ProgramObjective WHERE ProgramName = %s", (program_name,))
        program_objective_data = cursor.fetchall()
        return program_objective_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_course_eval(cursor, course_id, program_name):
    try:
        cursor.execute("SELECT * FROM CourseEval WHERE CourseID = %s AND ProgramName = %s", (course_id, program_name))
        course_eval_data = cursor.fetchall()
        return course_eval_data

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_section_eval(cursor, section_id, course_id, program_name):
    try:
        cursor.execute("SELECT * FROM SectionEval WHERE SectionID = %s AND CourseID = %s AND ProgramName = %s", (section_id, course_id, program_name))
        section_eval_data = cursor.fetchall()
        return section_eval_data

    except Error as e:
        print("Invalid input or error:", e)
        return None
