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
		self.suit_counts = self.get_suit_counts()
		self.ranks = self.get_ranks()
		self.rank_counts = self.get_rank_counts()
		self.max_rank_count = max(self.rank_counts.values())


	def get_suits(self):
		return [card[0] for card in self.cards]


	def get_suit_counts(self):
		suit_counts = collections.defaultdict(int)
		for suit in self.suits:
			suit_counts[suit] += 1
		return suit_counts


	def get_ranks(self):
		return sort([card[1] for card in self.cards])


	def get_rank_counts(self):
		rank_counts = collections.defaultdict(int)
		for rank in self.ranks:
			rank_counts[rank] += 1
		return rank_counts


	def get_flush_count(self):
		suits_count = (0, -1)
		for suit in self.suits:
			if self.suits.count(suit) > suits_count[0]:
				suits_count = (self.suits.count(suit), suit)
		return suits_count


	#
	# Return a list of n cards which have the highest ranks
	#
	def get_high_card(self, n):
		return list(self.rank_counts)[-n:]


	def is_two_pair(self):
		pairs = []
		high_card = 0
		for rank in self.rank_counts:
			if self.rank_counts[rank] == 2:
				pairs.append(rank)
			else:
				high_card = rank

		if len(pairs) > 1 and high_card != 0:
			return ("two pair", max([pairs[-1], pairs[-2]]), high_card)
		return (False, 0, 0)


	def is_straight(self):
		n = len(self.ranks)
		i = n - 1
		straight = []
		while i > 3:
			count = 0
			j = i - 1
			while j > i - 4:
				# Difference between adjacent indices is not 1
				if self.ranks[j] + 1 != self.ranks[j + 1]:
					i = j
					break
				count += 1
				j -= 1
			if count == 4:
				straight = self.ranks[j:i+1]

		if len(straight) > 0:
			return ("straight", straight[0], straight[-1])
		return (False, 0, 0)


	def is_flush(self):
		flush_suit = -1
		for suit in self.suit_counts:
			if self.suit_counts[suit] == 5:
				flush_suit = suit
				break

		if flush_suit == -1:
			return (False, 0, 0)

		flush_cards = []
		max_rank = 0
		for card in self.cards:
			if card[0] == flush_suit:
				max_rank = max(max_rank, card[1])
				flush_cards.append(card)

		return ("flush", max_rank, max_rank)


	def is_full_house(self):
		three_rank = 0
		pair_rank = 0
		for rank in self.rank_counts:
			if self.rank_counts[rank] == 3:
				three_rank = rank
			elif self.rank_counts[rank] == 2:
				pair_rank = rank

		if three_rank != 0 and pair_rank != 0:
			return ("full house", three_rank, pair_rank)
		return (False, 0, 0)


	#
	# Check for "n of a kind"
	#
	def is_n_of_a_kind(self, n):
		n_rank = 0
		high_card = 0
		for rank in self.rank_counts:
			if self.rank_counts[rank] == n:
				n_rank = rank 
			else:
				high_card = max(high_card, rank)

		if n_rank != 0 and high_card != 0:
			if n != 2:
				return (f"{n} of a kind", n_rank, high_card)
			else:
				return ("pair", n_rank, high_card)


	def evaluate_hand(self):
		rank_kinds = {
			1: eval_all_unique,
			2: eval_pair,
			3: eval_three_kind,
			4: eval_four_kind,
			5: eval_five_kind
		}

		def eval_all_unique(self):
			# Could be high card, straight, flush, or straight flush
			straight = self.is_straight()
			flush = self.is_flush()
			if straight[0] and not flush[0]:
				return straight
			elif not straight[0] and flush[0]:
				return flush
			elif straight[0] and flush[0]:
				return ("straight flush", straight[1], straight[2])
			else:
				high_cards = self.get_high_cards(2)
				return ("high card", high_cards[-1], high_cards[-2])


		def eval_pair(self):
			# Checking for full house
			full_house = self.is_full_house()
			if full_house[0]:
				return full_house
			# Checking for two pair
			two_pair = self.is_two_pair()
			if two_pair[0]:
				return two_pair 
			# Return high card and pair if full house and two pair were not found
			return self.is_n_of_a_kind(2)


		def eval_three_kind(self):
			# Checking for full house
			full_house = self.is_full_house()
			if full_house[0]:
				return full_house
			else:
				return self.is_n_of_a_kind(3)


		def eval_four_kind(self):
			return self.is_n_of_a_kind(4)


		def eval_five_kind(self):
			return self.is_n_of_a_kind(5)


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










