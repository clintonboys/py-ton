from ball import Ball
from player import *
from match import Match, MatchScore
from team import Team
from utils import parse_team_json, parse_match_json
import sys
import pymysql
import json
import os


def print_current_score_short_form(match):

	print '===================='
	print '|| - Over ' + str(match._session_over) + '.' + str(match._over_ball)
	print match._match_score.print_score()
	if match._match_score._scorecard[-1][0] < 10:
		print '|| *' + match._batsman_on_strike._name + ' ' + str(match._batsman_on_strike._runs[match._innings_number])
	print '||  ' + match._batsman_off_strike._name + ' ' + str(match._batsman_off_strike._runs[match._innings_number])
	print '===================='


def game_loop(match, database, conn, cursor, interactive = True):

	teamA = match._teams[0]
	teamB = match._teams[1]

	print '--- ' + teamA._name + ' won the toss and is batting first.'

	while not match._match_score.is_over():

		print_current_score_short_form(match)

		if match._over_ball == 0:
			user_action = raw_input('(f)ace the next ball, (d)eclare, (s)kip an over or e(x)it to menu...| ')
		else:
			user_action = raw_input('(f)ace the next ball, (d)eclare or e(x)it...| ')
		if user_action == 'x':
			print '---------------------------'
			print '----py-ton SIMULATOR ------'
			print '---------------------------'
			print '-(s)ave game---------------'
			print '-(l)oad game---------------'
			print '-e(x)it to main menu-------'
			print '(q)uit---------------------'
			print '---------------------------'
			user_sub_action = raw_input('--Choose your option.......')
			if user_sub_action == 's':
				match.to_json()
			elif user_sub_action == 'l':
				print 'TBD'
			elif user_sub_action == 'x':
				return True
			else:
				sys.exit()

		elif user_action == 'd':
			match.declare()

		elif user_action == 's':

			for i in range(0,6):
				print match.simulate_delivery(conn, database)

		elif user_action == 'f': 

			print match.simulate_delivery(conn, database)

		result = match._match_score.check_result(match)	
		
		conn.commit()

	print 'GAME OVER!!!'
	print '===================='
	print match._match_score.print_score(True, match)[0]
	print '|| ' + str(result)
	print '===================='
	print 'Bowling statistics'
	print match._match_score.print_score(True, match)[1]
	print 'Thanks for playing.'
	match.to_json()
	return True

