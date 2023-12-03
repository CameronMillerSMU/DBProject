from project import *

db = create_connection("localhost", "root", "beepboop", "DBprog")
cursor = db.cursor()
create_database(cursor, "DBprog")

#todo: create the tables from file 
def execute_scripts_from_file(filename):
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()

    # get commands 
    sql_commands = sql_file.split(';')

    # execute comamnds in file
    for command in sql_commands:
        try:
            cursor.execute(command)
        except Error as e:
            print(f"The error '{e}' occurred")

execute_scripts_from_file("test_schema.sql")


 