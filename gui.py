# import tkinter as tk
#
# def on_entry_button_click():
#     update_label("Entry Button clicked!")
#
# def on_query_button_click():
#     update_label("Query Button clicked!")
#
# def update_label(message):
#     entry_text = entry.get()
#     label.config(text=f"{message} Entered text: {entry_text}, Selected option: {var.get()}")
#
# def update_layout():
#     selected_option = var.get()
#
#     # Hide all widgets
#     entry_button.grid_forget()
#     query_button.grid_forget()
#     entry.grid_forget()
#
#     # Show widgets based on the selected option
#     if selected_option == "Department":
#         entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#         entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
#     elif selected_option == "Faculty":
#         query_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#     elif selected_option == "Program":
#         entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#         entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
#     elif selected_option == "Course":
#         query_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#         entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
#     elif selected_option == "Section":
#         entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#         query_button.grid(row=2, column=0, padx=5, pady=10, sticky="e")
#     elif selected_option == "Objectives":
#         entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#         query_button.grid(row=2, column=0, padx=5, pady=10, sticky="e")
#         entry.grid(row=3, column=0, padx=5, pady=10, sticky="e")
#
# if __name__ == "__main__":
#     # Create the main application window
#     app = tk.Tk()
#     app.title("DB Project")
#
#     # Create an unchangeable label at the top
#     unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 20), fg="blue")
#     unchangeable_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2, sticky="e")
#
#     # Create a label widget
#     label = tk.Label(app, text="Mode", font=("Times New Roman", 20), fg="black")
#     label.grid(row=1, column=0, padx=5, pady=10, sticky="e")
#
#     # Create the Entry button widget
#     entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
#     query_button = tk.Button(app, text="Query", command=on_query_button_click)
#
#     # Create a variable to store the selected option
#     var = tk.StringVar(app)
#
#     # Create a dropdown menu
#     options = ["Department", "Faculty", "Program", "Course", "Section", "Objectives"]
#     dropdown = tk.OptionMenu(app, var, *options, command=lambda x: update_layout())
#     dropdown.grid(row=1, column=1, padx=5, pady=10, sticky="e")
#
#     # Set a default option
#     var.set(options[0])
#
#     # Create a text input box
#     entry = tk.Entry(app)
#     entry.grid(row=2, column=1, padx=5, pady=10, sticky="e")
#
#     # Start the main event loop
#     app.mainloop()

import tkinter as tk

def on_entry_button_click():
    update_label("Entry Button clicked!")
    # Show entry mode buttons
    for button in entry_buttons:
        button.grid(sticky="e")
    # Hide query mode buttons
    for button in query_buttons:
        button.grid_forget()

def on_query_button_click():
    update_label("Query Button clicked!")
    # Show query mode buttons
    for button in query_buttons:
        button.grid(sticky="e")
    # Hide entry mode buttons
    for button in entry_buttons:
        button.grid_forget()

def update_label(message):
    label.config(text=message)

def update_layout():
    selected_option = var.get()

    # Hide all buttons and entry field
    for button in entry_buttons + query_buttons:
        button.grid_forget()
    entry.grid_forget()

    # Show relevant buttons and entry field based on the selected option
    if selected_option in ["Department", "Faculty", "Programs", "Courses", "Sections"]:
        # Entry mode
        for button in entry_buttons:
            button.grid(sticky="e")
        entry.grid(row=2, column=1, padx=5, pady=10, sticky="e")
    elif selected_option == "Learning objectives / sub-objectives":
        # Entry mode with additional button
        for button in entry_buttons:
            button.grid(sticky="e")
        on_entry_button_click()
    elif selected_option in ["department", "program", "semester and program", "academic year"]:
        # Query mode
        for button in query_buttons:
            button.grid(sticky="e")
    elif selected_option == "Objectives":
        on_query_button_click()

if __name__ == "__main__":
    # Create the main application window
    app = tk.Tk()
    app.title("DB Project")

    # Define buttons for Entry mode
    entry_buttons = [
        tk.Button(app, text="Department"),
        tk.Button(app, text="Faculty"),
        tk.Button(app, text="Programs"),
        tk.Button(app, text="Courses"),
        tk.Button(app, text="Sections"),
        tk.Button(app, text="Learning objectives / sub-objectives"),
    ]

    # Define buttons for Query mode
    query_buttons = [
        tk.Button(app, text="department"),
        tk.Button(app, text="program"),
        tk.Button(app, text="semester and program"),
        tk.Button(app, text="academic year"),
    ]

    # Create an unchangeable label at the top
    unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 20), fg="blue")
    unchangeable_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2, sticky="e")

    # Create a label widget for messages
    label = tk.Label(app, text="", font=("Times New Roman", 16), fg="black", anchor=tk.SE)
    label.grid(row=3, column=1, padx=5, pady=10, sticky="e")

    # Create the Entry button widget
    entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
    query_button = tk.Button(app, text="Query", command=on_query_button_click)

    # Create a variable to store the selected option
    var = tk.StringVar(app)

    # Create a dropdown menu
    options = [
        "Department", "Faculty", "Programs", "Courses", "Sections",
        "Learning objectives / sub-objectives", "department",
        "program", "semester and program", "academic year",
    ]
    dropdown = tk.OptionMenu(app, var, *options, command=lambda x: update_layout())
    dropdown.grid(row=1, column=1, padx=5, pady=10, sticky="e")

    # Set a default option
    var.set(options[0])

    # Create a text input box
    entry = tk.Entry(app)

    # Start the main event loop
    app.mainloop()
import tkinter as tk

def on_entry_button_click():
    update_label("Entry Button clicked!")
    # Show entry mode buttons
    for button in entry_buttons:
        button.grid(sticky="e")
    # Hide query mode buttons
    for button in query_buttons:
        button.grid_forget()

def on_query_button_click():
    update_label("Query Button clicked!")
    # Show query mode buttons
    for button in query_buttons:
        button.grid(sticky="e")
    # Hide entry mode buttons
    for button in entry_buttons:
        button.grid_forget()

def update_label(message):
    label.config(text=message)

def update_layout():
    selected_option = var.get()

    # Hide all buttons and entry field
    for button in entry_buttons + query_buttons:
        button.grid_forget()
    entry.grid_forget()

    # Show relevant buttons and entry field based on the selected option
    if selected_option in ["Department", "Faculty", "Programs", "Courses", "Sections"]:
        # Entry mode
        for button in entry_buttons:
            button.grid(sticky="e")
        entry.grid(row=2, column=1, padx=5, pady=10, sticky="e")
    elif selected_option == "Learning objectives / sub-objectives":
        # Entry mode with additional button
        for button in entry_buttons:
            button.grid(sticky="e")
        on_entry_button_click()
    elif selected_option in ["department", "program", "semester and program", "academic year"]:
        # Query mode
        for button in query_buttons:
            button.grid(sticky="e")
    elif selected_option == "Objectives":
        on_query_button_click()

if __name__ == "__main__":
    # Create the main application window
    app = tk.Tk()
    app.title("DB Project")

    # Define buttons for Entry mode
    entry_buttons = [
        tk.Button(app, text="Department"),
        tk.Button(app, text="Faculty"),
        tk.Button(app, text="Programs"),
        tk.Button(app, text="Courses"),
        tk.Button(app, text="Sections"),
        tk.Button(app, text="Learning objectives / sub-objectives"),
    ]

    # Define buttons for Query mode
    query_buttons = [
        tk.Button(app, text="department"),
        tk.Button(app, text="program"),
        tk.Button(app, text="semester and program"),
        tk.Button(app, text="academic year"),
    ]

    # Create an unchangeable label at the top
    unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 20), fg="blue")
    unchangeable_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2, sticky="e")

    # Create a label widget for messages
    label = tk.Label(app, text="", font=("Times New Roman", 16), fg="black", anchor=tk.SE)
    label.grid(row=3, column=1, padx=5, pady=10, sticky="e")

    # Create the Entry button widget
    entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
    query_button = tk.Button(app, text="Query", command=on_query_button_click)

    # Create a variable to store the selected option
    var = tk.StringVar(app)

    # Create a dropdown menu
    options = [
        "Department", "Faculty", "Programs", "Courses", "Sections",
        "Learning objectives / sub-objectives", "department",
        "program", "semester and program", "academic year",
    ]
    dropdown = tk.OptionMenu(app, var, *options, command=lambda x: update_layout())
    dropdown.grid(row=1, column=1, padx=5, pady=10, sticky="e")

    # Set a default option
    var.set(options[0])

    # Create a text input box
    entry = tk.Entry(app)

    # Start the main event loop
    app.mainloop()
