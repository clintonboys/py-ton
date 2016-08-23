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
		self._is_over = False

	def wicket_taken(self):
		before_wicket = self._scorecard
		innings_number = len(before_wicket) - 1
		wickets = before_wicket[innings_number][0]
		runs = before_wicket[innings_number][1]
		# if self._declared[innings_number] == False:
		# 	wickets += 1
		# 	self._scorecard[innings_number][0] = wickets
		# else:
		# 	self._declared[innings_number][0] = True
		# 	self._scorecard.append([0,0])
		# 	self._declared.append(False)
		# 	self._is_follow_on.append(False)
		print wickets
		if wickets < 10:
			self._scorecard[-1][0] += 1
		elif wickets == 10:
			self._scorecard.append([0,0])
			self._declared.append(False)
			self._is_follow_on.append(False)

	def declare(self):
		self._declared[-1] = True
		self._declared.append(False)
		self._scorecard.append([0,0])
		self._is_follow_on.append([False])

	def runs_scored(self, runs):
		innings_number = len(self._scorecard)
		self._scorecard[innings_number - 1][1] += runs

	def is_over(self):
		return self._is_over

	def check_result(self, match):

		self._innings_number = len(self._scorecard)
		if match._day == 5 and match._session == 3 and match._session_over == 31:
			return 'Match drawn.'

		elif self._innings_number >= 4:

			first_team_total = self._scorecard[0][1] + self._scorecard[2][1]
			second_team_total = self._scorecard[1][1] + self._scorecard[3][1]

			if self._scorecard[3][0] == 10:

				# team batting first wins
				if first_team_total > second_team_total:
					self._is_over = True
					return 'A won by ' + str(first_team_total - second_team_total) + ' runs.'

				elif first_team_total == second_team_total: 
					self._is_over = True
					return 'Match tied.'

			else:

				if second_team_total > first_team_total:
					self._is_over = True
					return 'B won by ' + str(10 - self._scorecard[3][0]) + ' wickets.'


	def __str__(self, full = False, match = None):
		if not full:
			current_scorecard = self._scorecard
			innings_number = len(current_scorecard)
			declared_add_list = []
			for i in range(0,innings_number):
				try:
					if self._declared[i]:
						declared_add_list.append(' (d)')
					else:
						declared_add_list.append('')
				except:
					declared_add_list = ''*innings_number
			is_ten_one = ''
			is_ten_two = ''
			is_ten_three = ''
			is_ten_four = ''
			if innings_number > 0:
				if current_scorecard[0][0] < 10:
					is_ten_one = str(current_scorecard[0][0]) + '/'
			if innings_number > 1:
				if current_scorecard[1][0] < 10:
					is_ten_two = str(current_scorecard[1][0]) + '/'
			if innings_number > 2:
				if current_scorecard[2][0] < 10:
					is_ten_three = str(current_scorecard[2][0]) + '/'
			if innings_number > 3:
				if current_scorecard[3][0] < 10:
					is_ten_four = str(current_scorecard[3][0]) + '/'



			if innings_number == 1:
				return '|| A: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0]
			elif innings_number == 2:
				return '|| A: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] \
			  + '\n' + '|| B: ' + is_ten_two + str(current_scorecard[1][1]) # + declared_add_list[1]
			elif innings_number == 3:
				if self._is_follow_on[2] == True:
					return '|| A: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] \
			      + '\n' + '|| B: ' + is_ten_two + str(current_scorecard[1][1]) + ' & ' + \
			      				      is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] + ' (f.o.)'
				else:
					return '|| A: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' \
					                + is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + \
					       '|| B: ' + is_ten_two + str(current_scorecard[1][1]) + declared_add_list[1]
			else:
				return '|| A: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' \
							    + is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + \
				       '|| B: ' + is_ten_two + str(current_scorecard[1][1]) + declared_add_list[1] + ' & ' \
				       	 		+ is_ten_four + str(current_scorecard[3][1]) + declared_add_list[3]

		else:
			if match:
				print '_A_(1st_inn._)_|_'
					       	 		





