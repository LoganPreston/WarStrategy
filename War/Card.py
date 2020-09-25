'''
Generic card class, can hold suit and rank of the card. Default will create Ace of Spades
'''
class Card():

	'''
	Initialize card suit and rank
	'''
	def __init__(self,suit='Spades',rank='Ace',value=1):
		self.suit=suit
		self.rank=rank
		self.value=value

	'''
	Return the suit of the card
	'''
	def getSuit(self):
		return self.suit

	'''
	Return the rank of the card
	'''
	def getRank(self):
		return self.rank

	'''
	return the value of the card
	'''
	def getValue(self):
		return self.value

	'''
	Print the card info in the form: <Rank> of <Suit>
	'''
	def __str__(self):
		return f'{self.rank} of {self.suit}'
