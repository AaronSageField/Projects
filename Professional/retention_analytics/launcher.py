import sys
import subprocess
import importlib.util
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
from threading import Thread
from io import StringIO
import time

# List of required modules
REQUIRED_MODULES = [
    ('win32com.client', 'pywin32'),
    ('pandas', 'pandas'),
    ('openpyxl', 'openpyxl'),
    ('scipy.stats', 'scipy')
]

class LauncherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Data Processor - Launcher")
        self.root.geometry("600x400")
        self.root.minsize(400, 300)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)

        # Output area
        self.output_frame = tk.Frame(self.root, padx=10, pady=10)
        self.output_frame.grid(row=0, column=0, sticky="nsew")
        self.output_frame.grid_rowconfigure(0, weight=1)
        self.output_frame.grid_columnconfigure(0, weight=1)

        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            wrap=tk.WORD,
            font=("Courier", 10),
            bg="white",
            fg="black",
            state='disabled',
            height=15
        )
        self.output_text.grid(row=0, column=0, sticky="nsew")

        # Status label
        self.status_var = tk.StringVar(value="Initializing...")
        self.status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        self.status_label.grid(row=1, column=0, sticky="ew")

        # Redirect stdout to text widget
        self.stdout = StringIO()
        sys.stdout = self

        # Flags for thread control
        self.running = True
        self.gui_active = True

        # Start dependency check in a separate thread
        self.thread = Thread(target=self.run)
        self.thread.start()

        # Periodically check if thread is done
        self.root.after(100, self.check_thread)

    def write(self, text):
        """Redirect print statements to the output text widget."""
        if self.gui_active:
            self.root.after(0, self._update_text, text)

    def _update_text(self, text):
        """Update text widget safely."""
        if self.gui_active:
            self.output_text.configure(state='normal')
            self.output_text.insert(tk.END, text)
            self.output_text.see(tk.END)
            self.output_text.configure(state='disabled')
            self.stdout.write(text)

    def flush(self):
        """Required for sys.stdout compatibility."""
        self.stdout.flush()

    def update_status(self, message):
        """Update the status label."""
        if self.gui_active:
            self.root.after(0, self.status_var.set, message)

    def check_dependencies(self):
        """Check if required modules are installed."""
        self.write("Checking dependencies...\n")
        self.update_status("Checking dependencies...")
        missing = []
        for module, package in REQUIRED_MODULES:
            if not self.is_module_installed(module):
                missing.append(package)
        if missing:
            self.write(f"Missing packages: {', '.join(missing)}\n")
        else:
            self.write("All dependencies are already installed.\n")
        return missing

    def is_module_installed(self, module_name):
        """Check if a module is installed."""
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            return False

    def install_dependencies(self, packages):
        """Attempt to install missing packages using pip."""
        self.update_status("Installing missing packages...")
        self.write("Attempting to install missing packages...\n")
        for package in packages:
            self.write(f"Installing {package}...\n")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                self.write(f"Successfully installed {package}\n")
            except subprocess.CalledProcessError as e:
                self.write(f"Failed to install {package}: {str(e)}\n")
                self.update_status(f"Failed to install {package}")
                return False
        self.write("All dependencies installed successfully.\n")
        self.update_status("Dependencies installed")
        return True

    def launch_ui(self):
        """Launch the ui.py script."""
        self.update_status("Launching application...")
        self.write("All dependencies satisfied. Launching application...\n")
        try:
            ui_path = os.path.join(os.path.dirname(__file__), "ui.py")
            if not os.path.exists(ui_path):
                raise FileNotFoundError(f"ui.py not found at {ui_path}")
            # Run ui.py and capture output
            result = subprocess.run(
                [sys.executable, ui_path],
                check=True,
                capture_output=True,
                text=True
            )
            self.write(result.stdout)
            self.write(result.stderr)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            self.write(f"Failed to launch ui.py: {str(e)}\n")
            if isinstance(e, subprocess.CalledProcessError):
                self.write(f"stdout: {e.stdout}\n")
                self.write(f"stderr: {e.stderr}\n")
            self.update_status("Error launching application")
            self.running = False
            return False
        return True

    def run(self):
        """Main method to check dependencies and launch UI."""
        try:
            missing = self.check_dependencies()
            if missing:
                if not self.install_dependencies(missing):
                    self.write("Failed to install some dependencies. Please install them manually.\n")
                    self.update_status("Installation failed. Please install dependencies manually.")
                    self.running = False
                    return
            if self.running:
                self.launch_success = self.launch_ui()
        except Exception as e:
            self.write(f"Unexpected error: {str(e)}\n")
            self.update_status("Unexpected error occurred")
            self.running = False

    def check_thread(self):
        """Check if the worker thread has completed and close GUI if successful."""
        if not self.thread.is_alive() and self.running:
            if hasattr(self, 'launch_success') and self.launch_success:
                self.gui_active = False
                self.root.destroy()
            else:
                self.update_status("Error occurred. Check log for details.")
        if self.running:
            self.root.after(100, self.check_thread)

    def on_closing(self):
        """Handle window close event."""
        if self.running:
            response = messagebox.askyesno(
                "Confirm Exit",
                "Dependency checking is in progress. Are you sure you want to exit?"
            )
            if not response:
                return
        self.running = False
        self.gui_active = False
        self.root.destroy()
        sys.exit(0)

def main():
    root = tk.Tk()
    app = LauncherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()