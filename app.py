from flask import Flask, request, render_template, redirect, url_for
from utils import *

app = Flask(__name__)
app.debug = True

NAME = ""

@app.route('/')
def entry():
    return render_template('entry.html')

@app.route('/game_list', methods=['GET'])
def game_list():
    global NAME  # Use the global keyword to access the global variable

    t = request.args.get('name', '')
    print(NAME, t)
    if t != "":
        NAME = t
        if append_name_to_csv(NAME):
            print(NAME, "added to database")
    game_name = request.args.get('game_name', '')
    game_color = request.args.get('color', '')
    if game_name != "":
        append_name_to_csv(NAME, game_name, game_color)
        print(game_color, game_name, " added to ", NAME)
    return render_template('game_list.html', name=NAME, games=find_games(NAME))

@app.route('/game', methods=['GET'])
def game():
    game_name = request.args.get('game_name', '')
    color = request.args.get('color', '')
    return render_template('game.html', game_name=game_name, color=color)

if __name__ == '__main__':
    app.run()
