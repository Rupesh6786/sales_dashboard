import tkinter as tk

def create_header(parent):
    header = tk.Frame(parent, bg='#34495e', height=50)
    header.pack(side='top', fill='x')
    label = tk.Label(header, text="Sales Dashboard", font=("Helvetica", 16), fg='white', bg='#34495e')
    label.pack(pady=10)
    return header
