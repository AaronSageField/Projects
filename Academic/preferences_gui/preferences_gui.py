# Aaron Sage Field
# Preferences GUI
# April 22nd, 2025
# Presentation Layer

import tkinter as tk
from tkinter import ttk
import db

class preferencesFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        
        # three input text fields and three output error labels
        self.name = None
        self.language = None
        self.autosave = None
        self.name_error = None
        self.language_error = None
        self.autosave_error = None

        # Read preferences from a file
        self.preferences = db.read()

        # calls initComponents to set up GUI components
        self.init_components()

    def init_components(self):
        
        # First three rows have a label, entry field, and error label
        ttk.Label(self, text = 'Name:').grid(row = 0, column = 0, padx = 5, pady = 2, sticky = tk.E)
        self.name = ttk.Entry(self, width = 21)
        self.name.grid(row = 0, column = 1, padx = 5, pady = 2)
        self.name.insert(0, self.preferences['name'])
        self.name_error = ttk.Label(self)
        self.name_error.grid(row = 0, column = 2, padx = 5, pady = 2, sticky = "w")
        ttk.Label(self, text = 'Language:').grid(row = 1, column = 0, padx = 5, pady = 2, sticky = tk.E)
        self.language = ttk.Entry(self, width = 21)
        self.language.grid(row = 1, column = 1, padx = 5, pady = 2)
        self.language.insert(0, self.preferences['language'])
        self.language_error = ttk.Label(self)
        self.language_error.grid(row = 1, column = 2, padx = 5, pady = 2, sticky = "w")
        ttk.Label(self, text = 'Auto Save Every x Minutes:').grid(row = 2, column = 0, padx = 5, pady = 2, sticky = tk.E)
        self.autosave = ttk.Entry(self, width = 21)
        self.autosave.grid(row = 2, column = 1, padx = 5, pady = 2)
        self.autosave.insert(0, self.preferences['autosave'])
        self.autosave_error = ttk.Label(self)
        self.autosave_error.grid(row = 2, column = 2, padx = 5, pady = 2, sticky = "w")

        # Call makeButtons method to populate two buttons
        self.makeButtons()

    def makeButtons(self):
        ttk.Button(self, text = 'Save', command = self.save, width = 9).grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'w')
        ttk.Button(self, text = 'Cancel', command = self.parent.destroy, width = 9).grid(row = 3, column = 1, padx = 5, pady = 5, sticky = tk.E)

    def validate_input(self, value, error_label, field_name):
        if not value:
            error_label.config(text = f'{field_name} is required.')
            return False
        try:
            int(value)
            error_label.config(text = f'{field_name} cannot be numeric.')
            return False
        except ValueError:
            error_label.config(text = '')
            return True

    def save(self):
        self.name_error.config(text = '')
        self.language_error.config(text = '')
        self.autosave_error.config(text = '')
        valid = True
        name = self.name.get().strip()
        language = self.language.get().strip()
        autosave = self.autosave.get().strip()

        # Check for valid data
        if not self.validate_input(name, self.name_error, 'Name'):
            valid = False
        if not self.validate_input(language, self.language_error, 'Language'):
            valid = False
        if not autosave:
            self.autosave_error.config(text = 'Auto Save is required.')
            valid = False
        else:
            try:
                if int(autosave) <= 0:
                    self.autosave_error.config(text = 'Must be greater than 0.')
                    valid = False
            except ValueError:
                self.autosave_error.config(text = 'Must be a number.')
                valid = False

        # if valid, db.save(preferences)
        if valid:
            preferences = {
                'name': name,
                'language': language,
                'autosave': autosave
            }
            
            # Send dictionary, overwrite 'preferences.txt'
            db.save(preferences)

            # Close GUI
            self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Preferences')
    preferences_frame = preferencesFrame(root)
    preferences_frame.pack(padx = 10, pady = 10)
    root.mainloop()
