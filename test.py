from testAll import *
from queries import *

dbConn = create_connection("localhost", "root", "beepboop", "progDB")
cursor = dbConn.cursor()
create_database(cursor, "progDB")

clear_database(cursor, dbConn, tables)
create_tables_from_file(cursor, "test_schema.sql", dbConn)

# populate all tables with random data 
populate_all_tables(cursor, dbConn)

# print(get_department(cursor, "CS01"))
# print(get_faculty(cursor, "F001"))
# print(get_faculty(cursor, "F004"))
# print(get_program(cursor, "Biology Program"))
# print(get_course(cursor, "BO010001"))
# print(get_section(cursor, "3", "BO010001"))
# print(get_learning_objective(cursor, "LO001"))
# print(get_sub_objective(cursor, "LO001.1"))
# print(get_program_course(cursor, "Biology Program"))
# print(get_program_objective(cursor, "Biology Program"))
# print(get_course_eval(cursor, "BO010001", "Biology Program"))
# print(get_section_eval(cursor, "3", "BO010001", "Biology Program"))

print(handle_department_entry(cursor, dbConn, "ABCD", "ABCD Department")) # good
print(handle_faculty_entry(cursor, dbConn, "1111111", "Test Falc", "faltest@gmail.com", "ABCD", "Adjunct")) #good
print(handle_program_entry(cursor, dbConn, "Test 2 Program", "1111111", "ABCD")) # good
print(handle_faculty_entry(cursor, dbConn, "1111113", "Test Falc 3", "faltest3@gmail.com", "ABCD", "boop")) #fail
#handle_course_entry(cursor, dbConn, "CS1111", "Test Course", "hello this course is for dunces like you", "0000")
print(handle_course_entry(cursor, dbConn, "ABCD0001", "Learning Abc's", "learn something", "ABCD"))
print(handle_section_entry(cursor, dbConn, "ABCD0001", "Fall", 2023, "1111111", 20))
print(handle_learningObjective_entry(cursor, dbConn, "LO1", "here is the decription"))
print(handle_subObjective_entry(cursor, dbConn, "LO1", "here is the sub objective description"))
print(handle_courseProgram_assignment(cursor, dbConn, "ABCD0001", "Test 2 Program"))


