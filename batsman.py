from ball import Ball

# batsman_stats = {"name": Don Bradman,
# 		   "handedness": "left",
# 		   "skill_multiplier": 3.0 # In terms of batting averages, a batman with a skill multiplier of 1.0
# 		   							# should expect to have a batting average of 30.
# 		   }

class Batsman(object):

	def __init__(self, match, score, is_out, is_on_strike, stats):
		self._match = match
		self._score = score
		self._is_out = is_out
		self._is_on_strike = is_on_strike
		self._name = stats["name"]
		self._handededness = stats["handedness"]
		self._skill_multiplier = stats["skill_multiplier"]

	@property
	def match(self):
	    return self._match
	
	def score(self):
		return self._score

	def is_out(self):
		return self._is_out

	def is_on_strike(self):
		return self._is_on_strike

	def handedness(self):
		return self._handededness

	def skill_multiplier(self):
		return self._skill_multiplier

	