import tkinter as tk

def on_entry_button_click():
    update_label("Entry Button clicked!")
    show_dropdown(1)

def on_query_button_click():
    update_label("Query Button clicked!")
    show_dropdown(2)

def update_label(message):
    entry_text = entry.get()
    label.config(text=f"{message} Entered text: {entry_text}, Selected option: {var.get()}, Selected dropdown: {dropdown_var.get()}")

def update_layout():
    selected_option = var.get()

    # Hide all widgets
    entry_button.grid_forget()
    query_button.grid_forget()
    entry.grid_forget()
    entry_dropdown.grid_forget()
    query_dropdown.grid_forget()

    # Show widgets based on the selected option
    if selected_option == "Department":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
    elif selected_option == "Faculty":
        query_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
    elif selected_option == "Program":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
    elif selected_option == "Course":
        query_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
    elif selected_option == "Section":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        query_button.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
    elif selected_option == "Objectives":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")
        query_button.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
        entry.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

def show_dropdown(selected_button):
    if selected_button == 1:
        entry_dropdown.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
        query_dropdown.grid_forget()
    elif selected_button == 2:
        query_dropdown.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
        entry_dropdown.grid_forget()

if __name__ == "__main__":
    # Create the main application window
    app = tk.Tk()
    app.title("DB Project")

    # Configure column and row weights to make the app flexible
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(1, weight=1)
    app.rowconfigure(2, weight=1)
    app.rowconfigure(3, weight=1)
    app.rowconfigure(4, weight=1)

    # Create an unchangeable label at the top
    unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 20), fg="blue")
    unchangeable_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2, sticky="ew")
    unchangeable_label.place(anchor="nw")

    # Create the Entry button widget
    entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
    entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

    # Create the Query button widget
    query_button = tk.Button(app, text="Query", command=on_query_button_click)
    query_button.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

    # Create a label widget at the bottom right
    label = tk.Label(app, text="Mode", font=("Times New Roman", 11), fg="Black")
    label.grid(row=4, column=1, padx=5, pady=10, sticky="sew")  # Updated sticky="sew" for bottom right

    # Create a variable to store the selected option
    var = tk.StringVar(app)

    # Create a text input box
    entry = tk.Entry(app)
    entry.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

    # Create a variable to store the selected dropdown option
    dropdown_var = tk.StringVar(app)

    # Create a dropdown menu for the Entry button
    entry_options = ["Department", "Faculty", "Program", "Course", "Section", "Objectives"]
    entry_dropdown = tk.OptionMenu(app, dropdown_var, *entry_options)
    entry_dropdown.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

    # Create a dropdown menu for the Query button
    query_options = ["Department", "Program", "Semester & Program", "Academic Year"]
    query_dropdown = tk.OptionMenu(app, dropdown_var, *query_options)

    # Start the main event loop
    app.mainloop()
