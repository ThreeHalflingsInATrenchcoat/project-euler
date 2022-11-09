# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
# 	 	2C 3S 8S 8D TD
# Pair of Eights
# 	 	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
# 	 	2C 5C 7D 8S QH
# Highest card Queen
# 	 	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
# 	 	3D 6D 7D TD QD
# Flush with Diamonds
# 	 	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
# 	 	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
# 	 	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
# 	 	3C 3D 3S 9S 9D
# Full House
# with Three Threes
# 	 	Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?

from enum import Enum

class HandValues(Enum):
    high_card = 1
    one_pair = 2
    two_pairs = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9

def poker_hand_score(hand: str) -> tuple:
    """gives a tuple score for a poker hand (hand type, high card)
    
    Args:
        hand: string formatted as "8C 2D TH AS 4D"

    Returns:
        a tuple with a score for hand type follow by the high card value
    """
    print(hand)

    hand = hand.replace('T', '10')
    hand = hand.replace('J', '11')
    hand = hand.replace('Q', '12')
    hand = hand.replace('K', '13')
    hand = hand.replace('A', '14')
    
    hand = hand.split(' ')


    # convert to tuples
    for card in range(5):
        hand[card] = (int(hand[card][:-1]), hand[card][-1])

    # display hand for reference
    hand.sort()
    print(hand)

    #high card
    high_card = max(hand, key=lambda x: x[0])[0]
    print(f'high card: {high_card}')

    #multiples
    numbers = {}
    for card in hand:
        numbers[card[0]] = numbers.setdefault(card[0], 0) + 1

    max_set = max[]


    






with open('054_poker.txt', 'r', encoding='UTF-8') as hands:
    hand = hands.readline().rstrip()
    hand = hands.readline().rstrip()
p1_hand = hand[:14]
p2_hand = hand[15:] 

poker_hand_score(p1_hand)
#p1_score = poker_hand_score(p1_hand)
#print(p1_score)