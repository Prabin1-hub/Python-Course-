games = []

while True:
    game = input("Enter your game or press to stop\n")
    if game == "":
        break
    else:
        games.append(game)

print("your favorite games: ")
for game in games:
    print(game)