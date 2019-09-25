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
	show_hands(player, dealer)

def show_hands(player, dealer):
	print(f"---------------------------------------------------------------------\n")
	print(f"Dealer's hand: {dealer.get_hand()}\n")
	print(f"Player's hand: {player.get_hand()}\n")
	print(f"---------------------------------------------------------------------\n")


def prompt_player_action(deck, player, dealer):

	response = input('Would you like to hit, stay or double-down? (h/s/d) ').lower()

	if response == 'h':

		player.hit(deck.pop(0))
		show_hands(player, dealer)

		if player.get_total() > 21:
			return -1
		elif player.get_total() == 21:
			return 1
		else:
			return 0

	elif response == 's':

		return 1

	elif response == 'd':

		player.double_down(deck.pop(0))
		
		if player.get_total() > 21:
			return -1
		else:
			return 1

	else:
		print("Type 'h' to hit, 's' to stay, or 'd' to double-down ")
		return 0

def return_cards_to_deck(deck, player, dealer):

	 new_deck = deck + player.return_cards() + dealer.return_cards()
	 return new_deck



