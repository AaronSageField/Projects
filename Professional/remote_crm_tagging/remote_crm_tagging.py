import requests
import re
import sys
import tkinter as tk
from tkinter import ttk, scrolledtext

class CRMUpdaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRM Record Updater")

        # API Configuration
        self.api_token = 'example'
        self.base_url = 'example'
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
        }

        # Record Type Selection
        ttk.Label(self.root, text="Record Type:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.record_type = tk.StringVar(value="Client")
        ttk.Radiobutton(self.root, text="Client", variable=self.record_type, value="Client").grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.root, text="Lead", variable=self.record_type, value="Lead").grid(row=0, column=2, padx=5, pady=5)

        # Tag Input
        ttk.Label(self.root, text="Tag:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.tag_entry = ttk.Entry(self.root, width=30)
        self.tag_entry.insert(0, "Test")
        self.tag_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        # Apply Button
        ttk.Button(self.root, text="Apply Now", command=self.apply_updates).grid(row=2, column=0, columnspan=3, pady=10)

        # Output Text Area
        self.output_text = scrolledtext.ScrolledText(self.root, width=50, height=10, wrap=tk.WORD)
        self.output_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.output_text.tag_configure("error", foreground="red")

        # Initial load of record IDs
        self.record_ids = self.read_record_ids()

    def validate_record_ids(self, content):
        # IDs must be in quotes, comma-separated; whitespace around commas allowed
        pattern = r'^"[^"]*"\s*(?:\s*,\s*"[^"]*"\s*)*$'
        return bool(re.match(pattern, content))

    def read_record_ids(self):
        try:
            with open("records.txt", "r") as file:
                raw_content = file.read()
                # Strip leading/trailing whitespace (including blank lines) before validation
                content = raw_content.strip()
                if not content:
                    self.output_text.insert(tk.END, "records.txt is empty.\n")
                    return []
                if not self.validate_record_ids(content):
                    self.output_text.insert(
                        tk.END,
                        "Invalid format in records.txt. Expected: \"id1\", \"id2\", \"id3\"\n",
                        "error"
                    )
                    return []
                # Split on commas and trim each ID
                raw_ids = content.split(",")
                return [rid.strip().strip('"') for rid in raw_ids if rid.strip()]
        except FileNotFoundError:
            self.output_text.insert(tk.END, "records.txt not found. Creating a new empty records.txt.\n")
            with open("records.txt", "w") as file:
                file.write("")
            self.output_text.insert(
                tk.END,
                "Please add records to records.txt in the format: \"id1\", \"id2\", \"id3\"\n"
            )
            return []
        except Exception as e:
            self.output_text.insert(tk.END, f"Error reading records.txt: {str(e)}\n", "error")
            return []

    def apply_updates(self):
        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Re-load record IDs each time, to pick up any file changes
        self.record_ids = self.read_record_ids()

        if not self.record_ids:
            self.output_text.insert(tk.END, "No valid record IDs to process.\n", "error")
            return

        tag = self.tag_entry.get().strip()
        if not tag:
            self.output_text.insert(tk.END, "Please enter a tag.\n", "error")
            return

        payload_template = {
            "type": self.record_type.get(),
            "tags": [tag]
        }

        for record_id in self.record_ids:
            payload = payload_template.copy()
            payload["record_id"] = record_id
            try:
                response = requests.patch(self.base_url, headers=self.headers, json=payload)
                self.output_text.insert(tk.END, f"Record ID: {record_id} - Response Code: {response.status_code}\n")
                self.output_text.insert(tk.END, f"Response: {response.text}\n")
                if response.status_code in (400, 422):
                    self.output_text.insert(
                        tk.END,
                        f"Error: Invalid tag '{tag}' for Record ID: {record_id}\n",
                        "error"
                    )
            except requests.RequestException as e:
                self.output_text.insert(tk.END, f"Error with Record ID {record_id}: {str(e)}\n", "error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRMUpdaterApp(root)
    root.mainloop()

