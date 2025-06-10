# Aaron Sage Field
# Task List
# April 19th, 2025
# Enables task management via a database
# Database module

import sqlite3
import os
import sys
import business

DATA = 'task_list_db.sqlite'

def get_tasks():
    conn = sqlite3.connect(DATA)
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM Task')
        rows = c.fetchall()
    except sqlite3.OperationalError as e:
        if 'no such table: Task' in str(e):
            c.execute('''
                CREATE TABLE Task (
                    taskID INTEGER NOT NULL PRIMARY KEY,
                    description TEXT NOT NULL,
                    completed INTEGER NOT NULL
                    )
                ''')
            conn.commit()
            c.execute('SELECT taskID, description, completed FROM Task')
            rows = c.fetchall()
        else:
            print(f'Database error: {e}\n')
            conn.close()
            sys.exit()
    tasks = [business.Task(row[1], row[2], row[0]) for row in rows]
    c.close()
    conn.close()
    return tasks

def update_row(primary_key): # Flip completed attribute for a row
    conn = sqlite3.connect(DATA)
    c = conn.cursor()
    c.execute('''
        UPDATE Task SET completed = CASE completed 
        WHEN 1 THEN 0 ELSE 1 END WHERE taskID = ?
        ''', (primary_key,))
    conn.commit()
    conn.close()

def delete_row(primary_key): # Delete row where primary_key is true
    conn = sqlite3.connect(DATA)
    c = conn.cursor()
    c.execute(f'DELETE FROM Task WHERE taskID = ?', (primary_key,))
    conn.commit()
    conn.close()

def insert_row(tasks, user_description): # Add a row
    conn = sqlite3.connect(DATA)
    c = conn.cursor()
    sequence = len(tasks) + 1
    c.execute(f'INSERT INTO Task VALUES(?, ?, ?)', (sequence, user_description, 0))
    conn.commit()
    c.close()
    conn.close()
