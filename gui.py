import tkinter as tk
from tkinter import ttk
from queries import *
from entry import *
from testAll import *

class DatabaseGUI:
    def __init__(self, master, cursor):
        self.master = master
        self.master.title("Database GUI")
        self.cursor = cursor
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
        entry_options = ["Program", "Department", "Faculty", "Course", "Section", "LearningObjective", "Evaluation", "Assign Course", "Assign Learning Objective"]
        self.action_var.set("Entry")
        self.show_options(entry_options)

    def show_query_options(self):
        query_options = ["Department", "Program", "Semester", "Academic Year"]
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
        # Queries
        if self.action_var.get() == "Query" and selected_option == "Program":
            self.show_program_query_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Department":
            self.show_department_query_form(selected_value)
        elif self.action_var.get() == "Entry" and selected_option == "Faculty":
            self.show_faculty_entry_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Semester":
            self.show_semester_query_form(selected_value)
        elif self.action_var.get() == "Query" and selected_option == "Academic Year":
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
        elif self.action_var.get() == "Entry" and selected_option == "LearningObjective":
            self.show_learning_objective_entry_form(selected_value)


    def show_department_query_form(self, selected_value):
        self.destroy_option_widgets()

        department_code_label = tk.Label(self.master, text=f"{selected_value} Code:")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_department_query(department_code_entry.get()))
        execute_button.pack()

        # Keep track of added widgets for clearing later
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button

    def show_program_query_form(self, selected_value):
        self.destroy_option_widgets()

        program_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        program_name_label.pack()

        program_name_entry = tk.Entry(self.master)
        program_name_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_program_query(program_name_entry.get()))
        execute_button.pack()

        self.option_widgets["program_name_label"] = program_name_label
        self.option_widgets["program_name_entry"] = program_name_entry
        self.option_widgets["execute_button"] = execute_button

    def show_semester_query_form(self, selected_value):
        self.destroy_option_widgets()

        semester_label = tk.Label(self.master, text=f"{selected_value} Name:")
        semester_label.pack()

        semester_entry = tk.Entry(self.master)
        semester_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_semester_query(semester_entry.get()))
        execute_button.pack()

        self.option_widgets["semester_label"] = semester_label
        self.option_widgets["semester_entry"] = semester_entry
        self.option_widgets["execute_button"] = execute_button

    def show_academic_year_query_form(self, selected_value):
        self.destroy_option_widgets()

        academic_year_label = tk.Label(self.master, text=f"{selected_value} Name:")
        academic_year_label.pack()

        academic_year_entry = tk.Entry(self.master)
        academic_year_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_academic_year_query(academic_year_entry.get()))
        execute_button.pack()

        self.option_widgets["academic_year_label"] = academic_year_label
        self.option_widgets["academic_year_entry"] = academic_year_entry
        self.option_widgets["execute_button"] = execute_button

    def show_program_entry_form(self, selected_value):
        self.destroy_option_widgets()

        program_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        program_name_label.pack()

        program_name_entry = tk.Entry(self.master)
        program_name_entry.pack()

        program_coordinator_label = tk.Label(self.master, text=f"{selected_value} Coordinator ID:")
        program_coordinator_label.pack()

        program_coordinator_entry = tk.Entry(self.master)
        program_coordinator_entry.pack()

        department_code_label = tk.Label(self.master, text="Department Code:")
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

        department_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        department_name_label.pack()

        department_name_entry = tk.Entry(self.master)
        department_name_entry.pack()

        department_code_label = tk.Label(self.master, text=f"{selected_value} Code:")
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

        faculty_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        faculty_name_label.pack()

        faculty_name_entry = tk.Entry(self.master)
        faculty_name_entry.pack()

        faculty_id_label = tk.Label(self.master, text=f"{selected_value} ID:")
        faculty_id_label.pack()

        faculty_id_entry = tk.Entry(self.master)
        faculty_id_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_faculty_entry(faculty_name_entry.get(), faculty_id_entry.get()))
        execute_button.pack()

        self.option_widgets["faculty_name_label"] = faculty_name_label
        self.option_widgets["faculty_name_entry"] = faculty_name_entry
        self.option_widgets["faculty_id_label"] = faculty_id_label
        self.option_widgets["faculty_id_entry"] = faculty_id_entry
        self.option_widgets["execute_button"] = execute_button

    def show_course_entry_form(self, selected_value):
        self.destroy_option_widgets()

        course_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        course_name_label.pack()

        course_name_entry = tk.Entry(self.master)
        course_name_entry.pack()

        course_id_label = tk.Label(self.master, text=f"{selected_value} ID:")
        course_id_label.pack()

        course_id_entry = tk.Entry(self.master)
        course_id_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_course_entry(course_name_entry.get(), course_id_entry.get()))
        execute_button.pack()

        self.option_widgets["course_name_label"] = course_name_label
        self.option_widgets["course_name_entry"] = course_name_entry
        self.option_widgets["course_id_label"] = course_id_label
        self.option_widgets["course_id_entry"] = course_id_entry
        self.option_widgets["execute_button"] = execute_button

    def show_section_entry_form(self, selected_value):
        self.destroy_option_widgets()

        section_id_label = tk.Label(self.master, text=f"{selected_value} ID:")
        section_id_label.pack()

        section_id_entry = tk.Entry(self.master)
        section_id_entry.pack()

        course_id_label = tk.Label(self.master, text=f"{selected_value} Course ID:")
        course_id_label.pack()

        course_id_entry = tk.Entry(self.master)
        course_id_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_section_entry(section_id_entry.get(), course_id_entry.get()))
        execute_button.pack()

        self.option_widgets["section_id_label"] = section_id_label
        self.option_widgets["section_id_entry"] = section_id_entry
        self.option_widgets["course_id_label"] = course_id_label
        self.option_widgets["course_id_entry"] = course_id_entry
        self.option_widgets["execute_button"] = execute_button

    def show_learning_objective_entry_form(self, selected_value):
        self.destroy_option_widgets()

        objective_name_label = tk.Label(self.master, text=f"{selected_value} Name:")
        objective_name_label.pack()

        objective_name_entry = tk.Entry(self.master)
        objective_name_entry.pack()

        objective_code_label = tk.Label(self.master, text=f"{selected_value} Code:")
        objective_code_label.pack()

        objective_code_entry = tk.Entry(self.master)
        objective_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.execute_learning_objective_entry(objective_name_entry.get(), objective_code_entry.get()))
        execute_button.pack()

        self.option_widgets["objective_name_label"] = objective_name_label
        self.option_widgets["objective_name_entry"] = objective_name_entry
        self.option_widgets["objective_code_label"] = objective_code_label
        self.option_widgets["objective_code_entry"] = objective_code_entry
        self.option_widgets["execute_button"] = execute_button

    def execute_department_query(self, department_code):
        department_data = get_department(self.cursor, department_code)

        if not department_data:
            result_text = "Department does not exist. Please check department code."
        else:
            department_id, department_name, department_code = department_data
            result_text = f"Department ID: {department_id}\nDepartment Name: {department_name}\nDepartment Code: {department_code}"

        # Display result in the console (you can customize this as needed)
        print(result_text)


if __name__ == "__main__":
    root = tk.Tk()

    gui = DatabaseGUI(root, None)
    root.mainloop()
