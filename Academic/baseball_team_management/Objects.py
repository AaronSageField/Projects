# Aaron Sage Field
# Team Management Program: Part 3
# April 22nd, 2025
# An object-oriented Baseball Team Manager program
# Business Layer

class Player:
    def __init__(self, playerID, batOrder, fName, lName, position, atBats, hits):
        self.playerID = playerID
        self.batOrder = batOrder
        self.fName = fName
        self.lName = lName
        self.position = position
        self.atBats = atBats
        self.hits = hits

    def __str__(self):
        return f"{self.fName} {self.lName}"

    def batting_average(self):
        return self.hits / self.atBats if self.atBats > 0 else 0

class Lineup:
    def __init__(self):
        self.__team = []

    def add(self, player_object):
        self.__team.append(player_object)

    def remove(self, lineup_number):
        del self.__team[lineup_number - 1]

    def get(self, lineup_number):
        return self.__team[lineup_number - 1]

    def move(self, old_lineup_number, new_lineup_number):
        player = self.__team.pop(old_lineup_number - 1)
        self.__team.insert(new_lineup_number - 1, player)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__team):
            raise StopIteration
        player = self.__team[self.__index]
        self.__index += 1
        return player

    def __len__(self):
        return len(self.__team)
