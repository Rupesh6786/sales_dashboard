import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from logic.analysis import get_basic_stats
from logic.visualization import plot_trends

dashboard_frame = None

def create_dashboard(parent):
    global dashboard_frame
    dashboard_frame = tk.Frame(parent, bg="#ffffff")
    dashboard_frame.pack(fill="both", expand=True)

def update_dashboard(parent, data):
    global dashboard_frame
    for widget in dashboard_frame.winfo_children():
        widget.destroy()

    stats = get_basic_stats(data)
    stats_box = tk.Text(dashboard_frame, height=10, font=("Segoe UI", 10))
    stats_box.insert("1.0", stats)
    stats_box.config(state='disabled')
    stats_box.pack(fill='x', padx=20, pady=10)

    fig = plot_trends(data)
    if fig:
        canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=20, pady=10, fill='both', expand=True)
