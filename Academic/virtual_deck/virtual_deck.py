# Aaron Sage Field
# Card Objects
# April 17th, 2025
# An object-oriented program that displays, shuffles, and deals a deck of cards

# Three classes in a single module
import business
import sys

def main():
    deck = business.Deck()
    hand = business.Hand()
    print('Cards - Tester\n')
    print('DECK')
    for card in deck:
        print(card)
    deck.shuffle()
    print(f'\nShuffled Deck Count: {deck.count()}\n')
    print('HAND')
    for i in range(0, 5):
        hand.addCard(deck.dealCard())
    for card in hand:
        print(card)
    print(f'\nHand points: {hand.totalPoints()}')
    print(f'Hand count: {hand.count()}')
    print(f'Deck count: {deck.count()}\n')
    sys.exit(0)

if __name__ in '__main__':
    main()
