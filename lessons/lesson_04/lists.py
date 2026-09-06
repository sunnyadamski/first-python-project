games = ["Skyrim", "The Witcher 3", "Cyberpunk 2077", "Red Dead Redemption 2"]

print(games[0])  # Output: Skyrim
print(games[-1])  # Output: Red Dead Redemption 2

games.append("Horizon Zero Dawn")
games.remove("Cyberpunk 2077")

print(len(games))  # Output: 4

for game in games:
    print(game)

games.sort()
print(games)  # Output: ['Horizon Zero Dawn', 'Red Dead Redemption 2', 'Skyrim', 'The Witcher 3']
