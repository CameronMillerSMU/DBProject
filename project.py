import csv
import mysql.connector as sql
from mysql.connector import Error

tables = ["Program", "Department", "Faculty", "Course", "Section", 
          "LearningObjective", "SubObjective", "CourseEval",
          "SectionEval", "ProgramObjective", "ProgramCourse"]

def create_database(cursor, database_name):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_table(cursor, table_name):
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))",
            multi=True)
        cursor.execute("SELECT 1", multi=True)
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = sql.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_tables_from_file(cursor, filename, connection):
    '''Note: if schema does not inlcude "IF NOT EXISTS" error occurs
    if the table already exists in the database
    '''
    try:
        with open(filename,'r') as file:
            sql_script = file.read()
            
        for result in cursor.execute(sql_script, multi=True):
            pass
    except Error as e:
        print(f"The error '{e} occurred'")
    
    connection.commit()


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