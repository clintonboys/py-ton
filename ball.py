'''
Class for an individual ball
'''

import scipy.stats
from player import *
import pymc as pm
import math
import random

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
    	
        wickets = pm.Poisson('b', 0.15).random()*self._bowler._skill_multiplier
        if wickets > 1:
    		self._wickets_taken = 1
    		determine_type = random.random()
    		if determine_type >= 0.0 and determine_type <= 0.4065:
    			catcher = random.choice([player.batsman() for player in self._match._teams[(self._match._teams.index(team)+1)%2]._players])
    			self._method_of_dismissal = 'c. ' + catcher._name + ' b. ' + bowler._name
    		elif determine_type <= (0.4065 + 0.1627):
    			keeper = [player.batsman() for player in self._match._teams[(self._match._teams.index(team)+1)%2]._players if player.batsman()._handedness == 'keeper'][0]
    			self._method_of_dismissal = 'c. ' + keeper._name + ' b. ' + bowler._name
    		elif determine_type <= (0.4065 + 0.1267 + 0.2143):
    			self._method_of_dismissal = 'b. ' + bowler._name
    		elif determine_type <= (0.4065 + 0.1267 + 0.2143 + 0.1430):
    			self._method_of_dismissal = 'lbw (b. ' + bowler._name + ')'
    		elif determine_type <= (0.4065 + 0.1267 + 0.2143 + 0.1430 + 0.0351):
    			fielder = random.choice([player.batsman() for player in self._match._teams[(self._match._teams.index(team)+1)%2]._players])
    			self._method_of_dismissal = 'run out (' + fielder._name + ')'
    		elif determine_type <= (0.4065 + 0.1267 + 0.2143 + 0.1430 + 0.0351 + 0.0203):
    			keeper = [player.batsman() for player in self._match._teams[(self._match._teams.index(team)+1)%2]._players if player.batsman()._handedness == 'keeper'][0]
    			self._method_of_dismissal = 'st. ' + keeper._name + ' (b. ' + bowler._name + ')'
    		else:
    			self._method_of_dismissal = 'hit wicket'
    	else:
    		self._wickets_taken = 0

    	# weather_multiplier = decay(match_age)
    	# batsman_skill_multiplier 
    	# bowler_skill_multiplier
    	# batsman_fatigue_multiplier = decay(innings_age)
    	if self._wickets_taken > 0:
    		self._runs_scored = 0
    	else:
    		self._runs_scored = int(math.ceil(pm.Poisson('a', 2.2).random()*self._batsman_on_strike._skill_multiplier))

        
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
    	return self._runs_scored

    def wickets_taken(self):
    	return self._wickets_taken

    def deliver(self):
    	self._batsman_on_strike._deliveries[self._innings-1] += 1
    	self._bowler._over[self._innings-1] += 1.0/6.0
    	if self.wickets_taken() > 0:
    		self._match._match_score.wicket_taken()
    		self._bowler._wickets[self._innings-1] += 1
    	else:
	    	self._match._match_score.runs_scored(self._runs_scored)
	    	self._batsman_on_strike._runs[self._innings-1] += self._runs_scored
	    	self._bowler._runs[self._innings -1] += self._runs_scored

	def __str__(self):
		return 'Over ' + str(self._over) + '.' + str(self._index)
