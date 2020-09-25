import unittest
import Card

class Card_Test(unittest.TestCase):

	'''
	Test the suit of the card is set appropriately
	'''
	def testCardSuit(self):
		card=Card.Card('Spades','Ace')
		self.assertEqual(card.getSuit(),'Spades')

	'''
	Test the rank of the card is set appropriately
	'''
	def testCardRank(self):
		card=Card.Card('Spades','Ace')
		self.assertEqual(card.getRank(),'Ace')

	'''
	Test the string output for the card works right
	'''
	def testStr(self):
		card=Card.Card('Spades','Ace')
		self.assertEqual(card.__str__(),'Ace of Spades')

if __name__=='__main__':
	unittest.main()