
import random
'''
Player class, holds cards
'''
class Player():

	'''
	Initialize player w/ name and empty hand
	'''
	def __init__(self,name):
		self.hand=[]
		self.discardPile=[]
		self.name=name

	'''
	Add card or multiple cards to the players hand
	'''
	def addCards(self,newCards):
		#adding many cards
		if type(newCards)==type(list()):
			self.hand.extend(newCards)
		#adding single card
		else:
			self.hand.append(newCards)		

	'''
	Remove a card from the hand
	'''
	def playCard(self):
		return self.hand.pop(0)

	'''
	Discard card(s) that will be added to hand later
	'''
	def discardCard(self,discardCards):
		#adding many cards
		if type(discardCards)==type(list()):
			self.discardPile.extend(discardCards)
		#adding single card
		else:
			self.discardPile.append(discardCards)

	'''
	Add discarded cards back to main hand, shuffle
	'''
	def addDiscardToHand(self,discardShuffles):
		for i in range(0,discardShuffles):
			random.shuffle(self.discardPile)
		self.hand=self.discardPile
		self.discardPile=[]

	'''
	Check how many cards are in a hand
	'''
	def numCards(self):
		return len(self.hand)

	'''
	Check number of discards that can be added to hand
	'''
	def numDiscards(self):
		return len(self.discardPile)

	'''
	print out player and number of cards
	'''
	def __str__(self):
		return f'{self.name} has {len(self.hand)} cards'

	def getPlayerName(self):
		return self.name
