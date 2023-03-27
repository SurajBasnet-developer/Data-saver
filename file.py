import os
import tkinter as tk

root = tk.Tk()
root.title("Data Entry App")

# Configure the label widget
label = tk.Label(root, text="Enter some data:")
label.configure(font=("Arial", 14))
label.pack()

# Configure the entry widget
entry = tk.Entry(root, width=50)
entry.configure(font=("Times New Roman", 12))
  # Set the height to 5
entry.pack()

def save_data():
    data = entry.get()

    if not os.path.exists("data.txt"):
        open("data.txt", "w").close()

    with open("data.txt", "a") as file:
        file.write(data + "\n")

    # Configure the label widget
    label.config(text="Data saved successfully!")
    label.configure(fg="green", font=("Arial", 14, "bold"))

# Configure the button widget
button = tk.Button(root, text="Save", command=save_data)
button.configure(font=("Arial", 12), bg="blue", fg="white")
button.pack()

root.mainloop()
