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
        self.option_widgets = {}

        self.selection_label = tk.Label(master, text="Select Action:")
        self.selection_label.pack()

        self.action_var = tk.StringVar()
        self.action_var.set("Select Action")

        self.action_dropdown = ttk.Combobox(master, textvariable=self.action_var, values=["Entry", "Query"])
        self.action_dropdown.pack(pady=0)  # Set pady to 0

        self.action_button = tk.Button(master, text="Select", command=self.handle_selection)
        self.action_button.pack()

        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack()

    def handle_selection(self):
        selected_action = self.action_var.get()

        if selected_action == "Entry":
            self.show_entry_options()
        elif selected_action == "Query":
            self.show_query_options()

    def show_entry_options(self):
        entry_options = ["Course", "Section", "LearningObjective", "Department", "Faculty", "Program", "Evaluation", "Assign Course", "Assign Learning Objective"]
        self.show_options(entry_options)

    def show_query_options(self):
        query_options = ["Department", "Program", "Semester", "Academic Year"]
        self.show_options(query_options)

    def show_options(self, options):
        option_label = tk.Label(self.master, text="Select Option:")
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

    def handle_option(self, selected_option, selected_value):
        if self.action_var.get() == "Query" and selected_option == "Department":
            self.show_department_query_form(selected_value)

        # Add more conditions for other combinations of action and selected option

    def show_department_query_form(self, selected_value):
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

    def execute_department_query(self, department_code):
        department_data = get_department(self.cursor, department_code)

        if not department_data:
            result_text = "Department does not exist. Please check department code."
        else:
            department_id, department_name, department_code = department_data
            result_text = f"Department ID: {department_id}\nDepartment Name: {department_name}\nDepartment Code: {department_code}"

        # Display result in the Text widget
        self.result_text.delete(1.0, tk.END)  # Clear previous text
        self.result_text.insert(tk.END, result_text)


if __name__ == "__main__":
    """CHANGE THIS TO RUN"""
    dbConn = create_connection("localhost", "root", "123456", "progDB")
    print(dbConn)
    cursor = dbConn.cursor()
    print(cursor)
    create_database(cursor, "progDB")
    
    
    create_tables_from_file(cursor, "test_schema.sql", dbConn)



    root = tk.Tk()

    gui = DatabaseGUI(root, cursor)
    root.mainloop()
