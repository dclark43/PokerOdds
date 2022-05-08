from flask import Flask, render_template, request
from odds import *
from hands import *

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main_page():
    return render_template('main.html')



@app.route('/analyze', methods = ['POST'])
def analyze_cards():
	
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


	print(stage)


	hand = [hand_card1, hand_card2]
	river = [river_card1, river_card2, river_card3, river_card4, river_card5]


	inputs = get_inputs(stage = stage, hand = hand, river = river)

	ah_odds_refactored = find_all_hands_odds_refactored(inputs)

	# my_hand, my_hand_odds = find_hand_and_odds(inputs)

	# return render_template('results.html', score = my_hand[0], rank1 = my_hand[1], rank2 = my_hand[2], percentage = my_hand_odds, hand = hand, river = river)
	return render_template('main.html')


if __name__ == "__main__":
	app.run()