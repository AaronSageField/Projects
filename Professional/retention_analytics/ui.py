import os
import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
from io import StringIO
from business import (
    define_spreadsheets,
    generate_mbob_snapshot,
    consolidate_commission_statements,
    calculate_retention_rates,
    find_data_folder,
    find_snapshots_folder,
    find_reports_folder
)

class PrintRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)
        self.text_widget.update()

    def flush(self):
        pass

class BusinessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Management System")
        self.root_directory = os.getcwd()

        # Configure main window
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        # Button frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        self.button_frame.columnconfigure((0, 1, 2), weight=1)

        # Buttons
        ttk.Button(
            self.button_frame,
            text="Generate Snapshot",
            command=self.run_generate_snapshot
        ).grid(row=0, column=0, padx=5, sticky=(tk.W, tk.E))
        
        ttk.Button(
            self.button_frame,
            text="Generate CCS",
            command=self.run_consolidate_commission
        ).grid(row=0, column=1, padx=5, sticky=(tk.W, tk.E))
        
        ttk.Button(
            self.button_frame,
            text="Calc Retention Rates",
            command=self.run_calculate_retention
        ).grid(row=0, column=2, padx=5, sticky=(tk.W, tk.E))

        # Output window
        self.output_text = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            height=20,
            font=("Courier", 10)
        )
        self.output_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Redirect print statements
        sys.stdout = PrintRedirector(self.output_text)

        # Initialize folders after GUI setup
        self.initialize_folders()

    def initialize_folders(self):
        """Initialize folders and display creation messages in output window."""
        self.reports_folder = find_reports_folder(self.root_directory)
        self.snapshots_folder = find_snapshots_folder(self.root_directory)
        self.data_folder = find_data_folder(self.root_directory)

    def run_generate_snapshot(self):
        self.output_text.delete(1.0, tk.END)
        reports = define_spreadsheets(self.reports_folder)
        generate_mbob_snapshot(self.snapshots_folder, self.data_folder, reports)

    def run_consolidate_commission(self):
        self.output_text.delete(1.0, tk.END)
        consolidate_commission_statements()

    def run_calculate_retention(self):
        self.output_text.delete(1.0, tk.END)
        calculate_retention_rates(self.root_directory)

if __name__ == "__main__":
    root = tk.Tk()
    app = BusinessGUI(root)
    root.mainloop()
