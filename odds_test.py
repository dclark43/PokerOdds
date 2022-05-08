from odds import *
from hands import *
import time


HANDS = ["high card", "pair", "two pair", "3 of a kind", "straight", "flush", "full house", "4 of a kind", "straight flush"]
SUITS = ["spade", "heart", "diamond", "club"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]


def test_pair():
	manual_input = False

	auto_run_stage = "river"
	hand_card1 = "5 hearts"
	hand_card2 = "9 hearts"
	river_card1 = "3 spades"
	river_card2 = "ten clubs"
	river_card3 = "5 diamonds"
	river_card4 = "king heart" # king heart
	river_card5 = "jack spade" # jack spade

	auto_run_hand = [hand_card1, hand_card2]
	auto_run_river = [river_card1, river_card2, river_card3, river_card4, river_card5]


	card_names = get_inputs(manual_input, auto_run_stage = auto_run_stage, auto_run_hand = auto_run_hand, auto_run_river = auto_run_river)


	(score, rank1, rank2) = find_hand_and_odds(card_names)

	return (score == "pair") and (rank1 == 5) and (rank2 == 13)










def main():


	if test_pair(): 
		print("PASSED ---------------- Pair") 
	else: 
		print("FAILED ---------------- Pair")










if __name__ == "__main__":
	main()