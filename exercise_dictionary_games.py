games = [
    {"name": "PUBG", "editor": "prabin", "year": 2018 }

]

new_game = {

    "name": input("enter the game name: \n"),
    "editor": input("enter the editor: \n"),
    "year": input("enter the year: \n")

}

games.append(new_game)

for game in games:
    print("game :",game["name"])