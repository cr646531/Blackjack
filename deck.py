'''
Deck helper methods: create_deck, print_deck, shuffle_deck
'''

from card import Card

# Creates a standard deck of 52 cards
def create_deck():
	ranks = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
	suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
	deck = []

	for key in ranks.keys():
		for suit in suits:
			temp = Card(key, suit, ranks[key])
			deck.append(temp)

	return deck

# Prints each individual card in a deck - used for testing purposes
def print_deck(deck):

	for card in deck:
		print(f'{str(card)}\n')


# Shuffles the deck
# This method shuffles the deck in place. It does not return a new deck.
def shuffle_deck(deck):
	import random

	random.shuffle(deck)