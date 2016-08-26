## initiate a game through user input
## load saved players and statistics

## simulate ball after ball through four innings

## ball one returns:
	# number of runs scored, and how
	# wickets, if any, and how
	# information like the ball's speed etc

## the player has the option to change to different 
## players with different properties at various times
## throughout the game when this may be beneficial

## player stats:
	# bowling (spin)
	# bowling (fast)
	# batting
	# catching
	# handed-ness

from ball import Ball
from player import *
from match import Match, MatchScore
from team import Team
import sys

ground = None




## Main game loop

print '------------------------//-'
print 'Welcome to pyCricket--/--/-'
print '-- v0.1--------------/--/--'
print '--------------------/__/O--'

over_no = 0
ball_no = 0

print '--- Set up your team ---'
team_choice = raw_input('(d)efault team...')
if team_choice == 'd':
	teamA = Team([Player(Batsman({"name": "DA Warner", "handedness": "left", "skill_multiplier": 2.1}), Bowler({"name": "DA Warner", "style": "spin", "skill_multiplier": 0.5})),
				  Player(Batsman({"name": "AJ Finch", "handedness": "left", "skill_multiplier": 2.0}), Bowler({"name": "AJ Finch", "style": "spin", "skill_multiplier": 0.3})),
				  Player(Batsman({"name": "SPD Smith", "handedness": "left", "skill_multiplier": 2.6}), Bowler({"name": "SPD Smith", "style": "spin", "skill_multiplier": 0.6})),
				  Player(Batsman({"name": "GJ Bailey", "handedness": "left", "skill_multiplier": 2.0}), Bowler({"name": "GJ Bailey", "style": "spin", "skill_multiplier": 0.2})),
				  Player(Batsman({"name": "MS Wade", "handedness": "keeper", "skill_multiplier": 1.9}),Bowler({"name": "MS Wade", "style": "spin", "skill_multiplier": 0.1})),
				  Player(Batsman({"name": "MC Henriques", "handedness": "left", "skill_multiplier": 2.0}), Bowler({"name": "MC Henriques", "style": "fast", "skill_multiplier": 1.8})),
				  Player(Batsman({"name": "TM Head", "handedness": "left", "skill_multiplier": 1.3}), Bowler({"name": "TM Head", "style": "spin", "skill_multiplier": 1.1})),
				  Player(Batsman({"name": "JP Faulkner", "handedness": "left", "skill_multiplier": 1.0}), Bowler({"name": "JP Faulkner", "style": "fast", "skill_multiplier": 1.9})),
				  Player(Batsman({"name": "MA Starc", "handedness": "left", "skill_multiplier": 0.8}), Bowler({"name": "MA Starc", "style": "fast", "skill_multiplier": 1.8})),
				  Player(Batsman({"name": "A Zampa", "handedness": "left", "skill_multiplier": 0.6}), Bowler({"name": "A Zampa", "style": "fast", "skill_multiplier": 2.0})),
				  Player(Batsman({"name": "NM Lyon", "handedness": "left", "skill_multiplier": 0.3}), Bowler({"name": "NM Lyon", "style": "spin", "skill_multiplier": 2.1}))], False)
	teamB = Team([Player(Batsman({"name": "AD Hales", "handedness": "left", "skill_multiplier": 4.1}), Bowler({"name": "AD Hales", "style": "spin", "skill_multiplier": 0.1})),
				  Player(Batsman({"name": "JJ Roy", "handedness": "left", "skill_multiplier": 2.0}), Bowler({"name": "JJ Roy", "style": "spin", "skill_multiplier": 0.1})),
				  Player(Batsman({"name": "JE Root", "handedness": "left", "skill_multiplier": 6.6}), Bowler({"name": "JE Root", "style": "spin", "skill_multiplier": 0.6})),
				  Player(Batsman({"name": "EJG Morgan", "handedness": "left", "skill_multiplier": 2.0}), Bowler({"name": "EJG Morgan", "style": "spin", "skill_multiplier": 0.4})),
				  Player(Batsman({"name": "BA Stokes", "handedness": "left", "skill_multiplier": 1.9}), Bowler({"name": "BA Stokes", "style": "spin", "skill_multiplier": 1.2})),
				  Player(Batsman({"name": "JC Buttler", "handedness": "keeper", "skill_multiplier": 2.0}), Bowler({"name": "JC Buttler", "style": "fast", "skill_multiplier": 1.1})),
				  Player(Batsman({"name": "MM Ali", "handedness": "left", "skill_multiplier": 1.3}), Bowler({"name": "MM Ali", "style": "spin", "skill_multiplier": 1.7})),
				  Player(Batsman({"name": "CR Woakes", "handedness": "left", "skill_multiplier": 1.0}), Bowler({"name": "CR Woakes", "style": "fast", "skill_multiplier": 2.0})),
				  Player(Batsman({"name": "AU Rashid", "handedness": "left", "skill_multiplier": 0.8}), Bowler({"name": "AU Rashid", "style": "fast", "skill_multiplier": 2.1})),
				  Player(Batsman({"name": "LE Plunkett", "handedness": "left", "skill_multiplier": 0.6}), Bowler({"name": "LE Plunkett", "style": "fast", "skill_multiplier": 2.3})),
				  Player(Batsman({"name": "MA Wood", "handedness": "left", "skill_multiplier": 0.3}), Bowler({"name": "MA Wood", "style": "spin", "skill_multiplier": 1.9}))], False)
teams = [teamA, teamB]
match_score = MatchScore()
match = Match(0,0,0,0,0, ground, match_score, teams)
bowler = teamB._players[10].bowler()
batsman_on_strike = teamA._players[0].batsman()
batsman_off_strike = teamA._players[1].batsman()
batting_team = teamA

while not match_score.is_over():

	user_action = raw_input('(f)ace the next ball, (d)eclare, (s)kip an over or e(x)it...| ')
	if user_action == 'x':
		print 'Thanks for playing.'
		sys.exit()
	elif user_action == 'd':
		batsman_off_strike._how_out[len(match_score._scorecard)-1] = 'not out'
		batsman_on_strike._how_out[len(match_score._scorecard)-1] = 'not out'		
		match_score.declare()
		batting_team = teams[(teams.index(batting_team) +1)%2]
		batsman_on_strike = batting_team._players[0].batsman()
		batsman_off_strike = batting_team._players[1].batsman()
	elif user_action == 'f': 
		if match_score._scorecard[-1][0] == 10:
			batsman_off_strike._how_out[len(match_score._scorecard)-1] = 'not out'
			result = match_score.check_result(match)
			batting_team = teams[(teams.index(batting_team) +1)%2]
			batsman_on_strike = batting_team._players[0].batsman()
			batsman_off_strike = batting_team._players[1].batsman()
			if len(match_score._scorecard) < 4:
				match_score._scorecard.append([0,0])
				match_score._declared.append(False)
				match_score._is_follow_on.append(False)
			print '=== INNINGS ' + str(len(match_score._scorecard)-1) + ' complete.'
		else:
			result = match_score.check_result(match)	
			this_ball = Ball(match, len(match_score._scorecard), over_no, ball_no, teams[len(match_score._scorecard)%2], bowler, batsman_on_strike, batsman_off_strike)
			this_ball.deliver()
			if this_ball._runs_scored%2 == 1:
				batsman_on_strike, batsman_off_strike = batsman_off_strike, batsman_on_strike
			if this_ball.wickets_taken() == 1 and match_score._scorecard[-1][0] < 10:
				batsman_on_strike._is_out[len(match_score._scorecard)-1] = True
				batsman_on_strike._how_out[len(match_score._scorecard)-1] = this_ball._method_of_dismissal
				batsman_on_strike = batting_team._players[min([i for i in range(0,len(batting_team._players))\
				 if not batting_team._players[i].batsman()._is_out[len(match_score._scorecard)-1] \
				 if i != [player.batsman() for player in batting_team._players].index(batsman_off_strike)])].batsman()
			print match_score._scorecard
			print '===================='
			print '|| - Over ' + str(over_no) + '.' + str(ball_no)
			print match_score.print_score()
			if match_score._scorecard[-1][0] < 10:
				print '|| *' + batsman_on_strike._name + ' ' + str(batsman_on_strike._runs[len(match_score._scorecard)-1])
			print '||  ' + batsman_off_strike._name + ' ' + str(batsman_off_strike._runs[len(match_score._scorecard)-1])
			print '===================='


	if ball_no == 5:
		ball_no = 0
		over_no += 1
		change_bowler = raw_input('change bowler? (y/n)...| ')
		if change_bowler == 'y':
			bowler_menu = ''
			index = 0
			sorted_bowlers = sorted(teams[(teams.index(batting_team) +1)%2]._players, key=lambda x:x.bowler()._skill_multiplier, reverse = True)
			for player in sorted_bowlers:
				bowler_menu = bowler_menu + player.bowler()._name + ' (' + str(player.bowler()._skill_multiplier) + '): ' + str(index) + '\n'
				index += 1
			new_bowler_index = raw_input('Choose the new bowler...' + '\n' + bowler_menu)
			try:
				bowler = sorted_bowlers[int(new_bowler_index)].bowler()
			except:
				pass

	else:
		ball_no += 1

print 'GAME OVER!!!'
print '===================='
print match_score.print_score(True, match)
print '|| ' + str(result)
print '===================='
print 'Thanks for playing.'