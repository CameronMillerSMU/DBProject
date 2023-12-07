hehe 

# Data Entry Functions
**File Name:**  entry.py

**Frontend Functions**
Use the handle_[table_name]_entry() functions to enter data into database. The only exceptions are for the assigning functions which will have assign in front them. They return strings that either denote success or failure. Some have specific failures, some don't.

These functions check for issues with the user input. So, if there is anything we missed out on checking add it to those functions. 


The enter_[table_name]_data() functions return True or False based on if the data was successfully entered or not. 


Things to fix later:
* System creating objective code for LearningObjective table
* SemesterID autoincrement fix 


This is in no way, shape or form safe against SQL injections 


Demo Notes

* Cannot have two section id in different years/semesters
