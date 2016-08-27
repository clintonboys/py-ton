from player import *
from tabulate import tabulate
import numpy as np

class Match(object):

	def __init__(self, day, session, session_over, innings, innings_over, ground, match_score, teams):
		self._day = day
		self._session = session
		self._session_over = session_over
		self._innings = innings
		self._innings_over = innings_over
		self._ground = ground
		self._match_score = match_score
		self._teams = teams

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
		if wickets < 10:
			self._scorecard[-1][0] += 1

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

		elif self._innings_number == 3 and self._scorecard[2][0] == 0 and self._scorecard[2][1] == 0 and (self._scorecard[0][1] + self._scorecard[2][1]) < self._scorecard[1][1]:
			return 'Eng won by an innings and ' + str(self._scorecard[1][1] - self._scorecard[2][1] - self._scorecard[0][1]) + ' runs.'

		elif self._innings_number >= 4:

			first_team_total = self._scorecard[0][1] + self._scorecard[2][1]
			second_team_total = self._scorecard[1][1] + self._scorecard[3][1]

			if self._scorecard[3][0] == 10:

				# team batting first wins
				if first_team_total > second_team_total:
					self._is_over = True
					return 'Aus won by ' + str(first_team_total - second_team_total) + ' runs.'

				elif first_team_total == second_team_total: 
					self._is_over = True
					return 'Match tied.'

			else:

				if second_team_total > first_team_total:
					self._is_over = True
					return 'Eng won by ' + str(10 - self._scorecard[3][0]) + ' wickets.'


	def print_score(self, full = False, match = None):
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

		if not full:
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
				return '|| Aus: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0]
			elif innings_number == 2:
				return '|| Aus: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] \
			  + '\n' + '|| Eng: ' + is_ten_two + str(current_scorecard[1][1]) # + declared_add_list[1]
			elif innings_number == 3:
				if self._is_follow_on[2] == True:
					return '|| Aus: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] \
			      + '\n' + '|| Eng: ' + is_ten_two + str(current_scorecard[1][1]) + ' & ' + \
			      				      is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] + ' (f.o.)'
				else:
					return '|| Aus: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' \
					                + is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + \
					       '|| Eng: ' + is_ten_two + str(current_scorecard[1][1]) + declared_add_list[1]
			else:
				return '|| Aus: ' + is_ten_one + str(current_scorecard[0][1]) + declared_add_list[0] + ' & ' \
							    + is_ten_three + str(current_scorecard[2][1]) + declared_add_list[2] +  '\n' + \
				       '|| Eng: ' + is_ten_two + str(current_scorecard[1][1]) + declared_add_list[1] + ' & ' \
				       	 		+ is_ten_four + str(current_scorecard[3][1]) + declared_add_list[3]

		else:
			if match:

				## Batting stats

				batting_stats_table = []
				if innings_number > 0:
					if self._scorecard[0][0] == 10:
						total_first = sum([match._teams[0]._players[i].batsman()._runs[0] for i in range(0, self._scorecard[0][0] +1)])
					else:
						total_first = str(self._scorecard[0][0])+'/'+str(sum([match._teams[0]._players[i].batsman()._runs[0] for i in range(0, self._scorecard[0][0] +1)]))+' (d)'
					batting_stats_table.append(['Aus (1st inn.)', total_first             , '','' ,''  ,''])
					batting_stats_table.append(['--------------','--------------','R'         ,'B','4s','6s'])
					for i in range(0, self._scorecard[0][0] + 1):
						batting_stats_table.append([match._teams[0]._players[i].batsman()._name, match._teams[0]._players[i].batsman()._how_out[0],match._teams[0]._players[i].batsman()._runs[0],match._teams[0]._players[i].batsman()._deliveries[0],match._teams[0]._players[i].batsman()._fours[0],match._teams[0]._players[i].batsman()._sixes[0] ])
				if innings_number > 1:
					if self._scorecard[1][0] == 10:
						total_second = sum([match._teams[1]._players[i].batsman()._runs[1] for i in range(0, self._scorecard[1][0] +1)])
					else:
						total_second = str(self._scorecard[1][0])+'/'+str(sum([match._teams[1]._players[i].batsman()._runs[1] for i in range(0, self._scorecard[1][0] +1)]))+' (d)'
					batting_stats_table[0]+= ['Eng (1st inn.)',total_second,'','','','']
					batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
					for j in range(0, self._scorecard[1][0] + 1):
						try:
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._name)
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._how_out[1])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._runs[1])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._deliveries[1])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._fours[1])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._sixes[1])							
						except:
							batting_stats_table.append([match._teams[1]._players[j].batsman()._name])
				if innings_number > 2:
					if self._scorecard[2][0] == 10:
						total_third = sum([match._teams[0]._players[i].batsman()._runs[2] for i in range(0, self._scorecard[2][0] +1)])					
					else:
						total_third = str(self._scorecard[2][0]) +'/' +str(sum([match._teams[0]._players[i].batsman()._runs[2] for i in range(0, self._scorecard[2][0] +1)]))+' (d)'
					batting_stats_table[0] += ['Aus (2nd inn.)', total_third, '', '','','']
					batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
					for j in range(0, self._scorecard[1][0] + 1):
						try:
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._name)
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._how_out[2])
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._runs[2])
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._deliveries[2])
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._fours[2])
							batting_stats_table[j+2].append(match._teams[0]._players[j].batsman()._sixes[2])							
						except:
							batting_stats_table.append([match._teams[0]._players[j].batsman()._name])
				if innings_number > 3:
					if self._scorecard[3][0] == 10:
						total_fourth = sum([match._teams[1]._players[i].batsman()._runs[3] for i in range(0, self._scorecard[3][0] +1)])										
					else:
						total_fourth = str(self._scorecard[3][0])+'/'+str(sum([match._teams[1]._players[i].batsman()._runs[3] for i in range(0, self._scorecard[3][0] +1)]))
					batting_stats_table[0] += ['Eng (2nd inn.)',total_fourth,'','','','']
					batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
					for j in range(0, self._scorecard[1][0] + 1):
						try:
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._name)
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._how_out[3])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._runs[3])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._deliveries[3])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._fours[3])
							batting_stats_table[j+2].append(match._teams[1]._players[j].batsman()._sixes[3])
						except:
							batting_stats_table.append([match._teams[1]._players[j].batsman()._name])

				## Bowling stats

				bowling_stats_table = []

				bowling_stats_table.append(['Eng (1st inn.)', 'O', 'M', 'W', 'R'])

				if innings_number > 0:
					bowlers = [player.bowler() for player in match._teams[1]._players if player.bowler()._over[0] > 0.0]
					for i in range(0,11):
						try:
							bowling_stats_table.append([bowlers[i]._name, np.round(bowlers[i]._over[0],2), bowlers[i]._maidens[0], bowlers[i]._wickets[0], bowlers[i]._runs[0]])
						except:
							pass
				
				if innings_number > 1:
					bowling_stats_table[0] += ['Aus (1st inn.)', 'O', 'M', 'W', 'R']
					bowlers = [player.bowler() for player in match._teams[0]._players if player.bowler()._over[1] > 0.0]
					for i in range(0,len(bowlers)):
						try:
							bowling_stats_table[i+1] += [bowlers[i]._name, np.round(bowlers[i]._over[1],2), bowlers[i]._maidens[1], bowlers[i]._wickets[1], bowlers[i]._runs[1]]
						except:
							bowling_stats_table.append(['','','','','', bowlers[i]._name, np.round(bowlers[i]._over[1],2), bowlers[i]._maidens[1], bowlers[i]._wickets[1], bowlers[i]._runs[1]])

				if innings_number > 2:
					bowling_stats_table[0] += ['Eng (2nd inn.)', 'O', 'M', 'W', 'R']
					bowlers = [player.bowler() for player in match._teams[1]._players if player.bowler()._over[2] > 0.0]
					for i in range(0,len(bowlers)):
						try:
							if len(bowling_stats_table[i+1]) == 5:
								bowling_stats_table[i+1] += ['','','','','', bowlers[i]._name, np.round(bowlers[i]._over[2],2), bowlers[i]._maidens[2], bowlers[i]._wickets[2], bowlers[i]._runs[2]]
							elif len(bowling_stats_table[i+1]) == 10:
								bowling_stats_table[i+1] += [bowlers[i]._name, np.round(bowlers[i]._over[2],2), bowlers[i]._maidens[2], bowlers[i]._wickets[2], bowlers[i]._runs[2]]
						except:
							bowling_stats_table.append(['','','','','','','','','','', bowlers[i]._name, np.round(bowlers[i]._over[2],2), bowlers[i]._maidens[2], bowlers[i]._wickets[2], bowlers[i]._runs[2]])

				if innings_number > 3:
					bowling_stats_table[0] += ['Aus (2nd inn.)', 'O', 'M', 'W', 'R']
					bowlers = [player.bowler() for player in match._teams[0]._players if player.bowler()._over[3] > 0.0]
					for i in range(0,len(bowlers)):
						try:
							if len(bowling_stats_table[i+1]) == 5:
								bowling_stats_table[i+1] += ['','','','','','','','','','', bowlers[i]._name, np.round(bowlers[i]._over[3],2), bowlers[i]._maidens[3], bowlers[i]._wickets[3], bowlers[i]._runs[3]]
							elif len(bowling_stats_table[i+1]) == 10:
								bowling_stats_table[i+1] += ['','','','','',bowlers[i]._name, np.round(bowlers[i]._over[3],2), bowlers[i]._maidens[3], bowlers[i]._wickets[3], bowlers[i]._runs[3]]
							elif len(bowling_stats_table[i+1]) == 15:
								bowling_stats_table[i+1] += [bowlers[i]._name, np.round(bowlers[i]._over[3],2), bowlers[i]._maidens[3], bowlers[i]._wickets[3], bowlers[i]._runs[3]]								
						except:
							bowling_stats_table.append(['','','','','','','','','','','','','','','', bowlers[i]._name, np.round(bowlers[i]._over[2],2), bowlers[i]._maidens[3], bowlers[i]._wickets[3], bowlers[i]._runs[3]])

				return tabulate(batting_stats_table), tabulate(bowling_stats_table)					       	 		





