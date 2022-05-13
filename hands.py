import collections

HANDS = ["high card", "pair", "two pair", "3 of a kind", "straight", "flush", "full house", "4 of a kind", "straight flush"]
SUITS = ["spade", "heart", "diamond", "club"]
RANKS = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

class Hand:

	# cards = n card list
	# 	[(suit1, rank1), (suit2, rank2), (suit3, rank3)]
	def __init__(self, cards):
		self.cards = cards
		self.suits = self.get_suits()
		self.ranks = self.get_ranks()
		self.rank_counts = self.get_rank_counts()
		self.max_rank_count = max(self.rank_counts.values())


	def get_suits(self):
		return [card[0] for card in self.cards]


	def get_ranks(self):
		return sort([card[1] for card in self.cards])


	def get_rank_counts(self):
		rank_counts = collections.defaultdict(int)
		for rank in self.ranks:
			rank_counts[rank] += 1
		return rank_counts


	def get_flush_count(self):
		suits = self.get_suits()

		suits_count = (0, -1)

		for suit in suits:
			if suits.count(suit) > suits_count[0]:
				suits_count = (suits.count(suit), suit)

		return suits_count


	def get_high_card(self):
		rank = self.get_ranks().index(max(self.get_ranks()))
		return rank



	def is_pair(self):
		pair_rank = 0
		for rank in self.get_ranks():
			if(self.get_ranks().count(rank) == 2):
				pair_rank = rank

		ranks = [rank for rank in self.get_ranks() if rank != pair_rank]

		if(len(ranks) == 0):
			return (False, 0, 0)

		high_card = max(ranks)
		
		if(pair_rank != 0):
			return ("pair", pair_rank, high_card)
		return (False, 0, 0)


	def is_two_pair(self):
		pair1_rank = 0
		pair2_rank = 0
		for rank in self.get_ranks():
			if(self.get_ranks().count(rank) == 2):
				pair1_rank = rank

		ranks = [rank for rank in self.get_ranks() if rank != pair1_rank]
		
		if(pair1_rank == 0):
			return (False, 0, 0)

		for rank in ranks:
			if(ranks.count(rank) == 2):
				pair2_rank = rank

		ranks = [rank for rank in self.get_ranks() if (rank != pair1_rank and rank != pair2_rank)]
		high_card = max(ranks)

		if(pair2_rank != 0):
			return ("two pair", max([pair1_rank, pair2_rank]), high_card)
		return (False, 0, 0)



	def is_three_of_a_kind(self):
		three_rank = 0
		for rank in self.get_ranks():
			if(self.get_ranks().count(rank) == 3):
				three_rank = rank

		ranks = [rank for rank in self.get_ranks() if rank != three_rank]
		if(len(ranks) == 0):
			return (False, 0, 0)

		high_card = max(ranks)
		
		if(three_rank != 0):
			return ("3 of a kind", three_rank, high_card)
		return (False, 0, 0)



	def is_straight(self):
		min_rank = 0
		max_rank = 0
		ranks = self.ranks
		# [2,5,6,7,9]
		'''for rank in ranks:
			if (rank + 1) in ranks and (rank + 2) in ranks and (rank + 3) in ranks and (rank + 4) in ranks:
				min_rank = rank
				max_rank = rank + 4'''
		for i in range(len(ranks) - 5):
			for j in range(i + 5):


		if min_rank != 0 and max_rank != 0:
			return ("straight", max_rank, max_rank)
		return (False, 0, 0)




	def is_flush(self):
		suits = self.get_suits()
		flush_suit = -1
		for suit in suits:
			if(suits.count(suit) == 5):
				flush_suit = suit
				break

		if(flush_suit == -1):
			return (False, 0, 0)

		flush_cards = []
		for card in self.cards:
			if(card[0] == flush_suit):
				flush_cards.append(card)

		max_rank = max([card[1] for card in flush_cards])

		return ("flush", max_rank, max_rank)



	def is_full_house(self):
		three_rank = 0
		pair_rank = 0
		for rank in self.get_ranks():
			if(self.get_ranks().count(rank) == 3):
				three_rank = rank

		if(three_rank == 0):
			return (False, 0, 0)

		ranks = [rank for rank in self.get_ranks() if rank != three_rank]

		for rank in ranks:
			if(ranks.count(rank) == 2):
				pair_rank = rank
			return ("full house", three_rank, pair_rank)
		return (False, 0, 0)



	def is_four_of_a_kind(self):
		four_rank = 0
		for rank in self.get_ranks():
			if(self.get_ranks().count(rank) == 4):
				four_rank = rank

		ranks = [rank for rank in self.get_ranks() if rank != four_rank]
		if(len(ranks) == 0):
			return (False, 0, 0)

		high_card = max(ranks)
		
		if(four_rank != 0):
			return ("4 of a kind", four_rank, high_card)
		return (False, 0, 0)








	def evaluate_hand(self):
		'''pair_rank = 0
		three_rank = 0
		four_rank = 0
		five_rank = 0
		ranks = self.get_ranks()
		suits = self.get_suits()

		high_card = 0
		best_score = ""'''

		# 
		# 2 2 5 5 5 7 9
		#

		'''for rank in ranks:
			rank_count = ranks.count(rank)
			if rank_count == 2:
				pair_rank = rank
				break
			elif rank_count == 3:
				three_rank = rank
				break
			elif rank_count == 4:
				four_rank = rank
				break
			elif rank_count == 5:
				five_rank = rank
				break'''

		rank_kinds = {
			1: eval_all_unique,
			2: eval_pair,
			3: eval_three_kind,
			4: eval_four_kind,
			5: eval_five_kind
		}

		def eval_all_unique(self):
			# Could be high card, straight, flush, or straight flush
			if self.max_rank_count == 1:
				return_tuple = ()
				straight = self.is_straight()
				flush = self.is_flush()

				if straight[0]:
					# print(straight)
					return_tuple = straight
				if flush[0]:
					# print(flush)
					return_tuple = flush
				if straight[0] and flush[0]:
					return_tuple = ("straight flush", straight[1], straight[2])

				if not straight[0] and not flush[0]:
					best_score = "high card"
					high_card = max(ranks)
					ranks.remove(high_card)
					return_tuple = ("high card", high_card, max(ranks))

				return return_tuple

		def eval_pair(self):
			# Check for two pair and full house and get high card, otherwise pair
			elif(pair_rank != 0):
				other_ranks = [rank for rank in ranks if rank != pair_rank]

				for rank in other_ranks:
					rank_count = other_ranks.count(rank)

					if(rank_count == 2):
						high_card = max([r for r in other_ranks if r != rank])
						return ("two pair", pair_rank, high_card)
					elif rank_count == 3:
						return ("full house", rank, pair_rank)


				high_card = max(other_ranks)
				return ("pair", pair_rank, high_card)

		def eval_three_kind(self):
			# Three of a kind or full house
			elif(three_rank != 0):
				other_ranks = [rank for rank in ranks if rank != three_rank]

				for rank in other_ranks:
					rank_count = other_ranks.count(rank)

					if(rank_count == 2):
						return ("full house", three_rank, rank)
					elif(rank_count == 3):
						return ("full house", max([three_rank, rank]), min([three_rank, rank]))

				high_card = max(other_ranks)
				return ("3 of a kind", three_rank, high_card)


		def eval_four_kind(self):
			# Four of a kind
			elif(four_rank != 0):
				other_ranks = [rank for rank in ranks if rank != four_rank]

				high_card = max(other_ranks)
				return ("4 of a kind", four_rank, high_card)


		def eval_five_kind(self):
			# Five of a kind
			elif(five_rank != 0):
				other_ranks = [rank for rank in ranks if rank != five_rank]

				high_card = max(other_ranks)
				return ("4 of a kind", five_rank, high_card)


		return rank_kinds[self.max_rank_count]()

		'''else:
			print("\nError: didn't capture score for some reason, check out this debugging info: \n\n")
			print("cards: ", self.cards)
			print("pair rank: ", pair_rank)
			print("3 rank: ", three_rank)
			print("4 rank: ", four_rank)
			print("5 rank: ", five_rank)
			print("ranks: ", ranks)
			print("suits: ", suits)

			print("high card: ", high_card)
			print("best score: ", best_score)

			return 0'''










