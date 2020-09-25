import Card
import random

suits=('Hearts','Spades','Diamonds','Clubs')
ranks=('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values={'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13}


'''
Deck class for War game
'''
class Deck_War():
	'''
	Initialize deck, one card for each value in each suit. 52 cards total.
	'''
	def __init__(self):
		self.deck=[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card.Card(suit,rank,values[rank]))

	'''
	shuffle the order of the deck
	'''
	def shuffle(self):
		random.shuffle(self.deck)


	'''
	Draw a card off the top of the deck. Pulls from the end of the list
	'''
	def draw(self):
		return self.deck.pop(0)

	'''
	Return the number of cards in the deck.
	'''
	def __len__(self):
		return len(self.deck)

	'''
	Give list of cards in deck
	'''
	def __str__(self):
		deckOrder=''
		for card in self.deck:
			deckOrder+=f'{card.__str__()}\n'
		return deckOrder
