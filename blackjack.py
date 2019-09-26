'''
Blackjack
'''

from deck import create_deck, print_deck, shuffle_deck, get_num_cards
from gameplay import create_player, prompt_bet, deal, show_hands, prompt_player_action, return_cards_to_deck
from player import Player
from dealer import Dealer

'''
Create dealer and player\
Create and shuffle the deck
Ask for the player's bet
Deal the cards
'''

dealer = Dealer()
player = create_player()
deck = create_deck()
game_over = False

while game_over == False:

	shuffle_deck(deck)
	prompt_bet(player)
	deal(deck, player, dealer)

	'''
	Player's turn:
		The flag determines when the player's turn is over. 
			If the flag is 0, the turn continues
			If the flag is 1, the turn is over
			If flag is -1, the player has busted - skip the dealer's turn
	'''
	flag = 0

	while flag == 0:
		flag = prompt_player_action(deck, player, dealer)

	'''
	The dealer only takes their turn if the player has not busted
	'''
	if flag != -1:
		dealer.play(deck)


	'''
	Check for the following end-game conditions: 
		player busts
		dealer busts
			player wins
			draw
			dealer wins
	'''
	show_hands(player, dealer)

	if player.get_total() > 21:

		print(f"You busted!")
		player.lose_bet()

	elif dealer.get_total() > 21:

		print(f"Dealer busted!")
		player.win_bet()

	else:

		if player.get_total() > dealer.get_total():

			print(f"You win!")
			player.win_bet()

		elif player.get_total() == dealer.get_total():

			print("Push")
			player.push()

		else:

			print("Dealer wins!")
			player.lose_bet()

	'''
	Return the cards to the deck, and ask the player if they want to play again
	'''		

	print(str(player))
	deck = return_cards_to_deck(deck, player, dealer)

	if player.get_bankroll() == 0:
		game_over = True
		print('GAME OVER\n')

	while game_over == False:

		play_again = input('Would you like to play again? (y/n) ').lower()

		if play_again == 'y':
			break
		elif play_again == 'n':
			game_over = True 
		else:
			print("Type 'y' for yes, and 'n' for no\n")






