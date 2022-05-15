from asyncore import loop
from odds import *
from hands import *
import time
import unittest


class TestOdds(unittest.TestCase):

	# -------------------------------------------------------------------------------------
	# 
	#	ALL UNIQUE CARDS IN RIVER
	# 
	# -------------------------------------------------------------------------------------

	# All unique cards in river and no possibility of straight or flush
	def test_unique_river_no_straight_or_flush(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['2 spades', '3 hearts', '7 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)

	
	# All unique cards in river with straight possibility - 3 in a row open ended
	def test_unique_river_three_consecutive_open(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '5 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# All unique cards in river with straight possibility - 3 in a row one ended
	def test_unique_river_three_consecutive_low_ace(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['ace spades', '2 hearts', '3 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# All unique cards in river with straight possibility - 3 with 1 card gap
	def test_unique_river_three_in_straight_one_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '6 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)



	# All unique cards in river with straight possibility - 3 with 2 card gap
	def test_unique_river_three_in_straight_two_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '7 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# All unique cards in river with straight possibility - 4 in a row open ended
	def test_unique_river_four_consecutive_open(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '5 clubs', '6 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# All unique cards in river with straight possibility - 4 in a row one ended
	def test_unique_river_four_consecutive_low_ace(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['ace spades', '2 hearts', '3 clubs', '4 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)



	# All unique cards in river with straight possibility - 4 with middle gap
	def test_unique_river_four_in_straight_with_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '6 clubs', '7 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)




	# -------------------------------------------------------------------------------------
	# 
	#	PAIR IN RIVER
	# 
	# -------------------------------------------------------------------------------------



	# Pair in river with no straight or flush possible
	def test_pair_river_no_straight_or_flush(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '9 clubs', '9 diamonds', 'queen spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# pair in river with straight possibility - 3 in a row open ended
	def test_pair_river_three_consecutive_open(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '5 clubs', '9 diamonds', '9 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# pair in river with straight possibility - 3 in a row one ended
	def test_pair_river_three_consecutive_low_ace(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['ace spades', '2 hearts', '3 clubs', '9 diamonds', '9 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# pair in river with straight possibility - 3 with 1 card gap
	def test_pair_river_three_in_straight_one_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '6 clubs', '9 diamonds', '9 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)



	# pair in river with straight possibility - 3 with 2 card gap
	def test_pair_river_three_in_straight_two_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '7 clubs', '9 diamonds', '9 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# pair in river with straight possibility - 4 in a row open ended
	def test_pair_river_four_consecutive_open(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '5 clubs', '6 diamonds', '4 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)


	# pair in river with straight possibility - 4 in a row one ended
	def test_pair_river_four_consecutive_low_ace(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['ace spades', '2 hearts', '3 clubs', '4 diamonds', '4 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)



	# pair in river with straight possibility - 4 with middle gap
	def test_pair_river_four_in_straight_with_gap(self):
		hand = ['5 diamonds', '10 hearts']
		river = ['3 spades', '4 hearts', '6 clubs', '7 diamonds', '3 spades']
		inputs = { 'stage': 'river', 'card_names': { 'hand': hand, 'river': river } }

		odds = find_all_hand_types_odds(inputs)
		looping_odds = find_odds_by_looping(inputs)

		self.assertEqual(odds, looping_odds)
		self.assertEqual(sum(odds.values()), 1)





	# -------------------------------------------------------------------------------------
	# 
	#	3 OF A KIND IN RIVER
	# 
	# -------------------------------------------------------------------------------------



	# -------------------------------------------------------------------------------------
	# 
	#	4 OF A KIND IN RIVER
	# 
	# -------------------------------------------------------------------------------------







if __name__ == "__main__":
	# TestOdds().test_pair_river_no_straight_or_flush()

	# run all tests
	unittest.main()