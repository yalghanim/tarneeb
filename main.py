from modules import Player
import random, operator

print("\n\nAhlan in Qaid Tarneeb v1")
print("\n~~~ 4-6 Players, No score limit, 5-6 players: >=6 talbat are double ~~~")

#counts how many players are playing(only take values between 4-6)
while True:
	num_players = input("\nCham wa7id eb yil3ab elyoum? [4, 5, or 6] ")
	if num_players in {'4', '5', '6'}:
		num_players = int(num_players)
		break
	else:
		continue

#established the score limit for the game, only takes integers
while True:
    try:
        scorelimit = int(input("\nLay cham eb til3ibon elyoum? "))
        break
    except ValueError:
        print("3a6ny raqam!!!")

#creates instances of players from the class Player
player1 = (Player(input("\n1st Player? ").lower(),0))
player2 = (Player(input("2nd Player? ").lower(),0))
player3 = (Player(input("3rd Player? ").lower(),0))
player4 = (Player(input("4th Player? ").lower(),0))
if num_players == 5:
	player5 = (Player(input("5th Player? ").lower(),0))
elif num_players == 6:
	player5 = (Player(input("5th Player? ").lower(),0))
	player6 = (Player(input("6th Player? ").lower(),0))

#welcome message for players
print ("Ahlan ", end=" ")
for player in Player.instances:
	print(player.name, end=", ")
print("...Yalla khanbalish!!!")

#adds players(K) to dictionary and starts scores(V) with 0
players = {}
for instance in Player.instances:
	players[instance.name] = instance.score

#randomly predicts who's going to win, and who deals first
print("\nShakla  " + random.choice(list(players.keys())).upper() + "  bifouz elyoum..\n")
print("\nw tara  " + random.choice(list(players.keys())).upper() + "  ywazi3 \n")

#adds a tally of players(K) & their talbat(V) to a dictionary, starts score with 0
talbat = {}
for instance in Player.instances:
	talbat[instance.name] = instance.score

#if talbat exceeds 9, then there will be losers for sure, hence 'hamya'
def hamya():
	if sum(talbat.values()) > 9:
		print("\n oh hal li3ba 7amya!!\n")
	else:
		pass

#tells you each player's talba
def talbattell():
	for k,v in sorted(talbat.items(), key=operator.itemgetter(1), reverse=True):
		print("\t" + k + " talib " + str(v) + " talbat")

#tells you the players' scores
def scoretell():
	print("\nScorat:")
	for k,v in sorted(players.items(), key=operator.itemgetter(1), reverse=True):
		print("\t" + k + " score is:\t" + str(v))

#tells you who's winning
def winning():
	winning = max(players, key=players.get)  
	print("\teli3ib 3ala:\t" + winning.upper())

#tells you who's losing
def losing():
	losing = min(players, key=players.get) 
	print("\t" + losing.upper() + " ysheel\n")

#establishes talbat for each player
def handtalba():
	for player, talba in talbat.items():
		while True:
			new_talba = input("\n" + player.upper() + " cham talib?  ")
			if new_talba in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
				new_talba = int(new_talba)
				talba = new_talba
				talbat[player]=talba
				break
			else:
				print("mn 1 lay 9")
				continue
	hamya()
	talbattell()

"""game engine; score calculator and tally, 
based on # of players and their respective talbat"""
def handscore():
	for player, score in players.items():
		while True:
			yabha = input("\t" + player + " yabha? [Y or N] ")
			yabha = yabha.lower()
			if yabha == ('y'):
				if num_players >= 5 and talbat.get(player) >= 6:
					amount = (talbat.get(player)) * 10 * 2
					score = score + amount
					players[player]=score
					print("\n kibeer ya  " + player + "!!\n")
					break
				elif num_players <= 4 and talbat.get(player) >= 7:
					amount = (talbat.get(player)) * 10 * 2
					score = score + amount
					players[player]=score
					print("\n kibeer ya  " + player + "!!\n")
					break
				else:
					amount = (talbat.get(player)) * 10
					score = score + amount
					players[player]=score
					break
			elif yabha == ('n'):
				amount = (talbat.get(player)) * 10
				score = score - amount
				players[player]=score
				break
			else:
				print("print Y or N (capitalization doesn't matter)")
				continue
	scoretell()

#function to accumulate all hand dealing functions together
def hand():
	handtalba()
	print("\n")
	handscore()
	print("\n")

"""main function; builds on all previous functions and sets the flow of the game. 
	If one player exceeds the scorelimit set above,
	the game will stop and winner will be announced"""
def game():
	pinnacle = 0
	while True:
		hand()
		for player in players:
			if players.get(player) > scorelimit:
				pinnacle += 1
			else:
				pass
		if pinnacle >= 1:
			winner = max(players, key=players.get)
			print("\n\t*** mabrooook  " + winner.upper() + "!!!  ***\n\n")
			break
		else:
			losing()
			winning()
			continue

game()




