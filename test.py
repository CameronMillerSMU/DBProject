from entry import *
from queries import *

dbConn = create_connection("localhost", "root", "beepboop", "progDB")
cursor = dbConn.cursor()
create_database(cursor, "progDB")

clear_database(cursor, dbConn, tables)
create_tables_from_file(cursor, "test_schema.sql", dbConn)

# populate all tables with random data 
populate_all_tables(cursor, dbConn)

get_department(cursor, "Computer Science")