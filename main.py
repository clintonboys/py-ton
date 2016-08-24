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
	teamA = Team([Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "DA Warner", "handedness": "left", "skill_multiplier": 2.1}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "AJ Finch", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "SPD Smith", "handedness": "left", "skill_multiplier": 2.6}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "GJ Bailey", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "MS Wade", "handedness": "left", "skill_multiplier": 1.9}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "MC Henriques", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "TM Head", "handedness": "left", "skill_multiplier": 1.3}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "JP Faulkner", "handedness": "left", "skill_multiplier": 1.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "MA Starc", "handedness": "left", "skill_multiplier": 0.8}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "A Zampa", "handedness": "left", "skill_multiplier": 0.6}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "NM Lyon", "handedness": "left", "skill_multiplier": 0.3}),], False)
	teamB = Team([Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "AD Hales", "handedness": "left", "skill_multiplier": 4.1}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "JJ Roy", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "JE Root", "handedness": "left", "skill_multiplier": 2.6}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "EJG Morgan", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "BA Stokes", "handedness": "left", "skill_multiplier": 1.9}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "JC Buttler", "handedness": "left", "skill_multiplier": 2.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "MM Ali", "handedness": "left", "skill_multiplier": 1.3}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "CR Woakes", "handedness": "left", "skill_multiplier": 1.0}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "AU Rashid", "handedness": "left", "skill_multiplier": 0.8}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "LE Plunkett", "handedness": "left", "skill_multiplier": 0.6}),
				  Batsman([0,0,0,0], [False, False, False, False], 1, {"name": "MA Wood", "handedness": "left", "skill_multiplier": 0.3}),], False)
teams = [teamA, teamB]
match_score = MatchScore()
match = Match(0,0,0,0,0, ground, match_score, teamA, teamB)
bowler = Bowler(match, 0, 0, 0, 0, 0, 0, 0, 0)
batsman_on_strike = teamA._players[0]
batsman_off_strike = teamA._players[1]
batting_team = teamA

while not match_score.is_over():

	user_action = raw_input('(f)ace the next ball, (d)eclare, (s)kip an over or e(x)it...| ')
	if user_action == 'x':
		print 'Thanks for playing.'
		sys.exit()
	elif user_action == 'd':
		match_score.declare()
		batting_team = teams[(teams.index(batting_team) +1)%2]
	elif user_action == 'f': 
		if match_score._scorecard[-1][0] == 10:
			batting_team = teams[(teams.index(batting_team) +1)%2]
			batsman_on_strike = batting_team._players[0]
			batsman_off_strike = batting_team._players[1]
			match_score._scorecard.append([0,0])
			match_score._declared.append(False)
			match_score._is_follow_on.append(False)
			print '=== INNINGS ' + str(len(match_score._scorecard)) + ' complete.'
		else:
			result = match_score.check_result(match)	
			this_ball = Ball(match, len(match_score._scorecard), over_no, ball_no, teams[len(match_score._scorecard)%2], bowler, batsman_on_strike, batsman_off_strike)
			this_ball.deliver()
			if this_ball._runs_scored%2 == 1:
				batsman_on_strike, batsman_off_strike = batsman_off_strike, batsman_on_strike
			if this_ball.wickets_taken() == 1 and match_score._scorecard[-1][0] < 10:
				batsman_on_strike._is_out[len(match_score._scorecard)-1] = True
				batsman_on_strike = batting_team._players[min([i for i in range(0,len(batting_team._players)) if not batting_team._players[i]._is_out[len(match_score._scorecard)-1] if i != batting_team._players.index(batsman_off_strike)])]
			print match_score._scorecard
			print '===================='
			print '|| - Over ' + str(over_no) + '.' + str(ball_no)
			print match_score.print_score()
			print '|| *' + batsman_on_strike._name + ' ' + str(batsman_on_strike._runs[len(match_score._scorecard)-1])
			print '||  ' + batsman_off_strike._name + ' ' + str(batsman_off_strike._runs[len(match_score._scorecard)-1])
			print '===================='


	if ball_no == 5:
		ball_no = 0
		over_no += 1
	else:
		ball_no += 1

print 'GAME OVER!!!'
print '===================='
print match_score.print_score(True, match)
print '|| ' + str(result)
print '===================='
print 'Thanks for playing.'