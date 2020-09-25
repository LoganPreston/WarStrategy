import unittest
import Deck_War
import copy

suits=('Hearts','Spades','Diamonds','Clubs')
ranks=('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values={'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13}

class Deck_War_Test(unittest.TestCase):

	'''
	test initializing the deck
	'''
	def testDeckCreation(self):
		deck=Deck_War.Deck_War()
		self.assertEqual(len(deck),52)

	'''
	test shuflling the deck, check the order isn't the same
	'''
	def testShuffle(self):
		deck=Deck_War.Deck_War()
		origOrder=copy.deepcopy(deck)
		deck.shuffle()
		self.assertFalse(origOrder.draw().__str__()==deck.draw().__str__())

	'''
	Try drawing one card on the deck. Since not shuffled, should be first card made.
	'''
	def testDraw(self):
		deck=Deck_War.Deck_War()
		card=deck.draw()
		self.assertEqual(card.__str__(),'Ace of Hearts')

	'''
	Check the value is being assigned right
	'''
	def testRankValue(self):
		deck=Deck_War.Deck_War()
		card=deck.draw()
		self.assertEqual(card.getValue(),values[card.getRank()])

	'''
	Make sure drawing one card decreases number of cards
	'''
	def testDrawUpdLen(self):
		deck=Deck_War.Deck_War()
		card=deck.draw()
		self.assertEqual(len(deck),51)

	'''
	Make sure drawing all cards in deck zeros it out
	'''
	def testDrawEntireDeck(self):
		deck=Deck_War.Deck_War()
		for i in range(1,53):
			card=deck.draw()
		self.assertEqual(len(deck),0)

	'''
	make sure overdrawing the deck throws exception.
	'''
	def testOverdrawDeck(self):
		deck=Deck_War.Deck_War()
		for i in range(1,53):
			card=deck.draw()
		with self.assertRaises(IndexError):
			card=deck.draw()

if __name__=='__main__':
	'''
	deck=Deck_War.Deck_War()
	origDeck=copy.deepcopy(deck)
	print('\t'.join([origDeck.draw().__str__() for i in range(1,53)]))
	print()
	deck.shuffle()
	print('\t'.join([deck.draw().__str__() for i in range(1,53)]))
	'''
	unittest.main()
