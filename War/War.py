import Deck_War
import Player
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def checkCards(playerOne,playerTwo,numDiscardShuffles):
	'''
	Function to check if the players have cards, or if they need discards

	Parameters
	----------
	playerOne : player, required
		first player to check
	playerTwo : player, required
		second player to check
	numDiscardShuffles : int, required
		number of times to shuffle the discard pile before placing it in the hand

	Returns
	-------
	True both players have at least one card to play, else False
	'''
	if playerOne.numCards()==0:
		if playerOne.numDiscards()!=0:
			playerOne.addDiscardToHand(numDiscardShuffles)
	if playerTwo.numCards()==0:
		if playerTwo.numDiscards()!=0:
			playerTwo.addDiscardToHand(numDiscardShuffles)
	return (playerOne.numCards()!=0 and playerTwo.numCards()!=0)


def playGame(numInitShuffles,numDiscardShuffles,warCards,maxRounds,displayEvents):
	'''
	Game logic for the game war
	
	Parameters
	----------
	numInitShuffles : int, required
		number of times to shuffle the inital deck
	numDiscard Shuffles :int, required
		number of times to shuffle discard piles before they go back to play
	warCards : int, required
		number of cards sacrificed by each player in war
	maxRounds : int, required
		max number of rounds before terminating
	displayEvents : bool, optional
		display each move by each player and outcomes.

	Returns
	-------
	Number of rounds to complete the game
	'''
	#create deck, and players. Shuffle deck and deal.
	deck=Deck_War.Deck_War()
	for i in range(numInitShuffles):
		deck.shuffle()

	playerOne=Player.Player('Player 1')
	playerTwo=Player.Player('Player 2')
	for i in range(1,53):
		#even cards to P1
		if i%2==0:
			playerOne.hand.append(deck.draw())
		#odd cards to P2.
		else:
			playerTwo.hand.append(deck.draw())
	#setup
	noWin=True
	roundCt=0

	while noWin:
		roundCt+=1
		if displayEvents:
			print(f'\nRound {roundCt}')
			print(f'{playerOne.getPlayerName()} has {playerOne.numCards()} cards left and {playerOne.numDiscards()} in discard')
			print(f'{playerTwo.getPlayerName()} has {playerTwo.numCards()} cards left and {playerTwo.numDiscards()} in discard')

		#make sure they have cards to play with
		noWin=checkCards(playerOne,playerTwo,numDiscardShuffles)
		if not noWin:
			continue
		
		#draw cards
		p1Card=playerOne.playCard()
		p2Card=playerTwo.playCard()
		if displayEvents:
			print(f'{playerOne.getPlayerName()} plays {p1Card} and {playerTwo.getPlayerName()} plays {p2Card}')
		#player 1 wins
		if p1Card.getValue()>p2Card.getValue():
			playerOne.discardCard([p1Card,p2Card])
			if displayEvents:
				print(f'\t{playerOne.getPlayerName()} wins this round')
		#player 2 wins
		elif p1Card.getValue()<p2Card.getValue():
			playerTwo.discardCard([p1Card,p2Card])
			if displayEvents:
				print(f'\t{playerTwo.getPlayerName()} wins this round')
		#same card value - WAR.
		else:
			if displayEvents:
				print('\tWAR!')
			# add tied cards to the war card lists
			p1WarCards=[p1Card]
			p2WarCards=[p2Card]
			while p1Card.getValue()==p2Card.getValue():
				#make sure they have cards to continue
				#p1 out of cards, check if discard pile has cards. If not, forfeit 
				noWin=checkCards(playerOne,playerTwo,numDiscardShuffles)
		
				if playerOne.numCards()==0:
					playerTwo.discardCard(p2WarCards)
					playerTwo.discardCard(p1WarCards)
					if displayEvents:
						print(f'\t{playerOne.getPlayerName()} ran out of cards!')
					break
				#p2 out of cards, check if discard pile has cards. If not, forfeit 
				elif playerTwo.numCards()==0:
					playerOne.discardCard(p1WarCards)
					playerOne.discardCard(p2WarCards)
					if displayEvents:
						print(f'\t{playerTwo.getPlayerName()} ran out of cards!')
					break
				#play specified number of sacrificial war cards. Making sure to leave at least one card for drawing.
				for i in range(0,warCards):
					if playerOne.numCards()>1:
						p1WarCards.append(playerOne.playCard())

					if playerTwo.numCards()>1:
						p2WarCards.append(playerTwo.playCard())
				#compare next round. should check if there are zero cards before playing.
				p1Card=playerOne.playCard()
				p2Card=playerTwo.playCard()
				if displayEvents:
					print(f'\t\t{playerOne.getPlayerName()} plays {p1Card} and {playerTwo.getPlayerName()} plays {p2Card}')

				p1WarCards.append(p1Card)
				p2WarCards.append(p2Card)

				#player 1 wins, gets cards back and all player 2's
				if p1Card.getValue()>p2Card.getValue():
					if displayEvents:
						print(f'\t\t{playerOne.getPlayerName()} wins the war')
					playerOne.discardCard(p1WarCards)
					playerOne.discardCard(p2WarCards)

				#player 2 wins, gets cards back and all player 1's
				elif p1Card.getValue()<p2Card.getValue():
					if displayEvents:
						print(f'\t\t{playerTwo.getPlayerName()} wins the war')
					playerTwo.discardCard(p2WarCards)
					playerTwo.discardCard(p1WarCards)
				#tie, loop again.
				else:
					if displayEvents:
						print('\tWAR CONTINUES')
					continue
		#check end condition
		playerOneTotCards=playerOne.numCards()+playerOne.numDiscards()
		playerTwoTotCards=playerTwo.numCards()+playerTwo.numDiscards()
		if playerOneTotCards==0 or playerTwoTotCards==0 or maxRounds<=roundCt:
			noWin=False

	
	#report who won.
	if displayEvents:
		print()
		if maxRounds<=roundCt:
			print(f'Tie, hit maximum rounds')
		if playerOneTotCards==0:
			print(f'{playerTwo.getPlayerName()} wins, {playerOne.getPlayerName()} ran out of cards!')
		else:
			print(f'{playerOne.getPlayerName()} wins, {playerTwo.getPlayerName()} ran out of cards!')

	return roundCt

def scrDots(ct,dot,num):
	'''
	Helper function to print dots to indicate the program is working

	Parameters
	----------
	ct : int, required
		 current count to reference
	dot : int, required
		count to display a dot at
	num : int, required
		count to display num at

	Returns
	-------
	ct+1. if incrementing count elsewhere, don't take the return
	'''
	if ct%num==0: print(ct,end="",flush=True)
	elif ct%dot==0: print('.',end="",flush=True)
	return ct+1



def main():
	'''
	Driver function
	'''
	fig,ax = plt.subplots()
	initShuffles=6
	#reshuffles=1
	warCards=3
	maxRounds=5000
	roundsToRun=100000
	dot,num=1000,10000
	color_list=['tab:blue','tab:orange','tab:green']
	for reshuffles in range(2):
		roundList=[]
		color=color_list[reshuffles]
		for i in range(roundsToRun):
			scrDots(i,dot,num)
			numRounds=playGame(initShuffles,reshuffles,warCards,maxRounds,False)
			roundList.append(numRounds)
		roundFreq=Counter(roundList)
		ax.scatter(list(roundFreq.keys()),list(roundFreq.values()),c=color,marker=',',s=1,label=f'{reshuffles} reshuffles')
	ax.set_xlabel('Rounds to complete (thousands)')
	ax.set_ylabel('Count')
	ax.legend()
	ax.set_title('Impact of Shuffling Discard Piles in War')
	plt.axis([0,maxRounds,0,roundsToRun/200])
	plt.show()
	print()
	return 0

main()
