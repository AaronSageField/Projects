# Aaron Sage Field
# Task List
# April 19th, 2025
# Enables task management via a database
# Presentation module

import sys
import business
import database as db

def display_incomplete(tasks):
    if tasks:
        for task in tasks:
            if task.completed == 0:
                print(f'{task.ID}. {task.description}')
    else:
        print('All tasks complete.')
    print('')

def display_complete(tasks):
    if tasks:
        for task in tasks:
            if task.completed == 1:
                print(f'{task.ID}. {task.description}')
    else:
        print('No completed tasks.')
    print('')

def add(tasks):
    user_description = input('Description: ')
    db.insert_row(tasks, user_description)
    print('')

def complete(tasks):
    user_index = input('Number: ')
    for task in tasks:
        try:
            if int(user_index) == task.ID:
                primary_key = int(user_index)
                db.update_row(primary_key)
                break
        except ValueError:
            print('Please enter a task number.')
    else:
        print('Task does not exist.')
    print('')

def delete(tasks):
    user_index = input('Number: ')
    for task in tasks:
        try:
            if int(user_index) == task.ID:
                primary_key = int(user_index)
                db.delete_row(primary_key)
                break
        except ValueError:
            print('Please enter a task number.')
    else:
        print('Task does not exist.')
    print('')

def display_commands(commands):
    print('COMMAND MENU')
    for key in commands:
        print(f'{key:<9}{commands[key]["description"]}')
    print(f'{"exit":<9}- Exit program\n')

def main():
    commands = {
        'view': {
            'description': '- View pending tasks',
            'function': display_incomplete
            },
        'history': {
            'description': '- View completed tasks',
            'function': display_complete
            },
        'add': {
            'description': '- Add a task',
            'function': add
            },
        'complete': {
            'description': '- Complete a task',
            'function': complete
            },
        'delete': {
            'description': '- Delete a task',
            'function': delete
            }
        }
    print('Task List\n')
    display_commands(commands)

    # Main loop
    while True:
        tasks = db.get_tasks()
        user_input = input('Command: ').strip().lower()
        if user_input == 'exit':
            print('Bye!')
            sys.exit()
        for key in commands:
            if user_input == key:
                commands[key]['function'](tasks)
                break
        else:
            print('Invalid command.\n')
            display_commands(commands)

if __name__ == '__main__':
    main()
