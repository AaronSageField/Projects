# Aaron Sage Field
# Team Management Program: Part 3
# April 22nd, 2025
# An object-oriented Baseball Team Manager program
# Presentation Layer

from datetime import date
import sys
from Objects import Player, Lineup
import db

def edit_stats(lineup):
    try:
        user_index = int(input('Enter a lineup number to edit: '))
        player = lineup.get(user_index)
        at_bats = int(input('At bats: '))
        if at_bats < 0 or len(str(at_bats)) > 5:
            raise ValueError
        hits = int(input('Hits: '))
        if hits < 0 or hits > at_bats or len(str(at_bats)) > 5:
            raise ValueError
        player.atBats = at_bats
        player.hits = hits
        db.update_player(player)
        print(f'{str(player)} was modified.\n')
    except ValueError:
        print('Please enter a valid player number or stats.\n')
    except IndexError:
        print('Please enter a valid player number.\n')

def edit_position(lineup, valid_positions):
    try:
        user_index = int(input('Enter a lineup number to edit: '))
        player = lineup.get(user_index)
        new_position = input('Enter a new Position: ').strip().upper()
        if new_position in valid_positions:
            player.position = new_position
            db.update_player(player)
            print(f'{str(player)} was updated.\n')
        else:
            print('Invalid position.\n')
    except ValueError:
        print('Please enter a valid player number.\n')
    except IndexError:
        print('Please enter a valid player number.\n')

def move_player(lineup):
    try:
        old_position = int(input('Enter a current lineup number to move: ').strip())
        player = lineup.get(old_position)
        print(f'{str(player)} was selected.')
        new_position = int(input('Enter a new lineup number: '))
        if new_position == old_position:
            raise ValueError
        lineup.move(old_position, new_position)
        db.update_bat_order(lineup)
        print(f'{str(player)} was moved.\n')
    except ValueError:
        print('Please enter a valid player number.\n')
    except IndexError:
        print('Please enter a valid player number.\n')

def remove_player(lineup):
    try:
        user_index = int(input('Enter a lineup number to remove: '))
        player = lineup.get(user_index)
        db.delete_player(player.playerID)
        lineup.remove(user_index)
        print(f'{str(player)} was removed!\n')
    except ValueError:
        print('Please enter a valid player number.\n')
    except IndexError:
        print('Please enter a valid player number.\n')

def add_player(lineup, valid_positions):
    f_name = input('First Name: ').strip()
    if not f_name:
        print('First name cannot be empty.\n')
        return
    l_name = input('Last Name: ').strip()
    if not l_name:
        print('Last name cannot be empty.\n')
        return
    elif len(f_name + ' ' + l_name) > 30:
        print('Full name cannot be longer than 30 characters.\n')
        return
    position = input('Position: ').strip().upper()
    if position not in valid_positions:
        print('Invalid position.\n')
        return
    try:
        at_bats = int(input('At bats: '))
        if at_bats < 0 or len(str(at_bats)) > 5:
            raise ValueError
        hits = int(input('Hits: '))
        if hits < 0 or hits > at_bats or len(str(at_bats)) > 5:
            raise ValueError
    except ValueError:
        print('Invalid stats.\n')
        return
    player = Player(None, len(lineup) + 1, f_name, l_name, position, at_bats, hits)
    player_id = db.add_player(player)
    player.playerID = player_id
    lineup.add(player)
    db.update_bat_order(lineup)
    print(f'{f_name} {l_name} was added!\n')

def display_lineup(lineup):
    local_separator = ('-' * 60)
    print(f'\n    Player{"POS":>31}{"AB":>6}{"H":>6}{"AVG":>8}\n{local_separator}')
    if lineup:
        for i, player in enumerate(lineup):
            print(f'{i + 1:<3}'
                  f'{str(player):<31}'
                  f'{player.position:>6}'
                  f'{player.atBats:>6}'
                  f'{player.hits:>6}'
                  f'{player.batting_average():>8.3f}')
    print('')

def display_menu(commands):
    print('MENU OPTIONS')
    for i, command in enumerate(commands):
        print(f'{command["id"]}{command["description"]}')
    print(f'{i + 2} - Exit program\n')

def countdown_calculator(current_date):
    print(f'CURRENT DATE:{current_date:>14}')
    user_input = input('GAME DATE:       ').strip()
    try:
        user_date = date.fromisoformat(user_input)
        current_date_math = date.fromisoformat(current_date)
        difference = user_date - current_date_math
        days = difference.days
        if days >= 0:
            print(f'DAYS UNTIL GAME: {days}\n')
        else:
            print('')
    except ValueError:
        print('')

def main():
    db.connect()
    lineup = db.get_players()
    valid_positions = ('C','1B','2B','3B','SS','LF','CF','RF','P')
    commands = [
        {'description': ' - Display lineup',
         'id': '1',
         'function': display_lineup},
        {'description': ' - Add player',
         'id': '2',
         'function': add_player},
        {'description': ' - Remove player',
         'id': '3',
         'function': remove_player},
        {'description': ' - Move player',
         'id': '4',
         'function': move_player},
        {'description': ' - Edit player position',
         'id': '5',
         'function': edit_position},
        {'description': ' - Edit player stats',
         'id': '6',
         'function': edit_stats}
    ]
    current_date = date.today().strftime('%Y-%m-%d')
    separator_line = ('=' * 60)
    printable_positions = ', '.join(valid_positions)
    print(f'{separator_line}\n{"Baseball Team Manager":>40}\n')
    countdown_calculator(current_date)
    display_menu(commands)
    print(f'POSITIONS\n{printable_positions}\n{separator_line}\n')
    while True:
        user_input = input('Menu option: ').strip()
        if user_input == str(len(commands) + 1):
            db.close()
            print('Bye!\n')
            sys.exit()
        for command in commands:
            if user_input == command['id']:
                if user_input in ['2','5']:
                    command['function'](lineup, valid_positions)
                else:
                    command['function'](lineup)
                break
        else:
            print('\nInvalid command.\n')
            display_menu(commands)

if __name__ in '__main__':
    main()
            
