'''
Gameplay
'''

from player import Player
from dealer import Dealer

def create_player():

	# create the player
	name = input('What is your name? ')
	player = Player(name)
	print(f'\n{str(player)}')
	return player

def prompt_bet(player):

	flag = -1

	while flag == -1:
		bet = input('How much would you like to bet? ')

		try:
			bet = int(bet)
			flag = player.take_bet(bet)
		except:
			print('Please enter a number!')


	print(f'Current bet: ${player.bet}')

def deal(deck, player, dealer):

	player.hit(deck.pop(0))
	player.hit(deck.pop(0))
	dealer.hit(deck.pop(0))

	print(f"Dealer's hand: {dealer.get_hand()}\n")
	print(f"Player's hand: {player.get_hand()}\n")
