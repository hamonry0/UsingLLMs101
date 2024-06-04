from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(user_choice, computer_choice)
        return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == '__main__':
    app.run(debug=True)
    