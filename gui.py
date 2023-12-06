import tkinter as tk
from tkinter import ttk
# from queries import *  # Assuming you have your query functions in a 'queries' module
# from entry import *    # Assuming you have your entry functions in an 'entry' module

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
        self.action_dropdown.pack()

        self.action_button = tk.Button(master, text="Select", command=self.handle_selection)
        self.action_button.pack()

        self.value_label = tk.Label(master, text="Value Returned:")
        self.value_label.pack()

        self.value_returned = tk.Label(master, text="")
        self.value_returned.pack()

    def handle_selection(self):
        # Clear previously added widgets
        for widget in self.option_widgets.values():
            widget.destroy()

        self.value_returned.config(text="")  # Clear the value returned label

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
        # Clear previously added widgets except for the first dropdown
        for key, widget in self.option_widgets.items():
            if key != "option_dropdown":
                widget.destroy()

        if self.action_var.get() == "Query" and selected_option == "Department":
            self.show_department_query_form(selected_value)

        # Add more conditions for other combinations of action and selected option

    def show_department_query_form(self, selected_value):
        department_code_label = tk.Label(self.master, text=f"{selected_value} Code:")
        department_code_label.pack()

        department_code_entry = tk.Entry(self.master)
        department_code_entry.pack()

        execute_button = tk.Button(self.master, text="Execute", command=lambda: self.handle_department_query(selected_value, department_code_entry.get()))
        execute_button.pack()

        # Keep track of added widgets for clearing later
        self.option_widgets["department_code_label"] = department_code_label
        self.option_widgets["department_code_entry"] = department_code_entry
        self.option_widgets["execute_button"] = execute_button

    def handle_department_query(self, selected_value, department_code):
        # Implement the query logic here using the entered department code
        result = get_department(self.cursor, department_code)  # Assuming get_department is a function in your 'queries' module
        self.display_result(result)

    def display_result(self, result):
        if result is not None:
            self.value_returned.config(text=str(result))
        else:
            self.value_returned.config(text="No data found.")

if __name__ == "__main__":
    root = tk.Tk()

    gui = DatabaseGUI(root, None)
    root.mainloop()