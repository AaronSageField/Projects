# Aaron Sage Field
# Card Objects
# April 17th, 2025
# An object-oriented program that displays, shuffles, and deals a deck of cards

import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck: 
    def __init__(self):
        self.__deck = []
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "Jack", "Queen", "King"]
        for suit in self.suits:
            for rank in self.ranks:
                if rank == "Ace":
                    value = 1
                elif rank in ["Jack", "Queen", "King"]:
                    value = 10
                else:
                    value = int(rank)
                card = Card(suit, rank, value)
                self.__deck.append(card)

    def shuffle(self):
        random.shuffle(self.__deck)

    def dealCard(self):
        return self.__deck.pop(0)

    def count(self):
        return len(self.__deck)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.__deck):
            raise StopIteration
        card = self.__deck[self._index]
        self._index += 1
        return card

class Hand:
    def __init__(self):
        self.__cards = []

    def addCard(self, card_object):
        self.__cards.append(card_object)

    def playCard(self, index=0):
        try:
            return self.__cards.pop(index)
        except (IndexError, TypeError):
            return None

    def count(self):
        return len(self.__cards)

    def totalPoints(self):
        total = 0
        for card in self.__cards:
            total += card.value
        return total

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.__cards):
            raise StopIteration
        card = self.__cards[self._index]
        self._index += 1
        return card
