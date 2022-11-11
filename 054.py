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

import math
import tools.timer as timer

def poker_hand_score(hand: str) -> int:
    """gives an int score for a poker hand
    
    Args:
        hand: string formatted as "8C 2D TH AS 4D"

    Returns:
        An integer score for the hand. Interpreting this number is not really important, just know that a higher int represents a better hand.

        Formatting:
            xx - straight flush, value of highest card, this covers royal flush
            xx - four of a kind, value of cards
            xx - full house, value of triple
            x  - flush, just use a 1
            x  - straight, just use a 1, the rest will be handled by card order
            xx - three of a kind, value of triple
            xx - value of higher pair if two pairs
            xx - value of lower pair if two pairs, or only pair if one
            xxxxxxxxxx - value of all cards in descending order

            a royal flush would be written as
            140000110000001413121110

            high card would be written as
            1311100802
    """

    hand = hand.replace('T', '10')
    hand = hand.replace('J', '11')
    hand = hand.replace('Q', '12')
    hand = hand.replace('K', '13')
    hand = hand.replace('A', '14')
    
    hand = hand.split(' ')

    hand_score = ''

    # convert to tuples
    for card in range(5):
        hand[card] = (f'{hand[card][:-1]:0>2}', hand[card][-1])

    # display hand for reference
    hand.sort(reverse=True)

    #cards
    for card in sorted(hand, reverse=True):
        hand_score += card[0]

    #multiples
    numbers = {}
    for card in hand:
        numbers[card[0]] = numbers.setdefault(card[0], 0) + 1

    pairs = [number for number, count in numbers.items() if count == 2]
    triples = [number for number, count in numbers.items() if count == 3]
    quads = [number for number, count in numbers.items() if count == 4]

    #single or lower pair
    if len(pairs) > 0:
        hand_score = min(pairs) + hand_score
    else:
        hand_score = '00' + hand_score
    
    #higher of two pairs
    if len(pairs) == 2:
        hand_score = max(pairs) + hand_score
    else:
        hand_score = '00' + hand_score
    
    #triples
    if len(triples) == 1:
        hand_score = triples[0] + hand_score
    else:
        hand_score = '00' + hand_score

    #straight
    straight = (len(numbers) == 5) and (int(min(numbers)) == int(max(numbers)) - 4)
    if straight:
        hand_score = max(numbers) + hand_score
    else:
        hand_score = '00' + hand_score

    #flush
    flush = all(card[1] == hand[0][1] for card in hand)
    if flush:
        hand_score = '1' + hand_score
    else:
        hand_score = '0' + hand_score

    #full house
    if len(triples) == 1 and len(pairs) == 1:
        hand_score = triples[0] + hand_score
    else:
        hand_score = '00' + hand_score
    
    #quads
    if len(quads) == 1:
        hand_score = quads[0] + hand_score
    else:
        hand_score = '00' + hand_score

    #straight flush
    if straight and flush:
        hand_score = max(numbers) + hand_score
    # this will be lost when converting to int
    # else:
    #     hand_score = '00' + hand_score

    return int(hand_score)

t = timer.Timer(verbose=True)
t.start()

with open('054_poker.txt', 'r', encoding='UTF-8') as hands:
    hand_number = 0
    p1_wins = 0
    p2_wins = 0
    for hand in hands.readlines():
        p1_hand = hand[:14]
        p2_hand = hand[15:].rstrip()

        p1_hand_score = poker_hand_score(p1_hand)
        p2_hand_score = poker_hand_score(p2_hand)

        # print(f'{p1_hand}: {p1_hand_score:>20}')
        # print(f'{p2_hand}: {p2_hand_score:>20}')

        hand_number += 1

        if p1_hand_score > p2_hand_score:
            p1_wins += 1
            # print(f'{hand_number}: P1 wins!')
        elif p2_hand_score > p1_hand_score:
            p2_wins += 1
            # print(f'{hand_number}: P2 wins!')
        else:
            None
            # print(f'{hand_number}: Tie! Nobody wins!')

        # print()

t.stop()

print(f'P1: {p1_wins}')
print(f'P2: {p2_wins}')