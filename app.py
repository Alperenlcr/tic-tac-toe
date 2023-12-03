from flask import Flask, request, render_template, redirect, url_for
from database_ops import *

app = Flask(__name__)
app.debug = True

NAME = ""

# This is the main page
@app.route('/')
def entry():
    return render_template('entry.html')

# This is the page that shows the list of games
@app.route('/game_list', methods=['GET'])
def game_list():
    # This is a global variable that stores the name of the user
    global NAME
    # This is the name of the user
    t = request.args.get('name', '')
    # If the name is not empty, set the global variable to the name
    if t != "":
        NAME = t
        # If the name is not in the database, add it
        if append_name_to_csv(NAME):
            print(NAME, "added to database")

    # This is the name of the game
    game_name = request.args.get('game_name', '')
    # This is the color of the game
    game_color = request.args.get('color', '')

    # If the game name contains this string, remove the game from the database
    if '€removeTheGame£' in game_name:
        game_name = game_name.replace('€removeTheGame£', '')
        remove_game_from_csv(NAME, game_name, game_color)
        return render_template('game_list.html', name=NAME, games=find_games(NAME))

    # If the game name is not empty, add it to the database
    if game_name != "":
        append_name_to_csv(NAME, game_name, game_color)
        print(game_color, game_name, " added to ", NAME)
    return render_template('game_list.html', name=NAME, games=find_games(NAME))

# This is the page that shows the game
@app.route('/game', methods=['GET'])
def game():
    # This is the name of the game
    game_name = request.args.get('game_name', '')
    # This is the color of the game
    color = request.args.get('color', '')

    return render_template('game.html', game_name=game_name, color=color)

if __name__ == '__main__':
    app.run()
