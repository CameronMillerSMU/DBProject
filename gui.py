import tkinter as tk

def on_entry_button_click():
    update_label("Entry Button clicked!")

def on_query_button_click():
    update_label("Query Button clicked!")

def update_label(message):
    entry_text = entry.get()
    label.config(text=f"{message} Entered text: {entry_text}, Selected option: {var.get()}")

def update_layout():
    selected_option = var.get()

    # Hide all widgets
    entry_button.grid_forget()
    query_button.grid_forget()
    entry.grid_forget()

    # Show widgets based on the selected option
    if selected_option == "Department":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    elif selected_option == "Faculty":
        query_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
    elif selected_option == "Program":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    elif selected_option == "Course":
        query_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        entry.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    elif selected_option == "Section":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        query_button.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    elif selected_option == "Objectives":
        entry_button.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        query_button.grid(row=2, column=0, padx=5, pady=10, sticky="e")
        entry.grid(row=3, column=0, padx=5, pady=10, sticky="e")

# Create the main application window
app = tk.Tk()
app.title("DB Project")

# Create an unchangeable label at the top
unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 20), fg="blue")
unchangeable_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2, sticky="e")

# Create a label widget
label = tk.Label(app, text="Mode", font=("Times New Roman", 20), fg="black")
label.grid(row=1, column=0, padx=5, pady=10, sticky="e")

# Create the Entry button widget
entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
query_button = tk.Button(app, text="Query", command=on_query_button_click)

# Create a variable to store the selected option
var = tk.StringVar(app)

# Create a dropdown menu
options = ["Department", "Faculty", "Program", "Course", "Section", "Objectives"]
dropdown = tk.OptionMenu(app, var, *options, command=lambda x: update_layout())
dropdown.grid(row=1, column=1, padx=5, pady=10, sticky="e")

# Set a default option
var.set(options[0])

# Create a text input box
entry = tk.Entry(app)
entry.grid(row=2, column=1, padx=5, pady=10, sticky="e")

# Start the main event loop
app.mainloop()
