from operator import attrgetter

class Team(object):

	def __init__(self, name, short_name, players, bats_first):
		self._players = players
		self._bats_first = bats_first
		self._name = name
		self._short_name = short_name

	@property
	def players(self):
	    return self._players

	@property
	def bats_first(self):
	    return self._bats_first

	def choose_bowler(self, current_bowler, choose = False):
		if not choose:
			# return the highest skilled bowler
			# with the least amount of overs bowled
			# who is not the current bowler
			min_overs = min([player.bowler().overs() for player in self._players])
			candidates = [player.bowler() for player in self._players if player.bowler().overs() == min_overs if player.bowler() != current_bowler]
			return candidates.sort(key = lambda x: x.skill_multiplier())
		else:
			return self._players[i].bowler()