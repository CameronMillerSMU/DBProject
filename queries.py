import mysql.connector as sql
from mysql.connector import Error
import re

# Queries
def get_department_faculty(cursor, department_code):
    try:
        cursor.execute('''
            SELECT f.FacultyID, f.FacultyName, f.FacultyRank, p.ProgramName
            FROM Faculty f
            LEFT JOIN Program p ON f.FacultyID = p.ProgramCoordinatorID
            WHERE f.DepartmentCode = %s''', (department_code,))
    
        department_faculty = cursor.fetchall()
        if not department_faculty:
            return None

        return department_faculty

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_department_program(cursor, department_code):
    try:
        cursor.execute("""
            SELECT d.*, ProgramName
            FROM Program p, Department d
            WHERE p.DepartmentCode = d.DepartmentCode
            AND p.DepartmentCode = %s """, (department_code,))

        department_program = cursor.fetchall()
        if not department_program:
            return None

        return department_program

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_all_faculty(cursor):
    try:
        cursor.execute("SELECT * FROM Faculty")
        all_faculty = cursor.fetchall()
        if all_faculty is not None:
            return "\n".join(map(str, all_faculty))
        else:
            return "There are no faculty"
    except Error as e:
        print("Invalid input or error: ", e)
        return "Could not retrieve all faculty"

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

"""
    Goal: 
        1) return all courses in this program along with the sub(objectives) associated with it
        2) return all of the objectives for a given program 

"""
def get_program(cursor, program_name):
    courses = get_all_courses(cursor, program_name)

    objectives = get_objs_by_prog(cursor, program_name)

    return courses, objectives 
"""
    Returns all courses and their corresponding objectives given a program nam
"""
def get_all_courses(cursor, prog_name):
    try:
        command = "SELECT se.courseID, c.courseTitle, se.ObjectiveCode, so.SubObjectiveCode, s.CourseYear \
        FROM courseEval se, learningobjective lo, subobjective so, course c, section s \
        WHERE se.ObjectiveCode = lo.ObjectiveCode \
        AND  se.courseID = c.courseID \
        AND s.CourseID = se.CourseID \
        AND s.CourseID = c.CourseID \
        AND lo.ObjectiveCode = so.ObjectiveCode \
        AND se.ObjectiveCode = so.ObjectiveCode \
        AND se.programName = '%s'" % (prog_name)
        cursor.execute(command)

        all_prog_course = cursor.fetchall()

        if all_prog_course is not None:
            return all_prog_course
        else:
            return "No courses for this program"

    except Error as e:
        print("Invalid input or error:", e)
        return None

"""
    Returns all objectives assigned to a certain program
"""
def get_objs_by_prog(cursor, prog_name):
    try:
        command = "SELECT DISTINCT lo.ObjectiveCode, lo.ObjectiveDescription \
        FROM courseeval, learningobjective lo \
        WHERE courseeval.ObjectiveCode = lo.ObjectiveCode \
        AND ProgramName = '%s'" % (prog_name)
        cursor.execute(command)

        objectives = cursor.fetchall()

        if objectives is not None:
            return objectives
        else:
            return "No objectives for this program"

    except Error as e:
        print("Invalid input or error:", e)
        return None

def get_section_eval_results(cursor, semester_name, program_name):
    try:
        cursor.execute("""
        SELECT s.SectionID, s.CourseID, se.ProgramName, se.ObjectiveCode, se.EvalType, se.StudentsMetObj
        FROM Section s
        LEFT JOIN SectionEval se ON s.SectionID = se.SectionID AND s.CourseID = se.CourseID
        WHERE s.SemesterName = %s AND se.ProgramName = %s;
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
            SELECT se.ObjectiveCode, so.SubObjectiveCode, c.CourseID, s.SectionID, s.SemesterName, s.CourseYear, se.EvalType, se.StudentsMetObj
            FROM  SectionEval se
            LEFT JOIN SubObjective so ON se.ObjectiveCode = so.ObjectiveCode
            LEFT JOIN CourseEval ce ON se.CourseID = ce.CourseID AND ce.ProgramName = se.ProgramName AND ce.ObjectiveCode = se.ObjectiveCode
            LEFT JOIN Section s ON se.SectionID = s.SectionID AND se.CourseID = s.CourseID
            LEFT JOIN Course c ON s.CourseID = c.CourseID
            WHERE s.semesterName = %s AND s.CourseYear = %s
            """, (semester, year,))

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
