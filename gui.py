import tkinter as tk
from tkinter import ttk

class DatabaseGUI:
    def __init__(self, master, cursor):
        self.master = master
        self.master.title("Database GUI")
        self.cursor = cursor
        self.option_widgets = []

        self.selection_label = tk.Label(master, text="Select Action:")
        self.selection_label.pack()

        self.action_var = tk.StringVar()
        self.action_var.set("Select Action")

        self.action_dropdown = ttk.Combobox(master, textvariable=self.action_var, values=["Entry", "Query"])
        self.action_dropdown.pack()

        self.action_button = tk.Button(master, text="Select", command=self.handle_selection)
        self.action_button.pack()

    def handle_selection(self):
        # Clear previously added dropdown and widgets
        for widget in self.option_widgets:
            widget.destroy()
        self.option_widgets = []

        selected_action = self.action_var.get()

        if selected_action == "Entry":
            self.show_entry_options()
        elif selected_action == "Query":
            self.show_query_options()

    def show_entry_options(self):
        entry_options = ["Course", "Section", "LearningObjective"]
        self.show_options(entry_options)

    def show_query_options(self):
        query_options = ["Department", "Faculty", "Program", "Course", "Section", "LearningObjective"]
        self.show_options(query_options)

    def show_options(self, options):
        option_label = tk.Label(self.master, text="Select Option:")
        option_label.pack()

        option_var = tk.StringVar()
        option_var.set("Select Option")

        option_dropdown = ttk.Combobox(self.master, textvariable=option_var, values=options)
        option_dropdown.pack()

        option_button = tk.Button(self.master, text="Submit", command=lambda: self.handle_option(option_var.get()))
        option_button.pack()

        # Keep track of added widgets for clearing later
        self.option_widgets.extend([option_label, option_dropdown, option_button])

    def handle_option(self, selected_option):
        # Do something with the selected option (e.g., show data entry form or query results)
        print(f"Selected Option: {selected_option}")

if __name__ == "__main__":
    root = tk.Tk()

    gui = DatabaseGUI(root, None)
    root.mainloop()
