import tkinter as tk
from services.report_generator import ReportGenerator

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FinSecure Dashboard")
        self.root.geometry("800x600")
        self.report = ReportGenerator()

    def run(self):
        tk.Label(self.root, text="FinSecure Management Dashboard", font=("Arial", 18, "bold")).pack(pady=10)
        metrics_frame = tk.Frame(self.root)
        metrics_frame.pack(pady=10)
        report_data = self.report.generate_summary()
        for i, line in enumerate(report_data):
            tk.Label(metrics_frame, text=line, font=("Arial", 13)).grid(row=i, column=0, sticky='w', padx=20, pady=2)
        self.root.mainloop()