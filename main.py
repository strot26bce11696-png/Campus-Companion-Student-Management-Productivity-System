import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()

root.title("Campus Companion")
root.geometry("800x500")

# Heading
title = tk.Label(
    root,
    text="Campus Companion",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="Your Personal College Management System",
    font=("Arial", 14)
)
subtitle.pack()

# Test button
def welcome():
    messagebox.showinfo(
        "Campus Companion",
        "Welcome to Campus Companion!"
    )

button = tk.Button(
    root,
    text="Get Started",
    command=welcome,
    font=("Arial", 14)
)
button.pack(pady=40)

# Start application
root.mainloop()