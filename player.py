class Player(object):

	def __init__(self, batsman, bowler):

		self._batsman = batsman
		self._bowler = bowler

	def bowler(self):
		return self._bowler

	def batsman(self):
		return self._batsman
		## a player is just a pair of a batsman and bowler

		## print condition joins


# batsman_stats = {"name": Don Bradman,
# 		   "handedness": "left",
# 		   "skill_multiplier": 3.0 # In terms of batting averages, a batman with a skill multiplier of 1.0
# 		   							# should expect to have a batting average of 30.
# 		   }

class Batsman(object):

	def __init__(self, stats):
		self._runs = [0,0,0,0]
		self._is_out = [False, False, False, False]
		self._how_out = ['did not bat', 'did not bat', 'did not bat', 'did not bat']
		self._deliveries = [0,0,0,0]
		self._fours = [0,0,0,0]
		self._sixes = [0,0,0,0]
		self._minutes = [0,0,0,0]
		self._is_on_strike = False
		self._name = stats["name"]
		self._handedness = stats["handedness"]
		self._skill_multiplier = stats["skill_multiplier"]		

	@property
	
	def runs(self, innings = None):
		if innings:
			return self._runs[innings]
		else:
			return self._runs

	def is_out(self, innings = None):
		if innings:
			return self._is_out[innings]
		else:
			return self._is_out

	def how_out(self, innings = None):
		if innings:
			return self._how_out[innings]
		else:
			return self._how_out

	def deliveries(self, innings = None):
		if innings:
			return self._deliveries[innings]
		else:
			return self._deliveries

	def fours(self, innings = None):
		if innings:
			return self._fours[innings]
		else:
			return self._fours

	def sixes(self, innings = None):
		if innings:
			return self._sixes[innings]
		else:
			return self._sixes

	def minutes(self, innings = None):
		if innings:
			return self._minutes[innings]
		else:
			return self._minutes

	def is_on_strike(self):
		return self._is_on_strike

	def name(self):
		return self._name

	def handedness(self):
		return self._handededness

	def skill_multiplier(self):
		return self._skill_multiplier


class Bowler(object):
	def __init__(self, stats):
		self._over = [0,0,0,0]
		self._maidens = [0,0,0,0]
		self._runs = [0,0,0,0]
		self._wickets = [0,0,0,0]
		self._spell = 0
		self._spell_over = 0
		self._spell_maidens = 0
		self._spell_wickets = 0
		self._spell_runs = 0
		self._name = stats["name"]
		self._style = stats["style"]
		self._skill_multiplier = stats["skill_multiplier"]

	def overs(self):
		return self._over

