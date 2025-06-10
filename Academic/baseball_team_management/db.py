# Database Layer

import sqlite3
from contextlib import closing
from Objects import Player, Lineup

DB_FILE = 'player_db.sqlite'
conn = None

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    global conn
    if conn:
        conn.close()
        conn = None

def get_players():
    with closing(conn.cursor()) as c:
        c.execute('SELECT playerID, batOrder, firstName, lastName, position, atBats, hits FROM Player')
        players_data = c.fetchall()
    lineup = Lineup()
    for row in players_data:
        player = Player(row['playerID'], row['batOrder'], row['firstName'], row['lastName'], row['position'], row['atBats'], row['hits'])
        lineup.add(player)
    return lineup

def get_player(playerID):
    with closing(conn.cursor()) as c:
        c.execute('SELECT playerID, batOrder, firstName, lastName, position, atBats, hits FROM Player WHERE playerID = ?', (playerID,))
        row = c.fetchone()
    if row:
        return Player(row['playerID'], row['batOrder'], row['firstName'], row['lastName'], row['position'], row['atBats'], row['hits'])
    return None

def add_player(player):
    player_id = None
    with closing(conn.cursor()) as c:
        c.execute('INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits) VALUES (?, ?, ?, ?, ?, ?)',
                       (player.batOrder, player.fName, player.lName, player.position, player.atBats, player.hits))
        conn.commit()
        c.execute('SELECT playerID FROM Player WHERE batOrder = ? AND firstName = ? AND lastName = ? AND position = ? AND atBats = ? AND hits = ?',
                       (player.batOrder, player.fName, player.lName, player.position, player.atBats, player.hits))
        result = c.fetchone()
    player_id = result['playerID']
    return player_id

def delete_player(playerID):
    with closing(conn.cursor()) as c:
        c.execute('DELETE FROM Player WHERE playerID = ?', (playerID,))
        conn.commit()

def update_bat_order(lineup):
    with closing(conn.cursor()) as c:
        for i, player in enumerate(lineup):
            c.execute('UPDATE Player SET batOrder = ? WHERE playerID = ?', (i + 1, player.playerID))
        conn.commit()

def update_player(player):
    with closing(conn.cursor()) as c:
        c.execute('UPDATE Player SET position = ?, atBats = ?, hits = ? WHERE playerID = ?',
                       (player.position, player.atBats, player.hits, player.playerID))
        conn.commit()
