from flask import Flask, render_template, request
from odds import *
from hands import *
import time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('main.html')



@app.route('/analyze', methods = ['POST'])
def analyze_cards():
	start_time = time.time()
	
	hand_card1 = request.form['hand_card1']
	hand_card2 = request.form['hand_card2']
	river_card1 = request.form['river_card1']
	river_card2 = request.form['river_card2']
	river_card3 = request.form['river_card3']
	river_card4 = request.form['river_card4']
	river_card5 = request.form['river_card5']

	# Determine stage based on how many cards are selected
	stage = ""
	if(hand_card1 and hand_card2):
		if(river_card1 and river_card2 and river_card3 and river_card4 and river_card5):
			stage = "river"
		elif(river_card1 and river_card2 and river_card3 and river_card4 and not river_card5):
			stage = "turn"
		elif(river_card1 and river_card2 and river_card3 and not river_card4 and not river_card5):
			stage = "flop"

		elif(not river_card1 and not river_card2 and not river_card3 and not river_card4 and not river_card5):
			stage = "preflop"

		else:
			print("Error: not a valid poker draw")


	hand = [hand_card1, hand_card2]
	river = [river_card1, river_card2, river_card3, river_card4, river_card5]
	my_hand = Hand(card_names_to_tuples({ 'hand': hand, 'river': river }))

	inputs = gather_inputs(stage = stage, hand = hand, river = river)

	# Returns a dictionary of odds for all types of hands: {'high card': high_card_odds, 'pair': pair_odds, ...}
	all_hand_types_odds = find_all_hand_types_odds(inputs)

	print("\n")
	print("My hand: ", hand)
	print("eval: ", my_hand.evaluate_hand())
	print("All hand types odds: ", all_hand_types_odds)
	print("sum of odds: ", str(sum(all_hand_types_odds.values())))

	end_time = time.time()
	print("total time (seconds) : ", str(end_time - start_time))
	print("\n")


	return render_template('results.html', hand = hand, river = river)


if __name__ == "__main__":
	app.run()












