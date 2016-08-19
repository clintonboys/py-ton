from player import *


class Match(object):

	def __init__(self, day, session, session_over, innings, innings_over, ground, match_score):
		self._day = day
		self._session = session
		self._session_over = session_over
		self._innings = innings
		self._ground = ground
		self._match_score = match_score

class MatchScore(object):

	def __init__(self):
		self._scorecard = [[0,0],[0,0],[0,0],[0,0]]
		self._declared = [False, False, False, False]
		self._is_follow_on = [False, False, False, False]

	def wicket_taken(self):
		before_wicket = self._scorecard
		innings_number = len(before_wicket)
		wickets = before_wicket[innings_number - 1][0]
		runs = before_wicket[innings_number -  1][1]
		if self._declared[innings_number - 1] == False:
			wickets += 1
			self._scorecard[innings_number - 1][0] = wickets
		else:
			return None # error
		if wickets == 9 and innings_number:
			self._scorecard.append([0,0])


	def runs_scored(self, runs):
		innings_number = len(self._scorecard)
		self._scorecard[innings_number - 1][1] += runs

	def check_result(self):

		self._innings_number = len(self._scorecard)
		if self._innings_number < 3:
			if self._day == 5 and self._session == 3 and self._session_over
		elif self._

		first_team_total = self._scorecard[0][1] + self._scorecard[2][1]
