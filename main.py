# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from gui.header import create_header
from gui.sidebar import create_sidebar
from gui.dashboard import create_dashboard, update_dashboard
from logic.data_loader import load_dataset
from logic.analysis import get_basic_stats
from logic.visualization import plot_trends, plot_graphs

class SalesDashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sales Analysis Dashboard")
        self.geometry("1200x700")
        self.configure(bg="#ecf0f1")
        self.resizable(False, False)

        self.data = None  # Loaded dataset

        create_header(self)
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)

        callbacks = {
            'upload': self.upload_data,
            'overview': self.show_overview,
            'trends': self.show_trends,
            'graphs': self.show_graphs
        }

        create_sidebar(self.main_frame, callbacks)
        self.content_area = tk.Frame(self.main_frame, bg='white')
        self.content_area.pack(side='left', fill='both', expand=True)

        create_dashboard(self.content_area)

    def upload_data(self):
        file_path = filedialog.askopenfilename(
            title="Select a Sales Dataset",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        if not file_path:
            return

        try:
            self.data = load_dataset(file_path)
            messagebox.showinfo("Success", "Dataset uploaded successfully!")
            update_dashboard(self.content_area, self.data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset:\n{str(e)}")

    def show_dashboard(self):
        if self.data is None:
            messagebox.showwarning("No Data", "Please upload a dataset first.")
            return
        update_dashboard(self.content_area, self.data)

    def show_overview(self):
        if self.data is not None:
            stats = get_basic_stats(self.data)
            self.display_text(stats)
        else:
            messagebox.showerror("Error", "Please upload a dataset first.")

    def show_trends(self):
        if self.data is not None:
            try:
                plot_trends(self.data)
            except Exception as e:
                messagebox.showerror("Trend Error", str(e))
        else:
            messagebox.showerror("Error", "Please upload a dataset first.")

    def show_graphs(self):
        if self.data is not None:
            try:
                plot_graphs(self.data)
            except Exception as e:
                messagebox.showerror("Graph Error", str(e))
        else:
            messagebox.showerror("Error", "Please upload a dataset first.")

    def display_text(self, text):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        text_widget = tk.Text(self.content_area)
        text_widget.insert('1.0', text)
        text_widget.pack(fill='both', expand=True)

if __name__ == "__main__":
    app = SalesDashboardApp()
    app.mainloop()