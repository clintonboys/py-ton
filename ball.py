'''
Class for an individual ball
'''

import scipy.stats
from player import *
import pymc as pm

class Ball(object):

    def __init__(self, match, innings, over, ball, 
    	         team, bowler, batsman_on_strike, batsman_off_strike):
    	self._match = match
        self._innings = innings     
        self._over = over  
        self._index = ball 
        self._team = team  
        self._bowler = bowler
        self._batsman_on_strike = batsman_on_strike
        self._batsman_off_strike = batsman_off_strike
        
    @property
    def innings(self):
        return self._innings

    def over(self):
        return self._over

    def index(self):
        return self._index

    def team(self):
        return self._team

    def bowler(self):
    	return self._bowler

    def batsman_on_strike(self):
    	return self._batsman_on_strike

    def batsman_off_strike(self):
    	return self._batsman_off_strike

    def runs_scored(self):
    	# weather_multiplier = decay(match_age)
    	# batsman_skill_multiplier 
    	# bowler_skill_multiplier
    	# batsman_fatigue_multiplier = decay(innings_age)
    	return pm.Poisson('a', 0.6).random()

    def wickets_taken(self):
    	return pm.Poisson('b', 0.07).random()
    	# prob of dismissal = Poisson
    	# batsman_skill_multiplier
    	# bowler_skill_multiplier
    	# type of dismissal

    def deliver(self):
    	if self.wickets_taken() > 0:
    		self._match._match_score.wicket_taken()
    		self._match._innings += 1
    	self._match._match_score.runs_scored(self.runs_scored())

	def __str__(self):
		return 'Over ' + str(self._over) + '.' + str(self._index)
