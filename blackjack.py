'''
Blackjack
'''

# Card class
class Card():

	def __init__(self, rank, suit, value):
		self.rank = rank
		self.suit = suit
		self.value = value

	def __str__(self):
		return f'| {self.rank} of {self.suit} |'

# Creates a deck of 52 cards
def create_deck():
	ranks = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
	suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

	for key in ranks.keys():
		for suit in suits:
			temp = Card(key, suit, ranks[key])
			deck.append(temp)

	return deck

# Prints each individual card in a deck
def print_deck(deck):
	for card in deck:
		print(f'{str(card)}\n')


# Shuffles the deck
def shuffle_deck(deck):
	import random

	random.shuffle(deck)

