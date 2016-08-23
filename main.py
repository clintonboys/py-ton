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

match_score = MatchScore()
match = Match(0,0,0,0,0, ground, match_score)
bowler = Bowler(match, 0, 0, 0, 0, 0, 0, 0, 0)



## Main game loop

print '------------------------//-'
print 'Welcome to pyCricket--/--/-'
print '-- v0.1--------------/--/--'
print '--------------------/__/O--'

i = 0
j = 0

print '--- Set up your team ---'
team_choice = raw_input('(d)efault team...')
if team_choice == 'd':
	team = Team([Batsman(match, 0, 0, 1, {"name": "Clinton", "handedness": "left", "skill_multiplier": 1.7}) for i in range(0,11)], False)

while not match_score.is_over():

	user_action = raw_input('(f)ace the next ball, (d)eclare, (s)kip an over or e(x)it...| ')
	if user_action == 'x':
		print 'Thanks for playing.'
		sys.exit()
	elif user_action == 'd':
		match_score.declare()
	elif user_action == 'f': 
		print '===================='
		print '|| - Over ' + str(i+1) + '.' + str(j+1)
		print match_score
		print '===================='
		print match_score._scorecard
		result = match_score.check_result(match)	
		this_ball = Ball(match, match.innings(), i, j, team, bowler, team._players[match_score._scorecard[-1][0]], team._players[match_score._scorecard[-1][0]])
		this_ball.deliver()
	if j == 5:
		j = 0
		i += 1
	else:
		j += 1

print 'GAME OVER!!!'
print '===================='
print match_score
print '|| ' + str(result)
print '===================='
print 'Thanks for playing.'