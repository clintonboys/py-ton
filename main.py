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

match_score = MatchScore()
match = Match(1, 1, 1, 1, 1, ground, match_score)
player = Batsman(match, 0, 0, 1, {"name": "Clinton",
								  "handedness": "left",
								  "skill_multiplier": 1.7})
team = Team([player, Batsman(), Batsman(),
			 Batsman(), Batsman(), Batsman(),
			 Batsman(), Batsman(), Batsman(),
			 Batsman(), Batsman()], False)

