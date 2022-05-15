from deck_of_cards import deck_of_cards
import itertools
from functools import cmp_to_key
import statistics
import time
import math

from hands import *

# 
# ------------------------- CONSTANTS -------------------------
# 
HANDS = ["high card", "pair", "two pair", "3 of a kind", "straight", "flush", "full house", "4 of a kind", "straight flush"]
SUITS = ["spade", "heart", "diamond", "club"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]


# 
# ------------------------- FORMATTING / INPUT GATHERING -------------------------
# 

#
# Convert Dictionary of card names in english to corresponding suit and rank numbers formatted in tuples
#	
#		suit: 0 = spades, 1 = hearts, 2 = diamonds, 3 = clubs
#		rank: 1 = Ace, 11 = Jack, 12 = Queen, 13 = King
# 
def card_names_to_tuples(card_names):
	suit = 0
	rank = 0
	card_number = 0

	cards = {"hand": [], "river": []}


	# Cards in hand
	for card_name in card_names["hand"] + card_names["river"]:
		card_number += 1

		if("spade" in card_name.lower()):
			suit = 0
		elif("heart" in card_name.lower()):
			suit = 1
		elif("diamond" in card_name.lower()):
			suit = 2
		elif("club" in card_name.lower()):
			suit = 3



		if("ace" in card_name.lower()):
			rank = 1
		elif("2" in card_name.lower()):
			rank = 2
		elif("3" in card_name.lower()):
			rank = 3
		elif("4" in card_name.lower()):
			rank = 4
		elif("5" in card_name.lower()):
			rank = 5
		elif("6" in card_name.lower()):
			rank = 6
		elif("7" in card_name.lower()):
			rank = 7
		elif("8" in card_name.lower()):
			rank = 8
		elif("9" in card_name.lower()):
			rank = 9
		elif("10" in card_name.lower()):
			rank = 10
		elif("jack" in card_name.lower()):
			rank = 11
		elif("queen" in card_name.lower()):
			rank = 12
		elif("king" in card_name.lower()):
			rank = 13


		if(card_number < 3):
			cards["hand"].append((suit, rank))
		else:
			cards["river"].append((suit, rank))


	return cards


# 
# Form inputs into dictionary
# 	returns {'stage': stage, 'card_names': card_names}
# 
def gather_inputs(stage = None, hand = None, river = None):
	inputs = {}

	card_names = {"hand": [card for card in hand if card != ""], "river": [card for card in river if card != ""]}
	inputs["card_names"] = card_names
	inputs["stage"] = stage


	return inputs




# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# 
#	ODDS CALCULATIONS
# 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------




# 
# Calculate the odds for any hand to be a high card given a river
# 
def find_high_card_odds(river):
	match river.max_rank_count:
		case 1:
			# 1st card rank can't match any card in river
			# 2nd card cant match 1st card or any card in river
			# odds for straight and flush must be subtracted
			odds_high_card = ((8/13) * (7/13)) - (find_straight_odds(river) + find_flush_odds(river)) # subtract straight_odds and flush_odds
		case _:
			# impossible, every hand will be > high card by default
			odds_high_card = 0.0

	return odds_high_card


# 
# Calculate the odds for any hand to be a pair given a river
# 
def find_pair_odds(river):
	match river.max_rank_count:
		case 1:
			# Scenario 1 (can be reversed so must * 2):
			# 	1st card rank must match one card in the river
			# 	2nd card cannot be any river card or the first card
			# Scenario 2:
			# 	1st card rank cannot be any rank that is in the river
			# 	2nd card rank must be the same as 1st card
			# subtract straight odds and flush odds
			odds_pair = (2 * (5/13) * (8/13)) + ((8/13) * (1/13))
		case 2:
			# 1st card rank can't be the same as any in the river
			# 2nd card rank can't be the same as any in the river or the 1st card
			# subtract straight odds and flush odds
			odds_pair = (9/13) * (8/13)
		case _:
			odds_pair = 0.0

	return odds_pair


# 
# Calculate the odds for any hand to be a two pair given a river
# 
def find_two_pair_odds(river):
	match river.max_rank_count:
		case 1:
			# 1st card rank must match one card in the river
			# 2nd card rank must match one card in the river that isn't the first card
			# subtract straight odds and flush odds
			odds_two_pair = (5/13) * (4/13)
		case 2:
			# ranks = (a, b, c, x, x)
			# Scenario 1:
			# 	1st card rank must match one card in the river that isn't x
			# 	2nd card rank cannot be x or 1st card rank
			# Scenario 2:
			# 	1st card rank can be anything but x
			# 	2nd card rank must be a, b, c, or 1st card
			# subtract straight odds and flush odds
			odds_two_pair = (2 * (3/13) * (11/13)) + ((3/13) * (1/13))
		case _:
			odds_two_pair = 0.0
	
	return odds_two_pair


# 
# Calculate the odds for any hand to be a 3 of a kind given a river
# 
def find_three_kind_odds(river):
	match river.max_rank_count:
		case 1:
			# 1st card rank must match one card in the river
			# 2nd card rank must be the same as the 1st card
			# subtract straight odds and flush odds
			odds_3_kind = (5/13) * (1/13)
		case 2:
			# ranks = (a, b, c, x, x)
			# 1st card rank matches x
			# 2nd card rank cannot be a, b, c, or x
			# subtract straight odds and flush odds
			odds_3_kind = 2 * (1/13) * (9/13)
		case 3:
			# ranks = (a, b, x, x, x)
			# 1st card can be anything except a, b, or x
			# 2nd card can be anything except a, b, x, or 1st card
			# subtract straight odds and flush odds
			odds_3_kind = (10/13) * (9/13)
		case _:
			odds_3_kind = 0.0
	
	return odds_3_kind


# 
# Calculate the odds for any hand to be a straight given a river
# 
def find_straight_odds(river):
	# straight odds
	# Calculate an array containing possible straights that can be formed.
	# Each of the possible straights requires 1 or 2 additional values for the straight to be satisfied.
	# Calculate the porobability of these values being in a player's hand for all possible straights in the array
	possible_straights = []
	for rank in river.ranks:
		# find cards in river that are in range = [rank, rank + 4]
		straight_cards = [x for x in river.ranks if x <= rank + 4 and x >= rank]
		straight_cards2 = [x for x in river.ranks if x <= rank + 3 and x >= rank - 1]
		straight_cards3 = [x for x in river.ranks if x <= rank + 2 and x >= rank - 2]

		# If there are at least 3 unique cards
		if(len(set(straight_cards)) >= 3 and rank >= 1 and rank + 4 <= 13):
			possible_straights.append(range(rank, rank + 5))
		if(len(set(straight_cards2)) >= 3 and rank - 1 >= 1 and rank + 3 <= 13):
			possible_straights.append(range(rank - 1, rank + 4))
		if(len(set(straight_cards3)) >= 3 and rank - 2 >= 1 and rank + 2 <= 13):
			possible_straights.append(range(rank - 2, rank + 3))


	possible_straights = list(set(possible_straights))

	odds_straight = 0.0

	cards_needed_list = []
	two_cards_needed_count = 0
	one_card_needed_count = 0

	min_cards_needed = 5
	for possible_straight in possible_straights:
		cards_needed = [x for x in possible_straight if x not in river.ranks]
		cards_needed_list.append(cards_needed)
		if len(cards_needed) < min_cards_needed:
			min_cards_needed = len(cards_needed)

	for cards_needed in cards_needed_list:
		if len(cards_needed) == 2:
			two_cards_needed_count += 1
		elif len(cards_needed) == 1:
			one_card_needed_count += 1


	
	for possible_straight in possible_straights:
		cards_needed = [x for x in possible_straight if x not in river.ranks]
		if len(cards_needed) == 2 and min_cards_needed == 2:
			odds_straight += 2 / (13 * 13)
		elif len(cards_needed) == 2 and min_cards_needed == 1 and two_cards_needed_count == 1:
			odds_straight += 1 / (13 * 13)
		elif len(cards_needed) == 2 and min_cards_needed == 1 and two_cards_needed_count == 2 and one_card_needed_count == 1:
			odds_straight += 1 / (13 * 13 * 2)
		elif len(cards_needed) == 1:
			odds_straight += 1 / 13
		elif len(cards_needed) == 0:
			odds_straight += 1
			break

	# subtract odds of flush, full house and 4 of a kind

	return odds_straight


# 
# Calculate the odds for any hand to be a flush given a river
# 
def find_flush_odds(river):
	# river_flush_count = tuple: (flush count, suit #)
	river_flush_count = river.get_flush_count()

	if river_flush_count[0] == 3:
		# first card same suit = 1/4 second card same suit 1/4
		# subtract odds of full house, 4 of a kind, and straight flush
		odds_flush = (1/4) * (1/4)
	elif river_flush_count[0] == 4:
		# first card same suit = 1/4 second card any suit 4/4
		# subtract odds of full house, 4 of a kind, and straight flush
		odds_flush = (1/4)
	elif river_flush_count[0] == 5:
		# any card any suit will result in a flush
		# subtract odds of full house, 4 of a kind, and straight flush
		odds_flush = 1.0
	else:
		odds_flush = 0.0

	return odds_flush


# 
# Calculate the odds for any hand to be a flush given a river
# 
def find_full_house_odds(river):
	match river.max_rank_count:
		case 2:
			# ranks = (a, b, c, x, x)
			# Scenario 1:
			# 	1st card rank matches x
			# 	2nd card rank matches a, b, or c
			# Scenario 2:
			# 	1st card rank matches a, b, or c
			# 	2nd card rank matches 1st card
			odds_full_house = (3 * (1/13) * (3/13))
		case 3:
			# ranks = (a, b, x, x, x)
			# 1st card rank must match a or b
			# 2nd card can be anything except 1st card and x
			odds_full_house = (2/13) * (11/13)
		case _:
			odds_full_house = 0.0
	
	return odds_full_house


# 
# Calculate the odds for any hand to be a 4 of a kind given a river
# 
def find_four_kind_odds(river):
	match river.max_rank_count:
		case 2:
			# ranks = (a, b, c, x, x)
			# 1st card rank must be x
			# 2nd card rank must be x
			odds_4_kind = (1/13) * (1/13)
		case 3:
			# ranks = (a, b, x, x, x)
			# 1st card rank must match x
			# 2nd card can be anything but x
			odds_4_kind = (1/13) * (12/13)
		case 4:
			# ranks = (a, x, x, x, x)
			# 1st card rank cannot be x
			# 2nd card rank cannot be x
			odds_4_kind = (12/13) * (12/13)
		case _:
			odds_4_kind = 0.0
	
	return odds_4_kind


# 
# Calculate the odds for any hand to be a straight flush given a river
# 
def find_straight_flush_odds(river):
	return 0.0

# 
# Find the odds of every type of hand given a river
# This is done assuming an infinite deck, for example the odds of getting an ace are always 4/52, not 3/51 once an ace is drawn
# 
def find_all_hand_types_odds(inputs):
	river = Hand(card_names_to_tuples(inputs["card_names"])["river"])

	odds = {
		'high_card': find_high_card_odds(river),
		'pair': find_pair_odds(river),
		'two_pair': find_two_pair_odds(river),
		'three_kind': find_three_kind_odds(river),
		'straight': find_straight_odds(river),
		'flush': find_flush_odds(river),
		'full_house': find_full_house_odds(river),
		'four_kind': find_four_kind_odds(river),
		'straight_flush': find_straight_flush_odds(river)
	}

	for key in odds:
		odds[key] = round(odds[key], 5)

	return odds



def find_odds_by_looping(inputs):
	hand_evals = []
	for suit1 in range(0, 4):
		for rank1 in range(1, 14):
			for suit2 in range(0, 4):
				for rank2 in range(1, 14):
					hand = [(suit1, rank1), (suit2, rank2)]
					cards = Hand(card_names_to_tuples(inputs["card_names"])["river"] + hand)
					eval = cards.evaluate_hand()
					hand_evals.append(eval)

	odds = {
		'high_card': len([x for x in hand_evals if x[0] == 'high card']) / len(hand_evals),
		'pair': len([x for x in hand_evals if x[0] == 'pair']) / len(hand_evals),
		'two_pair': len([x for x in hand_evals if x[0] == 'two pair']) / len(hand_evals),
		'three_kind': len([x for x in hand_evals if x[0] == '3 of a kind']) / len(hand_evals),
		'straight': len([x for x in hand_evals if x[0] == 'straight']) / len(hand_evals),
		'flush': len([x for x in hand_evals if x[0] == 'flush']) / len(hand_evals),
		'full_house': len([x for x in hand_evals if x[0] == 'full house']) / len(hand_evals),
		'four_kind': len([x for x in hand_evals if x[0] == '4 of a kind']) / len(hand_evals),
		'straight_flush': len([x for x in hand_evals if x[0] == 'straight flush']) / len(hand_evals)
	}

	for key in odds:
		odds[key] = round(odds[key], 5)
					

	return odds