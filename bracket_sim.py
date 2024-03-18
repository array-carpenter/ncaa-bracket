import random

# add the matchups in order for this file to work
teams = ["UConn", "Stetson", "FAU", "Northwestern", "San Diego St", "UAB", "Auburn", "Yale",
         "BYU", "Duquesne", "Illinois", "Morehead St", "Washington St", "Drake", "Iowa State", "S Dakota St",
         "North Carolina", "HOW/WAG", "Mississippi St", "Michigan St", "Saint Mary's", "Grand Canyon", "Alabama", "Charleston",
         "Clemson", "New Mexico", "Baylor", "Colgate", "Dayton", "Nevada", "Arizona", "Long Beach St",
         "Houston", "Longwood", "Nebraska", "Texas A&M", "Wisconsin", "James Madison", "Duke", "Vermont",
         "Texas Tech", "NC State", "Kentucky", "Oakland", "Florida", "BOIS/COL", "Marquette", "Western Kentucky",
         "Purdue", "MTST/GRAM", "Utah State", "TCU", "Gonzaga", "McNeese", "Kansas", "Samford",
         "South Carolina", "Oregon", "Creighton", "Akron", "Texas", "UVA/CSU", "Tennessee", "St. Peter's"]

# game sim
def simulate_game(team1, team2):
    winner = random.randint(0, 1)
    if winner == 0:
        return team1
    else:
        return team2

# sim round
def simulate_round(teams):
    winners = []
    # matchups
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i+1]
        winner = simulate_game(team1, team2)
        winners.append(winner)
    return winners

# entire tournament output
rounds = 6
for i in range(rounds):
    if i == 0:
        print("Second Round", "------------------------------------")
    if i == 1:
        print("Round of 32", "------------------------------------")
    if i == 2:
        print("Sweet 16", "------------------------------------")
    if i == 3:
        print("Elite 8", "------------------------------------")
    if i == 4:
        print("Final 4", "------------------------------------")
    if i == 5:
        print("Final", "------------------------------------")
    teams = simulate_round(teams)
    for j in range(len(teams)):
        print("Game", j+1, "winner:", teams[j])
    print()

# Output the winner
print("Your Randomized 2023 NCAA Men's Tournament Winner is:", teams[0])
