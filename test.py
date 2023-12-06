from entry import *
from queries import *

dbConn = create_connection("localhost", "root", "beepboop", "progDB")
cursor = dbConn.cursor()
create_database(cursor, "progDB")

clear_database(cursor, dbConn, tables)
create_tables_from_file(cursor, "test_schema.sql", dbConn)

# populate all tables with random data 
populate_all_tables(cursor, dbConn)

print(get_department(cursor, "CS01"))
print(get_faculty(cursor, "F001"))
print(get_faculty(cursor, "F004"))
print(get_program(cursor, "Biology Program"))
print(get_course(cursor, "BO010001"))
print(get_section(cursor, "3", "BO010001"))
print(get_learning_objective(cursor, "LO001"))
print(get_sub_objective(cursor, "LO001.1"))
print(get_program_course(cursor, "Biology Program"))
print(get_program_objective(cursor, "Biology Program"))
print(get_course_eval(cursor, "BO010001", "Biology Program"))
print(get_section_eval(cursor, "3", "BO010001", "Biology Program"))





print(get_section_eval(cursor, "1", "BO010001", "Biology Program"))