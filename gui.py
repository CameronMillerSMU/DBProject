import tkinter as tk

def on_entry_button_click():
    label.config(text="Entry Button clicked!")
    entry_text = entry.get()
    label.config(text=f"Entry Button clicked! Entered text: {entry_text}, Selected option: {var.get()}")

def on_query_button_click():
    label.config(text="Query Button clicked!")
    entry_text = entry.get()
    label.config(text=f"Query Button clicked! Entered text: {entry_text}, Selected option: {var.get()}")

# Create the main application window
app = tk.Tk()
app.title("DB Project")

# Create an unchangeable label at the top
unchangeable_label = tk.Label(app, text="Course Catalog Database", font=("Times New Roman", 50), fg="blue")
unchangeable_label.pack()

# Create a label widget
label = tk.Label(app, text="Mode", font=("Times New Roman", 20), fg="black")
label.pack()  # Pack the label into the window

# Create the Entry button widget
entry_button = tk.Button(app, text="Entry", command=on_entry_button_click)
entry_button.pack(padx=5, pady=10, side=tk.LEFT)  # Pack the button into the window

# Create the Query button widget
query_button = tk.Button(app, text="Query", command=on_query_button_click)
query_button.pack(padx=5, pady=20, side=tk.LEFT)  # Pack the button into the window

# Create a variable to store the selected option
var = tk.StringVar(app)

# Create a dropdown menu
options = ["Department", "Faculty", "Program", "Course", "Section", "Objectives"]
dropdown = tk.OptionMenu(app, var, *options)
dropdown.pack()

# Set a default option
var.set(options[0])

# Create a text input box
entry = tk.Entry(app)
entry.pack()

# Start the main event loop
app.mainloop()
