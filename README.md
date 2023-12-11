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
* add entry data to the return messages 


This is in no way, shape or form safe against SQL injections 


Demo Notes/To-Do

* Cannot have two section id in different years/semesters
* Entering results for a sectionEvaluation has no year, and the ids aren't unique,
    * proposed sol: add year, semester to Section eval table
    * issues: possibly duplicated data for no reason, should evaluations just go in section table?

Question: Should I change evaluation table or leave it????


Meeting Goals

- hour 1
    - make test/dummy data that aligns with our constraints
    - Test all of the entries and queries make sure everything works
    - finish up entry for section evaluation results
- hour 2 
    - finish presentation
    - split up presentation duties 
    - (individual/optional) make notes for presentation section 
- hour 3 
    - couple run throughs 
    - overflow time


## Final Report instructions 

Final report. You should upload your final report as a zip file by noon 12/12 (Tue). You final
report should contain:
* The source code for your program.
*  A written report that contains the following:
    * The database schema, with comments on what each table represents (you can use the CREATE TABLE statements to describe the schema)
    * A brief installation/user manual to instruct someone (assume he/she is a junior CS student, but hasn’t taken database yet) how to install and use the program
    * An implementation manual to describe the program. Describe the various functions/method/classes and what each of them do



Presentation 

Into


## Database Schema and Description 



# Installation and User Manual

## Installation 

## User Manual
