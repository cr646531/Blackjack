'''
Player class
	@parameters:
		name - defaults to 'Player'
	@methods:
		__init__
		__str__
		take_bet:
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
		push:
			Returns the bet to the player's hand, and reset the bet to 0
				@parameters: none
				@output: none
		hit:
			Adds a card to the player's hand
				@parameters: card
				@output: none
		double_down:
			Doubles the player's bet and adds a card to the player's hand
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

		return f'You have ${self.bankroll}\n'

	def take_bet(self, amount):
		if amount <= self.bankroll and amount > 0:
			self.bankroll -= amount
			self.bet = amount
			return 1
		elif amount <= 0:
			print(f'You must bet at least $1')
			return -1
		else:
			print(f'Insufficent funds! You only have ${self.bankroll}.')
			return -1

	def win_bet(self):

		self.bankroll += (self.bet * 2)
		self.bet = 0

	def lose_bet(self):

		self.bet = 0

	def push(self):
		self.bankroll += self.bet
		self.bet = 0

	def hit(self, card):

		self.hand.append(card)

	def double_down(self, card):

		if self.bet <= self.bankroll:
			self.bankroll -= self.bet
			self.bet *= 2
			self.hit(card)
		else:
			print("You don't have enough to double-down! ")
			self.hit(card)

	def return_cards(self):

		cards = self.hand
		self.hand = []
		return cards

	def get_total(self):

		num_aces = 0
		total = 0

		for card in self.hand:
			total += card.value
			if card.rank == 'Ace':
				num_aces += 1

		while num_aces != 0:
			if total > 21:
				total -= 10
				num_aces -= 1
			else:
				break

		return total

	def get_bankroll(self):

		return self.bankroll

	def get_bet(self):

		return f'{self.bet}'

	def get_hand(self):

		output = ''

		for card in self.hand:
			output += f'{str(card)} '

		output += f'({self.get_total()})'
		return output

