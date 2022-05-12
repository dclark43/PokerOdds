from deck_of_cards import deck_of_cards
import itertools
from functools import cmp_to_key
import statistics
import time
import math

from hands import *


# 
# ************************** CONSTANTS **************************
# 
MANUAL_INPUT = False

AUTO_RUN_STAGE = "turn"
AUTO_RUN_HAND_CARD1 = "5 hearts"
AUTO_RUN_HAND_CARD2 = "9 hearts"
AUTO_RUN_RIVER_CARD1 = "3 spades"
AUTO_RUN_RIVER_CARD2 = "5 clubs"
AUTO_RUN_RIVER_CARD3 = "5 diamonds"
AUTO_RUN_RIVER_CARD4 = "king heart" # king heart
AUTO_RUN_RIVER_CARD5 = "" # jack spade

HAND = [AUTO_RUN_HAND_CARD1, AUTO_RUN_HAND_CARD2]
RIVER = [AUTO_RUN_RIVER_CARD1, AUTO_RUN_RIVER_CARD2, AUTO_RUN_RIVER_CARD3, AUTO_RUN_RIVER_CARD4, AUTO_RUN_RIVER_CARD5]

HANDS = ["high card", "pair", "two pair", "3 of a kind", "straight", "flush", "full house", "4 of a kind", "straight flush"]
SUITS = ["spade", "heart", "diamond", "club"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]





#
# Check if the string entered is a valid name of a card
#
def validate_card_name(card_name):
	suit_valid = False
	rank_valid = False

	for suit in SUITS:
		if(suit in card_name.lower()):
			suit_valid = True

	for rank in RANKS:
		if(rank in card_name.lower()):
			rank_valid = True

	return suit_valid and rank_valid



#
# Convert Dictionary of card names in english to corresponding suit and rank numbers formatted in tuples
#	
#		suit: 0 = spades, 1 = hearts, 2 = diamonds, 3 = clubs, 4 = joker
#		rank: 1 = Ace, 11 = Jack, 12 = Queen, 13 = King, 14 = B&W Joker, 15 = Color Joker
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


def initialize_deck(num_decks):
	deck_obj = deck_of_cards.DeckOfCards()

	for i in range(num_decks - 1):
		deck_obj.add_deck()

	return deck_obj






# Find all possible 2 card hands and check best hands and rank - return a list ordered by strength
def calculate_all_hands_odds(stage, cards):
	deck_obj = initialize_deck(1)
	sorted_hands = []

	hands = list(itertools.combinations(deck_obj.deck, 2))
	unique_hands = []


	for hand in hands:
		if(hand in unique_hands):
			continue
		else:
			unique_hands.append(hand)



	for hand in unique_hands:
		hand = [(hand[0].suit, hand[0].rank), (hand[1].suit, hand[1].rank)]
		cards_in_play = hand + cards

		(best_combo, best_combo_rank, high_card) = Hand(cards_in_play).evaluate_hand()

		sorted_hands.append((hand, best_combo, best_combo_rank, high_card))
		

	sorted_hands.sort(key = hand_compare_key)


	# print(sorted_hands)

	return sorted_hands




def hand_compare(a, b):
	if(HANDS.index(a[1]) > HANDS.index(b[1])):
		return 1
	elif(HANDS.index(a[1]) == HANDS.index(b[1])):
		if(a[2] > b[2] or a[2] == 1):
			return 1
		elif(a[2] == b[2]):
			if(a[3] > b[3] or a[3] == 1):
				return 1
			else:
				return -1
		else:
			return -1
	else:
		return -1


hand_compare_key = cmp_to_key(hand_compare)





#
# Find the odds of a particular hand with a river by comparing to every other possible hand
#
def calculate_my_hand_odds(stage, cards, all_hands): 
	deck_obj = initialize_deck(1)
	odds = 0

	if(stage == "preflop"):
		odds = calculate_preflop_odds(cards, deck_obj)
	elif(stage == "flop"):
		odds = calculate_flop_odds(cards, deck_obj)
	elif(stage == "turn"):
		odds = calculate_turn_odds(cards, deck_obj)
	elif(stage == "river"):
		odds = calculate_river_odds(cards, all_hands)




	return odds



def calculate_preflop_odds(cards, deck_obj):

	return

def calculate_flop_odds(cards, deck_obj):
	start_time = time.time()

	percentages = []
	possible_scores = {"high card": 0, 
						"pair": 0, 
						"two pair": 0, 
						"3 of a kind": 0, 
						"straight": 0, 
						"flush": 0, 
						"full house": 0, 
						"4 of a kind": 0, 
						"straight flush": 0}

	for card4 in deck_obj.deck:
		end_time = time.time()
		print("time (seconds): ", end_time - start_time)
		print("******************")
		for card5 in deck_obj.deck:
			print("----- " + str(card4.suit) + ", " + str(card4.rank) + " ----- " + str(card5.suit) + ", " + str(card5.rank) + " -----")
			river_cards = cards["river"] + [(card4.suit, card4.rank)] + [(card5.suit, card5.rank)]
			all_hands_sorted = calculate_all_hands_odds("flop", river_cards)
			
			cards_in_play = cards["hand"] + river_cards
			(best_combo, best_combo_rank, high_card) = Hand(cards_in_play).evaluate_hand()
			my_hand = (cards["hand"], best_combo, best_combo_rank, high_card)

			possible_scores[best_combo] += 1

			percentage = my_hand_percentage(my_hand, all_hands_sorted)
			percentages.append(percentage)

	possible_score_percentages = {"high card": (possible_scores["high card"] / 52) * 100,
								  "pair": (possible_scores["pair"] / 52) * 100,
								  "two pair": (possible_scores["two pair"] / 52) * 100,
								  "3 of a kind": (possible_scores["3 of a kind"] / 52) * 100,
								  "straight": (possible_scores["straight"] / 52) * 100,
								  "flush": (possible_scores["flush"] / 52) * 100,
								  "full house": (possible_scores["full house"] / 52) * 100,
								  "4 of a kind": (possible_scores["4 of a kind"] / 52) * 100,
								  "straight flush": (possible_scores["straight flush"] / 52) * 100}

	return (statistics.mean(percentages), possible_score_percentages)



def calculate_turn_odds(cards, deck_obj):
	percentages = []
	possible_scores = {"high card": 0, 
						"pair": 0, 
						"two pair": 0, 
						"3 of a kind": 0, 
						"straight": 0, 
						"flush": 0, 
						"full house": 0, 
						"4 of a kind": 0, 
						"straight flush": 0}

	for card in deck_obj.deck:
		river_cards = cards["river"] + [(card.suit, card.rank)]
		all_hands_sorted = calculate_all_hands_odds("turn", river_cards)
		
		cards_in_play = cards["hand"] + river_cards
		(best_score, best_score_rank, high_card) = Hand(cards_in_play).evaluate_hand()
		my_hand = (cards["hand"], best_score, best_score_rank, high_card)

		possible_scores[best_score] += 1

		percentage = my_hand_percentage(my_hand, all_hands_sorted)
		percentages.append(percentage)

	possible_score_percentages = {"high card": (possible_scores["high card"] / 52) * 100,
								  "pair": (possible_scores["pair"] / 52) * 100,
								  "two pair": (possible_scores["two pair"] / 52) * 100,
								  "3 of a kind": (possible_scores["3 of a kind"] / 52) * 100,
								  "straight": (possible_scores["straight"] / 52) * 100,
								  "flush": (possible_scores["flush"] / 52) * 100,
								  "full house": (possible_scores["full house"] / 52) * 100,
								  "4 of a kind": (possible_scores["4 of a kind"] / 52) * 100,
								  "straight flush": (possible_scores["straight flush"] / 52) * 100}


	return (statistics.mean(percentages), possible_score_percentages)



def calculate_river_odds(cards, all_hands):
	cards_in_play = cards["hand"] + cards["river"]

	(best_score, best_score_rank, high_card) = Hand(cards_in_play).evaluate_hand()
	my_hand = (cards["hand"], best_score, best_score_rank, high_card)

	return my_hand_percentage(my_hand, all_hands)



def my_hand_percentage(my_hand, all_hands):
	my_hand_reversed = ([my_hand[0][1], my_hand[0][0]], my_hand[1], my_hand[2], my_hand[3])
	my_hand_index = 0

	if(all_hands.count(my_hand) >= 1):
		my_hand_index = all_hands.index(my_hand)
	elif(all_hands.count(my_hand_reversed) >= 1):
		my_hand_index = all_hands.index(my_hand_reversed)
	else:
		print("error in my_hand_percentage: unable to find hand in list of possible hands")
		print(my_hand)
		return 0
	all_hands_length = len(all_hands)
	return ((my_hand_index) / all_hands_length) * 100





def get_inputs(stage = None, hand = None, river = None):
	inputs = {}

	card_names = {"hand": [card for card in hand if card != ""], "river": [card for card in river if card != ""]}
	inputs["card_names"] = card_names
	inputs["stage"] = stage


	return inputs




def find_hand_and_odds(inputs):
	# Start timer
	start_time = time.time()


	cards = card_names_to_tuples(inputs["card_names"])

	print("\n\n")
	print(cards)

	all_hands = calculate_all_hands_odds(inputs["stage"], cards["river"])
	# best_possible_hand = all_hands[-1]

	# best_hand_translated1 = RANKS[best_possible_hand[0][0][1] - 1] + " of " + SUITS[best_possible_hand[0][0][0] - 1]
	# best_hand_translated2 = RANKS[best_possible_hand[0][1][1] - 1] + " of " + SUITS[best_possible_hand[0][1][0] - 1]

	# print("\n\n")
	# print(best_possible_hand[1] + ": " + best_hand_translated1 + " and " + best_hand_translated2)
	# print("\n\n")
	# print(best_possible_hand)

	print("\n")

	my_hand = Hand(cards["hand"] + cards["river"]).evaluate_hand()
	my_hand_odds = calculate_my_hand_odds(inputs["stage"], cards, all_hands)


	end_time = time.time()
	print("total time (seconds) : ", str(end_time - start_time))
	print("\n")


	return my_hand, my_hand_odds



# This is done assuming an infinite deck, for example the odds of getting an ace are always 4/52, not 3/51 once an ace is drawn
def find_all_hands_odds_refactored(inputs):
	river = Hand(card_names_to_tuples(inputs["card_names"])["river"])
	river_ranks = river.get_ranks()
	river_suits = river.get_suits()

	# tuple: (flush count, suit #)
	river_flush_count = river.get_flush_count()


	if(inputs["stage"] == "river"):
		num_unique_hands = math.comb(52, 2)



		(score, rank1, rank2) = river.evaluate_hand()

		odds_straight_flush = 0
		odds_4_kind = 0
		odds_full_house = 0
		odds_flush = 0
		odds_straight = 0
		odds_3_kind = 0
		odds_two_pair = 0
		odds_pair = 0
		odds_high_card = 0
		total_odds = 0
		# if river has all different ranks (a, b, c, d, e)
		if len(set(river_ranks)) == 5:
			# straight-flush, flush, straight, or high card
			print("river cards all different ranks")

			# flush odds
			if river_flush_count[0] == 3:
				# first card same suit = 1/4 second card same suit 1/4
				odds_flush = (1/4) * (1/4)
			elif river_flush_count[0] == 4:
				# first card same suit = 1/4 second card any suit 4/4
				odds_flush = (1/4)
			elif river_flush_count[0] == 5:
				# any card any suit will result in a flush
				odds_flush = 1.0


			
			# both cards must be same rank as any card in the river
			# first card 20/52 since there are 5 possible cards to match in 4 different suits, second card 4/52 must match first card's rank
			odds_3_kind = (5/13) * (1/13)


			# straight odds
			# Calculate an array S containing possible straights that can be formed.
			# Each of the possible straights requires 1 or 2 additional values for the straight to be satisfied.
			# Calculate the porobability of these values being in a player's hand for all possible straights in the array
			possible_straights = []
			for rank in river_ranks:
				# find cards in river that are in range = [rank, rank + 4]
				straight_cards = [x for x in river_ranks if x <= rank + 4 and x >= rank]
				straight_cards2 = [x for x in river_ranks if x <= rank + 3 and x >= rank - 1]
				straight_cards3 = [x for x in river_ranks if x <= rank + 2 and x >= rank - 2]

				# If there are at least 3 unique cards
				if(len(set(straight_cards)) >= 3 and rank >= 1 and rank + 4 <= 13):
					possible_straights.append(range(rank, rank + 5))
				if(len(set(straight_cards2)) >= 3 and rank - 1 >= 1 and rank + 3 <= 13):
					possible_straights.append(range(rank - 1, rank + 4))
				if(len(set(straight_cards3)) >= 3 and rank - 2 >= 1 and rank + 2 <= 13):
					possible_straights.append(range(rank - 2, rank + 3))


			# print("possible straights: ", possible_straights)
			possible_straights = list(set(possible_straights))

			odds_straight = 0

			for possible_straight in possible_straights:
				cards_needed = [x for x in possible_straight if x not in river_ranks]
				if len(cards_needed) == 2:
					odds_straight += 1 / (13 * 13)
				elif len(cards_needed) == 1:
					odds_straight += 1 / 13
				elif len(cards_needed) == 0:
					odds_straight += 1

			odds_two_pair = (5/13) * (4/13)

			odds_pair = (5/13)

			odds_high_card = 1

			total_odds = (odds_straight_flush + odds_4_kind + odds_flush + odds_straight + odds_3_kind + odds_two_pair + odds_pair)

		# (a, b, c, x, x)
		elif score == "pair":
			# first card same rank as pair = 4/52, second card can be anything other than a, b, c, or x = 36/52
			# 	OR both cards are rank a, b, or c -> first card = 12/52 second card = 4/52
			odds_3_kind = ((1/13) * (9/13)) + ((3/13) * (1/13))

			if river_flush_count[0] == 3:
				# first card same suit = 1/4 second card same suit 1/4
				odds_flush = (1/4) * (1/4)
			elif river_flush_count[0] == 4:
				# first card same suit = 1/4 second card any suit 4/4
				odds_flush = (1/4)
			elif river_flush_count[0] == 5:
				# any card any suit will result in a flush
				odds_flush = 1.0

			# first card rank x = 4/52 second card rank a, b, or c = 12/52
			# 	OR both cards rank a, b, or c = 12/52 and 4/52
			odds_full_house = ((1/13) * (3/13)) + ((3/13) * (1/13))

			# first card same rank = 4/52, second card same rank = 4/52
			odds_4_kind = (1/13) * (1/13)

			# straight odds
			# Calculate an array S containing possible straights that can be formed.
			# Each of the possible straights requires 1 or 2 additional values for the straight to be satisfied.
			# Calculate the porobability of these values being in a player's hand for all possible straights in the array
			possible_straights = []
			for rank in river_ranks:
				# find cards in river that are in range = [rank, rank + 4]
				straight_cards = [x for x in river_ranks if x <= rank + 4 and x >= rank]
				straight_cards2 = [x for x in river_ranks if x <= rank + 3 and x >= rank - 1]
				straight_cards3 = [x for x in river_ranks if x <= rank + 2 and x >= rank - 2]

				# If there are at least 3 unique cards
				if(len(set(straight_cards)) >= 3 and rank >= 1 and rank + 4 <= 13):
					possible_straights.append(range(rank, rank + 5))
				if(len(set(straight_cards2)) >= 3 and rank - 1 >= 1 and rank + 3 <= 13):
					possible_straights.append(range(rank - 1, rank + 4))
				if(len(set(straight_cards3)) >= 3 and rank - 2 >= 1 and rank + 2 <= 13):
					possible_straights.append(range(rank - 2, rank + 3))


			# print("possible straights: ", possible_straights)
			possible_straights = list(set(possible_straights))

			odds_straight = 0

			for possible_straight in possible_straights:
				cards_needed = [x for x in possible_straight if x not in river_ranks]
				if len(cards_needed) == 2:
					odds_straight += 1 / (13 * 13)
				elif len(cards_needed) == 1:
					odds_straight += 1 / 13
				elif len(cards_needed) == 0:
					odds_straight += 1

			odds_two_pair = (3/13) * (11/13)

			odds_pair = (9/13) * (8/13)

			odds_high_card = 1

			total_odds = odds_straight_flush + odds_4_kind + odds_flush + odds_straight + odds_3_kind + odds_two_pair + odds_pair

		# (a, b, x, x, x)
		elif score == "3 of a kind":
			# both cards can be anything other than a, b, or x = 40/52
			odds_3_kind = (10/13) * (10/13)

			if river_flush_count[0] == 3:
				# first card same suit = 1/4 second card same suit 1/4
				odds_flush = (1/4) * (1/4)
			elif river_flush_count[0] == 4:
				# first card same suit = 1/4 second card any suit 4/4
				odds_flush = (1/4)
			elif river_flush_count[0] == 5:
				# any card any suit will result in a flush
				odds_flush = 1.0

			# first card rank a or b = 8/52, second card anything except rank x = 48/52
			odds_full_house = ((2/13) * (12/13))

			# first card same rank = 4/52, second card can be any other rank 48/52
			odds_4_kind = (1/13) * (12/13)


			# straight odds
			# Calculate an array S containing possible straights that can be formed.
			# Each of the possible straights requires 1 or 2 additional values for the straight to be satisfied.
			# Calculate the porobability of these values being in a player's hand for all possible straights in the array
			possible_straights = []
			for rank in river_ranks:
				# find cards in river that are in range = [rank, rank + 4]
				straight_cards = [x for x in river_ranks if x <= rank + 4 and x >= rank]
				straight_cards2 = [x for x in river_ranks if x <= rank + 3 and x >= rank - 1]
				straight_cards3 = [x for x in river_ranks if x <= rank + 2 and x >= rank - 2]

				# If there are at least 3 unique cards
				if(len(set(straight_cards)) >= 3 and rank >= 1 and rank + 4 <= 13):
					possible_straights.append(range(rank, rank + 5))
				if(len(set(straight_cards2)) >= 3 and rank - 1 >= 1 and rank + 3 <= 13):
					possible_straights.append(range(rank - 1, rank + 4))
				if(len(set(straight_cards3)) >= 3 and rank - 2 >= 1 and rank + 2 <= 13):
					possible_straights.append(range(rank - 2, rank + 3))


			# print("possible straights: ", possible_straights)
			possible_straights = list(set(possible_straights))

			odds_straight = 0

			for possible_straight in possible_straights:
				cards_needed = [x for x in possible_straight if x not in river_ranks]
				if len(cards_needed) == 2:
					odds_straight += 1 / (13 * 13)
				elif len(cards_needed) == 1:
					odds_straight += 1 / 13
				elif len(cards_needed) == 0:
					odds_straight += 1

			total_odds = odds_straight_flush + odds_4_kind + odds_flush + odds_straight + odds_3_kind + odds_two_pair + odds_pair

		# (a, x, x, x, x)
		elif score == "4 of a kind":
			# everything is 4 of a kind except for 5 of a kind
			odds_4_kind == 1.0 - (1/13)

			if river_flush_count[0] == 3:
				# first card same suit = 1/4 second card same suit 1/4
				odds_flush = (1/4) * (1/4)
			elif river_flush_count[0] == 4:
				# first card same suit = 1/4 second card any suit 4/4
				odds_flush = (1/4)
			elif river_flush_count[0] == 5:
				# any card any suit will result in a flush
				odds_flush = 1.0


		# (x, x, x, x, x)
		else:
			print("Not sure what goes here, 5 of a kind in the river??  Damn thats crazy bruh, I can't belive I actually covered this edge case!")





	print("high card: " + str(odds_high_card * 100) + ' %')
	print("pair: " + str(odds_pair * 100) + ' %')
	print("two pair: " + str(odds_two_pair * 100) + ' %')
	print("3 of a kind: " + str(odds_3_kind * 100) + ' %')
	print("straight: " + str(odds_straight * 100) + ' %')
	print("flush: " + str(odds_flush * 100) + ' %')
	print("full house: " + str(odds_full_house * 100) + ' %')
	print("4 of a kind: " + str(odds_4_kind * 100) + ' %')

	print("total odds: " + str(total_odds * 100) + ' %')
	# print(num_possible_hands)
	# print(num_4_kind / num_possible_hands)

		# 
		# for straight:
		# 	
		# if river is straight already:
		# 	every hand is a straight except for a flush
		# elif river has 4 cards within a 5 card range:
		# 	let first card in river be rank = n
		# 	every hand that contains the missing rank in range(5) is a straight
		# elif river has 3 cards within a 5 card range:
		# 	let first card in river be rank = n
		# 	every hand that contains the missing 2 ranks in the 5-range is a straight
		# 
		# 
		# 
		# 
		# 3 of a kind:
		# 
		# if river has all unique ranks (a, b, c, d, e):
		# 	3 of a kind only when player has a pair of a, b, c, d, or e
		# 		p = p(first card a, b, c, d, e) * p(second card same as first card)
		# 		p = 		5/13				* 				1/13
		# 
		# else if river contains a pair of rank x (a, b, c, x, x)
		# 	3 of a kind if player has a pair of a, b, c or if player has one x and one non-x
		# 		p = p(first card a, b, c) * p(second card same as first card)		or 		p(first card x) * p(second card not x)
		# 		p = 		3/13		  * 			1/13						+			1/13		*		12/13
		# 
		# else if river contains 3 of a kind of rank x (a, b, x, x, x)
		# 	every hand is 3 of a kind
		# 		p = 1
		# 
		# 
		# 


	print(river.cards)



	return river








# ***********************************
# 			  MAIN METHOD 
# ***********************************
def main():

	inputs = get_inputs()

	find_hand_and_odds(inputs)

	











if __name__ == "__main__":
	main()