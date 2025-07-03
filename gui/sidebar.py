import tkinter as tk

def create_sidebar(parent, callbacks):
    sidebar = tk.Frame(parent, bg='#2c3e50', width=200)
    sidebar.pack(side='left', fill='y')

    buttons = [
        ("Upload", callbacks['upload']),
        ("Overview", callbacks['overview']),
        ("Trends", callbacks['trends']),
        ("Graphs", callbacks['graphs']),
    ]

    for label, cmd in buttons:
        btn = tk.Button(sidebar, text=label, command=cmd, fg='white', bg='#34495e', relief='flat')
        btn.pack(fill='x', pady=5, padx=10)

    return sidebar
