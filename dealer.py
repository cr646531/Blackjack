'''
Dealer class
	@parameters: none
	@methods:
		play:
			continues to hit until the dealer reaches at least 17
'''

from player import Player

class Dealer(Player):

	def __init__(self):
		Player.__init__(self)

	def play(self, deck):

		while self.get_total() <= 16:
			self.hit(deck.pop(0))

		

