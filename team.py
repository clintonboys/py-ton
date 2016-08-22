class Team(object):

	def __init__(self, players, bats_first):
		self._players = players
		self._bats_first = bats_first

	@property
	def players(self):
	    return self._players

	@property
	def bats_first(self):
	    return self._bats_first