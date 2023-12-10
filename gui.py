import tkinter as tk
from tkinter import ttk
from queries import *
from entry import *
from testAll import *

class DatabaseGUI:
    def __init__(self, master, cursor, connector):
        self.master = master
        self.master.title("Database GUI")
        self.cursor = cursor
        self.connector = connector
        self.option_widgets = {}  # Initialize option_widgets dictionary
        self.action_var = tk.StringVar()  # Initialize action_var

        self.main_menu()

    def main_menu(self):
        self.selection_label = tk.Label(self.master, text="Select Action:")
        self.selection_label.pack()

        entry_button = tk.Button(self.master, text="Entry", command=self.show_entry_options)
        entry_button.pack()

        query_button = tk.Button(self.master, text="Query", command=self.show_query_options)
        query_button.pack()

    def show_entry_options(self):
        # destroy the previous selected option label
        if hasattr(self, 'selected_option_label'):
            self.selected_option_label.destroy()

        entry_options = ["Program", "Department", "Faculty", "Course", "Section", "Learning Objective"]
        self.action_var.set("Entry")
        self.show_options(entry_options)

    def show_query_options(self):
        # destroy the previous selected option label
        if hasattr(self, 'selected_option_label'):
            self.selected_option_label.destroy()

        query_options = ["Department", "Program", "Semester Program Results", "Academic Year Program Results"]
        self.action_var.set("Query")
        self.show_options(query_options)

    def show_options(self, options):
        # destroy the previous widgets
        if hasattr(self, 'selection_label'):
            self.selection_label.destroy()
        self.destroy_option_widgets()

        # show "Select Option (Entry)" or "Select Option (Query)" depending on selected action
        option_label = tk.Label(self.master, text=f"Select Option ({self.action_var.get()})")
        option_label.pack()

        option_var = tk.StringVar()
        option_var.set("Select Option")

        option_dropdown = ttk.Combobox(self.master, textvariable=option_var, values=options)
        option_dropdown.pack()

        option_button = tk.Button(self.master, text="Submit", command=lambda: self.handle_option(option_var.get(), option_dropdown.get()))
        option_button.pack()

        # Keep track of added widgets for clearing later
        self.option_widgets["option_label"] = option_label
        self.option_widgets["option_dropdown"] = option_dropdown
        self.option_widgets["option_button"] = option_button

    def destroy_option_widgets(self):
        # destroy the previous widgets
        for widget in self.option_widgets.values():
            widget.destroy()

    def handle_option(self, selected_option, selected_value):
        # show the selected option above the form
        self.selected_option_label = tk.Label(self.master, text=f"Selected Option: {selected_option}")
        self.selected_option_label.pack()

        # Queries
        if self.action_var.get() == "Query" and selected_option == "Department":
            self.show_department_query_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Program":
            self.show_program_query_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Semester Program Results":
            self.show_semester_program_query_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Academic Year Program Results":
            self.show_academic_year_query_form(selected_value)

        # Entries
        elif self.action_var.get() == "Entry" and selected_option == "Program":
            self.show_program_entry_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Department":
            self.show_department_entry_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Faculty":
            self.show_faculty_entry_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Course":
            self.show_course_entry_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Section":
            self.show_section_entry_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Learning Objective":
            self.show_learning_objective_entry_form(selected_value)

    def show_program_entry_form(self, selected_value):
        self.destroy_option_widgets()

        program_name_label = tk.Label(self.master, text=f"{selected_value} Name (max 255 characters):")
        program_name_label.pack()

        program_name_entry = tk.Entry(self.master)
        program_name_entry.pack()

        program_coordinator_label = tk.Label(self.master, text=f"{selected_value} Coordinator ID (max 10 characters):")
        program_coordinator_label.pack()

        program_coordinator_entry = tk.Entry(self.master)
        program_coordinator_entry.pack()

        department_code_label = tk.Label(self.master, text="Department Code (max 4 alpha characters):")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_program_entry(program_name_entry.get(), program_coordinator_entry.get(), department_code_entry.get()))
        execute_button.pack()

        self.option_widgets["program_name_label"] = program_name_label
        self.option_widgets["program_name_entry"] = program_name_entry
        self.option_widgets["program_coordinator_label"] = program_coordinator_label
        self.option_widgets["program_coordinator_entry"] = program_coordinator_entry
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button

    def show_department_entry_form(self, selected_value):
        self.destroy_option_widgets()

        department_name_label = tk.Label(self.master, text=f"{selected_value} Name (max 255 characters):")
        department_name_label.pack()

        department_name_entry = tk.Entry(self.master)
        department_name_entry.pack()

        department_code_label = tk.Label(self.master, text=f"{selected_value} Code (max 4 alpha characters):")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_department_entry(department_name_entry.get(), department_code_entry.get()))
        execute_button.pack()

        self.option_widgets["department_name_label"] = department_name_label
        self.option_widgets["department_name_entry"] = department_name_entry
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button

    def show_faculty_entry_form(self, selected_value):
        self.destroy_option_widgets()

        faculty_name_label = tk.Label(self.master, text=f"{selected_value} Name (max 255 characters):")
        faculty_name_label.pack()

        faculty_name_entry = tk.Entry(self.master)
        faculty_name_entry.pack()

        faculty_email_label = tk.Label(self.master, text=f"{selected_value} Email (max 255 characters):")
        faculty_email_label.pack()

        faculty_email_entry = tk.Entry(self.master)
        faculty_email_entry.pack()

        department_code_label = tk.Label(self.master, text="Department Code (max 4 alpha characters):")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        faculty_rank_label = tk.Label(self.master, text="Faculty Rank (Full, Associate, Assistant, Adjunct):")
        faculty_rank_label.pack()

        faculty_rank_entry = tk.Entry(self.master)
        faculty_rank_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_faculty_entry(faculty_name_entry.get(), faculty_email_entry.get(), department_code_entry.get(), faculty_rank_entry.get()))
        execute_button.pack()

        self.option_widgets["faculty_name_label"] = faculty_name_label
        self.option_widgets["faculty_name_entry"] = faculty_name_entry
        self.option_widgets["faculty_email_label"] = faculty_email_label
        self.option_widgets["faculty_email_entry"] = faculty_email_entry
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["faculty_rank_label"] = faculty_rank_label
        self.option_widgets["faculty_rank_entry"] = faculty_rank_entry
        self.option_widgets["execute_button"] = execute_button

    def show_course_entry_form(self, selected_value):
        self.destroy_option_widgets()

        course_id_label = tk.Label(self.master, text=f"{selected_value} ID (max 8 characters):")
        course_id_label.pack()

        course_id_entry = tk.Entry(self.master)
        course_id_entry.pack()

        course_title_label = tk.Label(self.master, text=f"{selected_value} Title (max 255 characters):")
        course_title_label.pack()

        course_title_entry = tk.Entry(self.master)
        course_title_entry.pack()

        course_description_label = tk.Label(self.master, text=f"{selected_value} Description:")
        course_description_label.pack()

        course_description_entry = tk.Entry(self.master)
        course_description_entry.pack()

        department_code_label = tk.Label(self.master, text="Department Code (max 4 alpha characters):")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_course_entry(course_id_entry.get(), course_title_entry.get(), course_description_entry.get(), department_code_entry.get()))
        execute_button.pack()

        self.option_widgets["course_id_label"] = course_id_label
        self.option_widgets["course_id_entry"] = course_id_entry
        self.option_widgets["course_title_label"] = course_title_label
        self.option_widgets["course_title_entry"] = course_title_entry
        self.option_widgets["course_description_label"] = course_description_label
        self.option_widgets["course_description_entry"] = course_description_entry
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button
        
    def show_section_entry_form(self, selected_value):
        self.destroy_option_widgets()

        course_id_label = tk.Label(self.master, text=f"{selected_value} ID (max 8 characters):")
        course_id_label.pack()

        course_id_entry = tk.Entry(self.master)
        course_id_entry.pack()

        semester_label = tk.Label(self.master, text=f"{selected_value} Semester (Fall, Spring, Summer):")
        semester_label.pack()

        semester_entry = tk.Entry(self.master)
        semester_entry.pack()

        year_label = tk.Label(self.master, text=f"{selected_value} Year:")
        year_label.pack()

        year_entry = tk.Entry(self.master)
        year_entry.pack()

        faculty_id_label = tk.Label(self.master, text=f"{selected_value} Faculty ID (max 10 characters):")
        faculty_id_label.pack()

        faculty_id_entry = tk.Entry(self.master)
        faculty_id_entry.pack()

        students_enrolled_label = tk.Label(self.master, text=f"{selected_value} Students Enrolled:")
        students_enrolled_label.pack()

        students_enrolled_entry = tk.Entry(self.master)
        students_enrolled_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_section_entry(course_id_entry.get(), semester_entry.get(), year_entry.get(), faculty_id_entry.get(), students_enrolled_entry.get()))
        execute_button.pack()

        self.option_widgets["course_id_label"] = course_id_label
        self.option_widgets["course_id_entry"] = course_id_entry
        self.option_widgets["semester_label"] = semester_label
        self.option_widgets["semester_entry"] = semester_entry
        self.option_widgets["year_label"] = year_label
        self.option_widgets["year_entry"] = year_entry
        self.option_widgets["faculty_id_label"] = faculty_id_label
        self.option_widgets["faculty_id_entry"] = faculty_id_entry
        self.option_widgets["students_enrolled_label"] = students_enrolled_label
        self.option_widgets["students_enrolled_entry"] = students_enrolled_entry
        self.option_widgets["execute_button"] = execute_button

    def show_learning_objective_entry_form(self, selected_value):
        self.destroy_option_widgets()

        objective_code_label = tk.Label(self.master, text=f"{selected_value} Code (max 10 characters):")
        objective_code_label.pack()

        objective_code_entry = tk.Entry(self.master)
        objective_code_entry.pack()

        objective_description_label = tk.Label(self.master, text=f"{selected_value} Description:")
        objective_description_label.pack()

        objective_description_entry = tk.Entry(self.master)
        objective_description_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_learning_objective_entry(objective_code_entry.get(), objective_description_entry.get()))
        execute_button.pack()

        self.option_widgets["objective_code_label"] = objective_code_label
        self.option_widgets["objective_code_entry"] = objective_code_entry
        self.option_widgets["objective_description_label"] = objective_description_label
        self.option_widgets["objective_description_entry"] = objective_description_entry
        self.option_widgets["execute_button"] = execute_button


    def execute_program_entry(self, program_name, program_coordinator_id, department_code):
        result_text = handle_program_entry(self.cursor, self.connector, program_name, program_coordinator_id, department_code)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

    def execute_department_entry(self, department_name, department_code):
        result_text = handle_department_entry(self.cursor, self.connector, department_code, department_name)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

    def execute_faculty_entry(self, faculty_name, faculty_email, department_code, faculty_rank):
        result_text = handle_faculty_entry(self.cursor, self.connector, faculty_name, faculty_email, department_code, faculty_rank)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

    def execute_course_entry(self, course_id, course_title, course_description, department_code):
        result_text = handle_course_entry(self.cursor, self.connector, course_id, course_title, course_description, department_code)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

    def execute_section_entry(self, course_id, semester, year, faculty_id, students_enrolled):
        result_text = handle_section_entry(self.cursor, self.connector, course_id, semester, year, faculty_id, students_enrolled)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

    def execute_learning_objective_entry(self, objective_code, objective_description):
        result_text = handle_learningObjective_entry(self.cursor, self.connector, objective_code, objective_description)
        print(result_text)

        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()


    def show_program_query_form(self, selected_value):
        self.destroy_option_widgets()

        program_name_label = tk.Label(self.master, text=f"{selected_value} Name (max 255 characters):")
        program_name_label.pack()

        program_name_entry = tk.Entry(self.master)
        program_name_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_program_query(program_name_entry.get()))
        execute_button.pack()

        self.option_widgets["program_name_label"] = program_name_label
        self.option_widgets["program_name_entry"] = program_name_entry
        self.option_widgets["execute_button"] = execute_button

    def show_department_query_form(self, selected_value):
        self.destroy_option_widgets()

        department_code_label = tk.Label(self.master, text=f"{selected_value} Code (max 4 alpha characters):")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_department_query(department_code_entry.get()))
        execute_button.pack()

        # Keep track of added widgets for clearing later
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button

    def show_semester_program_query_form(self, selected_value):
        self.destroy_option_widgets()

        semester_name_label = tk.Label(self.master, text=f"{selected_value} Semester (Fall, Spring, Summer):")
        semester_name_label.pack()

        semester_name_entry = tk.Entry(self.master)
        semester_name_entry.pack()

        program_name_label = tk.Label(self.master, text=f"{selected_value} Program (max 255 characters):")
        program_name_label.pack()

        program_name_entry = tk.Entry(self.master)
        program_name_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_semester_program_query(semester_name_entry.get(), program_name_entry.get()))
        execute_button.pack()

        self.option_widgets["semester_name_label"] = semester_name_label
        self.option_widgets["semester_name_entry"] = semester_name_entry
        self.option_widgets["program_name_label"] = program_name_label
        self.option_widgets["program_name_entry"] = program_name_entry
        self.option_widgets["execute_button"] = execute_button


    def execute_program_query(self, program_name):
        program_data = get_program(self.cursor, program_name)

        if not program_data:
            result_text = "Program does not exist. Please check program name."
        else:
            program_name, program_coordinator_id, department_code = program_data
            #result_text = f"Program ID: {program_id}\nProgram Name: {program_name}\nProgram Coordinator ID: {program_coordinator_id}\nDepartment Code: {department_code}"
            result_text = f"Program Name: {program_name}\nProgram Coordinator ID: {program_coordinator_id}\nDepartment Code: {department_code}"
        print(result_text)

    def execute_department_query(self, department_code):
        department_data = get_department(self.cursor, department_code)

        if not department_data:
            result_text = "Department does not exist. Please check department code."
        else:
            department_id, department_name, department_code = department_data
            result_text = f"Department ID: {department_id}\nDepartment Name: {department_name}\nDepartment Code: {department_code}"
        print(result_text)

    def execute_semester_program_query(self, semester_name, program_name):
        program_data = get_section_eval_results(self.cursor, semester_name, program_name)

        if not program_data:
            result_text = "No results found. Please check semester name and program name."
        else:
            result_text = ""
            for section_id, course_id, program_name, objective_code, eval_type, students_met_obj in program_data:
                result_text += f"Section ID: {section_id}\nCourse ID: {course_id}\nProgram Name: {program_name}\nObjective Code: {objective_code}\nEvaluation Type: {eval_type}\nStudents Met Objective: {students_met_obj}\n\n"
        print(result_text)


if __name__ == "__main__":
    root = tk.Tk()

    """CHANGE THIS TO RUN"""
    dbConn = create_connection("localhost", "root", "123456", "progDB")
    cursor = dbConn.cursor()
    create_database(cursor, "progDB")
    clear_database(cursor, dbConn, tables)
    
    create_tables_from_file(cursor, "test_schema.sql", dbConn)
    
    populate_all_tables(cursor, dbConn)

    gui = DatabaseGUI(root, cursor, dbConn)
    root.mainloop()
