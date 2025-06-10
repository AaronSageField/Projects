import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import business

class RedirectText: 
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, text)
        self.text_widget.configure(state='disabled')
        self.text_widget.see(tk.END)

    def flush(self):
        pass

class MBOSnapshotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MBOB Snapshot Generator")
        self.geometry("800x600")

        # Main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.TOP, pady=(0, 10))

        # Generate Snapshot Button
        self.generate_btn = ttk.Button(button_frame, text="Generate Snapshot", command=self._on_generate)
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        # Consolidate Commission Statements Button
        self.consolidate_btn = ttk.Button(button_frame, text="Consolidate Commission Statements", command=self._on_consolidate)
        self.consolidate_btn.pack(side=tk.LEFT, padx=5)

        # Calculate Retention Rates Button
        self.retention_btn = ttk.Button(button_frame, text="Calculate Retention Rates", command=self._on_retention)
        self.retention_btn.pack(side=tk.LEFT, padx=5)

        # Output log area
        self.log_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, state='disabled')
        self.log_area.pack(fill=tk.BOTH, expand=True)

        # Redirect stdout and stderr
        sys.stdout = RedirectText(self.log_area)
        sys.stderr = RedirectText(self.log_area)

    def _on_generate(self):
        self.generate_btn.config(state=tk.DISABLED)
        self.consolidate_btn.config(state=tk.DISABLED)
        self.retention_btn.config(state=tk.DISABLED)
        self.log_area.configure(state='normal')
        self.log_area.delete('1.0', tk.END)
        self.log_area.configure(state='disabled')
        threading.Thread(target=self._run_generation, daemon=True).start()

    def _on_consolidate(self):
        self.generate_btn.config(state=tk.DISABLED)
        self.consolidate_btn.config(state=tk.DISABLED)
        self.retention_btn.config(state=tk.DISABLED)
        self.log_area.configure(state='normal')
        self.log_area.delete('1.0', tk.END)
        self.log_area.configure(state='disabled')
        threading.Thread(target=self._run_consolidate, daemon=True).start()

    def _on_retention(self):
        self.generate_btn.config(state=tk.DISABLED)
        self.consolidate_btn.config(state=tk.DISABLED)
        self.retention_btn.config(state=tk.DISABLED)
        self.log_area.configure(state='normal')
        self.log_area.delete('1.0', tk.END)
        self.log_area.configure(state='disabled')
        threading.Thread(target=self._run_retention, daemon=True).start()

    def _run_generation(self):
        try:
            root_directory = os.getcwd()
            reports_folder = business.find_reports_folder(root_directory)
            snapshots_folder = business.find_snapshots_folder(root_directory)
            data_folder = business.find_data_folder(root_directory)

            print('Validating report data...')
            reports = business.define_spreadsheets(reports_folder)
            required = ['UHC Book of Business',
                        'Humana Book of Business',
                        'Devoted Book of Business',
                        'Cigna Book of Business',
                        'Aetna Book of Business']

            # Collect which required reports are actually present
            found = [r['name'] for r in reports if r['name'] in required]

            # If fewer than two, show error and abort
            if len(found) < 2:
                missing = set(required) - set(found)
                messagebox.showerror("Insufficient Reports",
                                     (f"At least two of the following reports are required: {', '.join(required)}.\n"
                                      f"Found only {len(found)}: {', '.join(found) or 'none'}.\n"
                                      "Please add more report files and try again."
                                      )
                                     )
                return
            print('Validating snapshot data...')
            data = business.define_data(data_folder)

            business.generate_mbob_snapshot(snapshots_folder, data_folder, reports)
            messagebox.showinfo("Success", "Snapshot generation complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
        finally:
            # Re-enable buttons
            self.generate_btn.config(state=tk.NORMAL)
            self.consolidate_btn.config(state=tk.NORMAL)
            self.retention_btn.config(state=tk.NORMAL)

    def _run_consolidate(self):
        try:
            business.consolidate_commission_statements()
            messagebox.showinfo("Success", "Commission statements consolidation complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
        finally:
            # Re-enable buttons
            self.generate_btn.config(state=tk.NORMAL)
            self.consolidate_btn.config(state=tk.NORMAL)
            self.retention_btn.config(state=tk.NORMAL)

    def _run_retention(self):
        try:
            root_directory = os.getcwd()
            business.calculate_retention_rates(root_directory)
            messagebox.showinfo("Success", "Retention rates calculation complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")
        finally:
            # Re-enable buttons
            self.generate_btn.config(state=tk.NORMAL)
            self.consolidate_btn.config(state=tk.NORMAL)
            self.retention_btn.config(state=tk.NORMAL)

if __name__ == '__main__':
    app = MBOSnapshotApp()
    app.mainloop()