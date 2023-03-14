import random

# add the matchups in order for this file to work
teams = ["Alabama", "AMCC/SMO", "Maryland", "West Virginia", "San Diego St", "Charleston", "Virginia", "Furman",
         "Creighton", "NC State", "Baylor", "UCSB", "Missouri", "Utah State", "Arizona", "Princeton",
         "Houston", "N Kentucky", "Iowa", "Auburn", "Miami", "Drake", "Indiana", "Kent State",
         "Iowa State", "MSST/Pitt", "Xavier", "Kennesaw St", "Texas A&M", "Penn State", "Texas", "Colgate",
         "Purdue", "TXSO/FDU", "Memphis", "FAU", "Duke", "Oral Roberts", "Tennessee", "Louisiana",
         "Kentucky", "Providence", "Kansas St", "Montana St", "Michigan St", "USC", "Marquette", "Vermont",
         "Kansas", "Howard", "Arkansas", "Illinois", "Saint Mary's", "VCU", "UConn", "Iona",
         "TCU", "ASU/Nev", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St", "UCLA", "UNC Asheville"]

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
