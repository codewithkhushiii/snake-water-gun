from flask import Flask, request, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    youstr = data.get("choice")
    
    youdict = {"s": 1, "w": -1, "g": 0}
    reversedict = {1: "snake", -1: "water", 0: "gun"}

    if youstr not in youdict:
        return jsonify({"error": "Invalid input"}), 400

    you = youdict[youstr]
    computer = random.choice([1, -1, 0])

    if you == computer:
        outcome = "draw"
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        outcome = "win"
    else:
        outcome = "lose"

    return jsonify({
        "you": reversedict[you],
        "computer": reversedict[computer],
        "outcome": outcome
    })

if __name__ == "__main__":
    app.run(debug=True)
