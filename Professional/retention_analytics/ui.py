import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import sys
import importlib.util
import traceback
from io import StringIO
import contextlib
import uuid
import logic  # Import the provided logic.py

# List of required modules
REQUIRED_MODULES = [
    ('win32com.client', 'pywin32'),
    ('pandas', 'pandas'),
    ('pandas.errors', 'pandas'),
    ('openpyxl', 'openpyxl'),
    ('scipy.stats', 'scipy')
]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Data Processor")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)

        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_rowconfigure(0, weight=1)

        # Left column: Buttons
        self.button_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame.grid(row=0, column=0, sticky="nsew")
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Buttons
        buttons = [
            ("Generate Snapshot", self.generate_snapshot),
            ("Generate CCS", self.generate_ccs),
            ("Compare Data", self.compare_data),
            ("View Analytics", self.view_analytics),
            ("Help", self.display_help)
        ]
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                font=("Arial", 12),
                padx=10,
                pady=5
            )
            btn.grid(row=i, column=0, pady=5, sticky="ew")

        # Right column: Terminal output
        self.terminal_frame = tk.Frame(self.root, padx=10, pady=10)
        self.terminal_frame.grid(row=0, column=1, sticky="nsew")
        self.terminal_frame.grid_rowconfigure(0, weight=1)
        self.terminal_frame.grid_columnconfigure(0, weight=1)

        self.terminal = scrolledtext.ScrolledText(
            self.terminal_frame,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="white",
            fg="black",
            state='disabled'
        )
        self.terminal.grid(row=0, column=0, sticky="nsew")

        # Redirect print statements to terminal
        self.stdout = StringIO()
        sys.stdout = self
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Check dependencies on startup
        self.check_dependencies()

    def write(self, text):
        """Redirect print statements to the terminal widget."""
        self.terminal.configure(state='normal')
        self.terminal.insert(tk.END, text)
        self.terminal.see(tk.END)
        self.terminal.configure(state='disabled')
        self.stdout.write(text)

    def flush(self):
        """Required for sys.stdout compatibility."""
        self.stdout.flush()

    def clear_terminal(self):
        """Clear all text in the terminal widget."""
        self.terminal.configure(state='normal')
        self.terminal.delete(1.0, tk.END)
        self.terminal.configure(state='disabled')

    def check_dependencies(self):
        """Check if required modules are installed."""
        missing = []
        for module, package in REQUIRED_MODULES:
            try:
                importlib.import_module(module)
            except ImportError:
                missing.append(package)

        if missing:
            missing_str = ", ".join(missing)
            response = messagebox.askyesno(
                "Missing Dependencies",
                f"The following required packages are not installed: {missing_str}\n"
                "Would you like to install them now?"
            )
            if response:
                self.install_dependencies(missing)
            else:
                self.root.destroy()
                sys.exit(1)

    def install_dependencies(self, packages):
        """Attempt to install missing packages using pip."""
        self.clear_terminal()
        for package in packages:
            try:
                self.write(f"Installing {package}...\n")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                self.write(f"Successfully installed {package}\n")
            except subprocess.CalledProcessError:
                self.write(f"Failed to install {package}. Please install it manually.\n")
                messagebox.showerror(
                    "Installation Failed",
                    f"Failed to install {package}. Please install it manually and restart the application."
                )
                self.root.destroy()
                sys.exit(1)

    def run_function(self, func):
        """Run a function from logic.py and capture its output."""
        try:
            with contextlib.redirect_stdout(self):
                func()
        except Exception as e:
            self.write(f"Error: {str(e)}\n")
            self.write(traceback.format_exc() + "\n")

    def generate_snapshot(self):
        self.clear_terminal()
        self.write("Starting Generate Snapshot...\n")
        self.run_function(logic.generate_snapshot)

    def generate_ccs(self):
        self.clear_terminal()
        self.write("Starting Generate CCS...\n")
        self.run_function(logic.generate_ccs)

    def compare_data(self):
        self.clear_terminal()
        self.write("Starting Compare Data...\n")
        self.run_function(logic.compare_data)

    def view_analytics(self):
        self.clear_terminal()
        self.write("Starting View Analytics...\n")
        self.run_function(logic.view_analytics)

    def display_help(self):
        self.clear_terminal()
        self.write("Displaying Help...\n")
        self.run_function(logic.display_help)

    def on_closing(self):
        """Restore sys.stdout and close the application."""
        sys.stdout = sys.__stdout__
        self.root.destroy()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
