class Player(object):

	def __init__(self, batsman, bowler):

		self._batsman = batsman
		self._bowler = bowler
		## a player is just a pair of a batsman and bowler

		## print condition joins


# batsman_stats = {"name": Don Bradman,
# 		   "handedness": "left",
# 		   "skill_multiplier": 3.0 # In terms of batting averages, a batman with a skill multiplier of 1.0
# 		   							# should expect to have a batting average of 30.
# 		   }

class Batsman(object):

	def __init__(self, match, runs, is_out, is_on_strike, stats):
		self._match = match
		self._runs = runs
		self._is_out = is_out
		self._is_on_strike = is_on_strike
		self._name = stats["name"]
		self._handededness = stats["handedness"]
		self._skill_multiplier = stats["skill_multiplier"]

	@property
	def match(self):
	    return self._match
	
	def runs(self):
		return self._runs

	def is_out(self):
		return self._is_out

	def is_on_strike(self):
		return self._is_on_strike

	def handedness(self):
		return self._handededness

	def skill_multiplier(self):
		return self._skill_multiplier

class Bowler(object):
	def __init__(self, match, over, spell, spell_over, ball, wickets, spell_wickets, runs, spell_runs):
		self._match = match
		self._runs = runs
		self._wickets = wickets
