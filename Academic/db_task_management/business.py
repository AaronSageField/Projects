# Aaron Sage Field
# Task List
# April 19th, 2025
# Enables task management via a database
# Business Module

class Task:
    def __init__(self, description, completed, ID):
        self.description = description
        self.completed = completed
        self.ID = ID

    def __str__(self):
        if self.completed == 1:
            return self.description + ' (DONE!)'
        else:
            return self.description
