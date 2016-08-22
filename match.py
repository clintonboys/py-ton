from player import *


class Match(object):

	def __init__(self, day, session, session_over, innings, innings_over, ground, match_score):
		self._day = day
		self._session = session
		self._session_over = session_over
		self._innings = innings
		self._innings_over = innings_over
		self._ground = ground
		self._match_score = match_score

	@property
	def day(self):
	    return self._day

	def session(self):
		return self._session

	def session_over(self):
		return self._session_over

	def innings(self):
		return self._innings

	def innings_over(self):
		return self._innings_over

	def ground(self):
		return self._ground

	def match_score(self):
		return self._match_score


class MatchScore(object):

	def __init__(self):
		self._scorecard = [[0,0]]
		self._declared = [False]
		self._is_follow_on = [False]

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
		if wickets == 10 and innings_number:
			self._scorecard.append([0,0])
			self._declared.append(False)
			self._is_follow_on.append(False)


	def runs_scored(self, runs):
		innings_number = len(self._scorecard)
		self._scorecard[innings_number - 1][1] += runs

	def check_result(self):

		self._innings_number = len(self._scorecard)
		if self._day == 5 and self._session == 3 and self._session_over == 31:
			return 'draw'

		elif self._innings_number == 4:

			first_team_total = self._scorecard[0][1] + self._scorecard[2][1]
			second_team_total = self._scorecard[1][1] + self._scorecard[3][1]

			if first_team_total > second_team_total:
				return 'first_team_wins' 
				# work out how
			else:
				return None 

	def __str__(self):
		current_scorecard = self._scorecard
		innings_number = len(current_scorecard)
		print innings_number
		declared_add_list = []
		for i in range(0,innings_number):
			try:
				if self._declared[i]:
					declared_add_list.append(' (d)')
				else:
					declared_add_list.append('')
			except:
				declared_add_list = ''*innings_number
		if innings_number == 1:
			return 'A: ' + str(current_scorecard[0][0]) + '/' + str(current_scorecard[0][1]) + declared_add_list[0]
		elif innings_number == 2:
			return 'A: ' + str(current_scorecard[0][0]) + '/' + str(current_scorecard[0][1]) + declared_add_list[0] + '\n' + 'B: ' + str(current_scorecard[1][0]) + '/' + str(current_scorecard[1][1]) # + declared_add_list[1]
		elif innings_number == 3:
			if self._is_follow_on[2] == True:
				return 'A: ' + str(current_scorecard[0][0]) + '/' + str(current_scorecard[0][1]) + declared_add_list[0] + '\n' + 'B: ' + str(current_scorecard[1][0]) + '/' + str(current_scorecard[1][1]) + ' & ' + str(current_scorecard[2][0]) + '/' + str(current_scorecard[2][1]) + declared_add_list[2] + ' (f.o.)'
			else:
				return 'A: ' + str(current_scorecard[0][0]) + '/' + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' + str(current_scorecard[2][0]) + '/' + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + 'B: ' + str(current_scorecard[1][0]) + '/' + str(current_scorecard[1][1]) + declared_add_list[1]
		else:
			return 'A: ' + str(current_scorecard[0][0]) + '/' + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' + str(current_scorecard[2][0]) + '/' + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + 'B: ' + str(current_scorecard[1][0]) + '/' + str(current_scorecard[1][1]) + declared_add_list[1] + ' & ' + str(current_scorecard[3][0]) + '/' + str(current_scorecard[3][1]) + declared_add_list[3]





