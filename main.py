from ball import Ball
from player import *
from match import Match, MatchScore
from team import Team
from utils import parse_team_json, parse_match_json
import sys
import pymysql

## Main game loop

print '------------------------//-'
print 'Welcome to pyCricket--/--/-'
print '-- v0.1--------------/--/--'
print '--------------------/__/O--'

print '--- Set up your team ---'
match, match_score = parse_match_json('match1.json')
team_choice = raw_input('(d)efault team...')
if team_choice == 'd':
	teams = match._teams
	teamA = teams[0]
	teamB = teams[1]

print '--- ' + teams[0]._name + ' won the toss and is batting first.'

bowler = teamB._players[10].bowler()
batsman_on_strike = teamA._players[0].batsman()
batsman_off_strike = teamA._players[1].batsman()
batting_team = teamA
ball_no = 0 
over_no = 0
session_over_no = 0
over_runs = 0

def delivery(over_runs, match, over_no, ball_no, bowler, batsman_on_strike, batsman_off_strike, cursor):

	this_ball = Ball(match, len(match_score._scorecard), over_no, ball_no, teams[len(match_score._scorecard)%2], bowler, batsman_on_strike, batsman_off_strike)
	this_ball.deliver()
	over_runs += this_ball._runs_scored
	batsman_on_strike._deliveries[len(match_score._scorecard)-1] += 1
	batsman_on_strike._minutes[len(match_score._scorecard)-1] += 3
	if this_ball._runs_scored%2 == 1:
		batsman_on_strike, batsman_off_strike = batsman_off_strike, batsman_on_strike
	if this_ball._runs_scored == 4:
		batsman_on_strike._fours[len(match_score._scorecard)-1] += 1
	if this_ball._runs_scored == 6:
		batsman_on_strike._sixes[len(match_score._scorecard)-1] += 1
	wickets_taken_this_ball = this_ball.wickets_taken()
	if wickets_taken_this_ball == 1 and match_score._scorecard[-1][0] < 10:
		batsman_on_strike._is_out[len(match_score._scorecard)-1] = True
		batsman_on_strike._how_out[len(match_score._scorecard)-1] = this_ball._method_of_dismissal
		batsman_on_strike = batting_team._players[min([i for i in range(0,len(batting_team._players))\
		 if not batting_team._players[i].batsman()._is_out[len(match_score._scorecard)-1] \
		 if i != [player.batsman() for player in batting_team._players].index(batsman_off_strike)])].batsman()

	if wickets_taken_this_ball > 0:
		is_wickets = True
		dismissal = this_ball._method_of_dismissal
	else:
		is_wickets = False
		dismissal = ''
	query = '''INSERT INTO clinton.ball_history (match_home_team, match_away_team, match_ground, match_start_date, match_end_date, match_day, match_innings, innings_wickets_down, innings_runs, innings_batting_team, innings_bowling_team, day_session, session_over, over_ball, batsman_on_strike, batsman_off_strike, bowler, keeper, field, ball_runs_scored, ball_extras_scored, ball_extras_reason, wicket_taken, wicket_reason, wicket_catcher)
		VALUES ({0}, {1}, \'{2}\', \'{3}\',\'{4}\', {5}, 
			    {6}, {7}, {8},
			    {9}, {10},
			    {11}, {12}, {13}, \'{14}\', \'{15}\', \'{16}\', "", 
			    "", {17} , 0, "", {18}, \'{19}\', "");'''.format(teams[0]._id, teams[1]._id, 1, '2016-12-26', '2016-12-30', match._day, match._innings, match_score._scorecard[match._innings][0], match_score._scorecard[match._innings][1], batting_team._id, match._teams[(match._teams.index(batting_team)+1)%2]._id, match._session, match._session_over, ball_no, batsman_on_strike._name, batsman_off_strike._name, bowler._name, this_ball._runs_scored, is_wickets, dismissal)
	print query
	cursor.execute(query)
	return batsman_on_strike, batsman_off_strike, over_runs

def prompt_change_bowler(current_bowler):

	change_bowler = raw_input('change bowler? (y/n)...| ')
	if change_bowler == 'y':
		bowler_menu = ''
		index = 0
		sorted_bowlers = sorted(teams[(teams.index(batting_team) +1)%2]._players, key=lambda x:x.bowler()._skill_multiplier, reverse = True)
		for player in sorted_bowlers:
			bowler_menu = bowler_menu + player.bowler()._name + ' (' + str(player.bowler()._skill_multiplier) + '): ' + str(index) + '\n'
			index += 1
		new_bowler_index = raw_input('Choose the new bowler...' + '\n' + bowler_menu)
		try:
			return sorted_bowlers[int(new_bowler_index)].bowler()
		except:
			return current_bowler
	else:
		return current_bowler

def print_current_score_short_form(over_no, ball_no, match_score, batsman_on_strike, batsman_off_strike):

	print '===================='
	print '|| - Over ' + str(over_no) + '.' + str(ball_no)
	print match_score.print_score()
	if match_score._scorecard[-1][0] < 10:
		print '|| *' + batsman_on_strike._name + ' ' + str(batsman_on_strike._runs[len(match_score._scorecard)-1])
	print '||  ' + batsman_off_strike._name + ' ' + str(batsman_off_strike._runs[len(match_score._scorecard)-1])
	print '===================='


while not match_score.is_over():
	conn = pymysql.connect(host = 'localhost',port = 3306, user='root')
	cursor = conn.cursor()
	if ball_no == 0:
		user_action = raw_input('(f)ace the next ball, (d)eclare, (s)kip an over or e(x)it...| ')
	else:
		user_action = raw_input('(f)ace the next ball, (d)eclare or e(x)it...| ')
	if user_action == 'x':
		print 'Thanks for playing.'
		sys.exit()
	elif user_action == 'd':

		batsman_off_strike._how_out[len(match_score._scorecard)-1] = 'not out'
		batsman_on_strike._how_out[len(match_score._scorecard)-1] = 'not out'		
		match_score.declare()
		batting_team = teams[(teams.index(batting_team) +1)%2]
		batsman_on_strike = batting_team._players[0].batsman()
		batsman_off_strike = batting_team._players[1].batsman()

	elif user_action == 's':

		for i in range(0,6):
			batsman_on_strike, batsman_off_strike, over_runs = delivery(over_runs, match, over_no, i, bowler, batsman_on_strike, batsman_off_strike, cursor)
		batsman_on_strike, batsman_off_strike = batsman_off_strike, batsman_on_strike			
		print_current_score_short_form(over_no, ball_no, match_score, batsman_on_strike, batsman_off_strike)
		ball_no = 0
		over_no += 1
		session_over_no += 1
		if over_runs == 0:
			bowler._maidens[len(match_score._scorecard)-1] += 1	
		over_runs = 0
		bowler = prompt_change_bowler(bowler)

	elif user_action == 'f': 

		batsman_on_strike, batsman_off_strike, over_runs = delivery(over_runs, match, over_no, ball_no, bowler, batsman_on_strike, batsman_off_strike, cursor)
		print_current_score_short_form(over_no, ball_no, match_score, batsman_on_strike, batsman_off_strike)	
		if ball_no == 5:
			batsman_on_strike, batsman_off_strike = batsman_off_strike, batsman_on_strike
			ball_no = 0
			over_no += 1
			session_over_no += 1
			if over_runs == 0:
				bowler._maidens[len(match_score._scorecard)-1] += 1	
			over_runs = 0

			bowler = prompt_change_bowler(bowler)
		else:
			ball_no += 1

	result = match_score.check_result(match)	

	if match_score._scorecard[-1][0] == 10:
		batsman_off_strike._how_out[len(match_score._scorecard)-1] = 'not out'
		batting_team = teams[(teams.index(batting_team) +1)%2]
		batsman_on_strike = batting_team._players[0].batsman()
		batsman_off_strike = batting_team._players[1].batsman()
		if len(match_score._scorecard) < 4:
			match_score._scorecard.append([0,0])
			match_score._declared.append(False)
			match_score._is_follow_on.append(False)
		print_current_score_short_form(over_no, ball_no, match_score, batsman_on_strike, batsman_off_strike)	
		print '=== INNINGS ' + str(len(match_score._scorecard)-1) + ' complete.'
		innings_over_no = 0
		ball_no = 0
	
	if session_over_no == 30:
		if session_no == 0:
			print '-- Lunch break'
			session_over_no = 0
			session_no += 1
		elif session_no == 1:
			print '-- Tea break'
			session_over_no = 0
			session_no += 1
		else:
			print '-- Stumps'
			session_over_no = 0
			session_no = 0
			day_no += 1
	conn.commit()
	conn.close()

print 'GAME OVER!!!'
print '===================='
print match_score.print_score(True, match)[0]
print '|| ' + str(result)
print '===================='
print 'Bowling statistics'
print match_score.print_score(True, match)[1]
print 'Thanks for playing.'