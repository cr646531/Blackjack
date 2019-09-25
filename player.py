'''
Player class
	@parameters:
		name - defaults to 'Player'
	@methods:
		__init__
		__str__
		bet:
			Removes the bet from the player's bankroll and stores it
				@parameters: amount
				@output: returns 1 if successful. returns -1 if the bet is not between $1 and the player's current bankroll
		win_bet:
			Adds the winnings and the initial bet to the players bankroll, and resets the bet to 0
				@parameters: none
				@output: none
		lose_bet:
			Resets the bet to 0
				@parameters: none
				@output: none
		hit:
			Adds a card to the player's hand
				@parameters: card
				@output: none
		return_cards:
			Removes the cards from the player's hand, so they can be returned to the deck
				@parameters: none
				@output: list of cards
		get_total:
			Returns the total value of the cards in the player's hand (accounting for aces)
				@parameters: none
				@output: total
		get_bankroll:
			Returns the amount of money the player has as a string
				@parameters: none
				@output: bankroll (string)
		get_bet:
			Returns the amount of money the player bet as a string
				@parameters: none
				@output: bet (string)
		get_hand:
			Returns the player's hand as a string
				@parameters: none
				@output: none

'''

class Player():

	def __init__(self, name='Player'):

		self.name = name
		self.hand = []
		self.bankroll = 100
		self.bet = 0

	def __str__(self):

		return f'{self.name} has ${self.bankroll}'

	def bet(self, amount):

		if amount <= self.bankroll:
			self.bankroll -= amount
			self.bet = amount
			return 1
		elif amount <= 0:
			print(f'You must bet at least $1')
		else:
			print(f'Insufficent funds! You only have ${self.bankroll}.')
			return -1

	def win_bet(self):

		self.bankroll += (self.bet * 2)
		self.bet = 0

	def lose_bet(self):

		self.bet = 0

	def hit(self, card):

		self.hand.append(card)

	def return_cards(self):

		cards = hand
		hand = []
		return cards

	def get_total(self):

		num_aces = 0

		for card in self.hand:
			total += card.value
			if card.rank == 'Ace':
				num_aces++

		while num_aces != 0:
			if total > 21:
				total -= 10
				num_aces--
			else:
				break

		return total

	def get_bankroll(self):

		return f'{self.bankroll}'

	def get_bet(self):

		return f'{self.bet}'

	def get_hand(self):

		output = ''

		for card in self.hand:
			output += f'{str(card)} '

		output += f'({self.get_total()})'


