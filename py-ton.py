import os
import re
import pymysql
import logging
from utils import *
from match import *
from game_loop import *
from sqls import sqls

def game_init(conn, cursor):
	os.system('clear')
	print '------------------------//-'
	print 'Welcome to pyCricket--/--/-'
	print '-- v0.1--------------/--/--'
	print '--------------------/__/O--'
	print '(c) Clinton Boys 2016------'
	print '---------------------------'
	try:
		cursor.execute('use pyton_master;')
	except:
		for query in sqls["first_play_queries"]:
			cursor.execute(query)
		conn.commit()					  	
	queries = sqls["get_max_ids"]
	max_ids = []		 
	for query in queries:
		cursor.execute(query)
		max_ids.append(cursor.fetchone()[0])
	return {"match": max_ids[0], "teams": max_ids[1], "grounds": max_ids[2], "players": max_ids[3]}

def main_menu():
	#os.system('clear')
	print '---------------------------'
	print '---------MAIN MENU---------'
	print '(n)ew game-----------------'
	print '(l)oad game----------------'
	print '(h)elp---------------------'
	print '---------------------------'
	user_choice = ''
	while user_choice not in ('n','l','h'):
		user_choice = raw_input('Make your selection.. ')
	return user_choice

def new_game(conn, cursor):
	file_name = ''
	while not re.match(r'^[a-z]+$',file_name):
		print '---------------------------'
		print 'Please enter a name for ---'
		print 'your game file (no spaces, '
		print 'lower case characters only)'
		print '---------------------------'
		file_name = raw_input('Enter a file name.. ')
	try:
		cursor.execute('create database {0};'.format(file_name))
		cursor.execute('use {0};'.format(file_name))
		conn.commit()
		return file_name
	except Exception, e:
		print str(e)
		return None

def load_game(cursor):
	file_name = raw_input('Enter a file name.. ')
	try:
		cursor.execute('use {0}'.format(file_name))
		return file_name
	except Exception, e:
		print str(e)
		return None

def database_init(database, conn, cursor):
	create_query = sqls["init_database"].format(database)
	try:
		cursor.execute(create_query)
	except Exception, e:
		logging.warning(str(e))
	conn.commit

def print_help():
	print 'Help in progress..'

def choose_mode(is_new):
	os.system('clear')
	start ='---------------------------\n' +\
	       '---------GAME MENU---------\n' +\
           '---------------------------\n' +\
	       '--INTERACTIVE MODE---------\n' +\
	       '(n)ew match----------------\n'
	if not is_new:
		middle = '(c)continue match----------\n'
	else:
		middle = ''
	end = '---------------------------\n' +\
	      '--SIMULATOR----------------\n' +\
	      '(s)simulator---------------\n' +\
	      '---------------------------\n' +\
	      '--STATISTICS---------------\n' +\
	      's(t)ats mode---------------\n' +\
	      '---------------------------'
	print start+middle+end
	user_choice = ''
	while user_choice not in ('n','c','s','t'):
		user_choice = raw_input('Make your selection.. ')
	return user_choice

def new_match(conn, cursor, database, max_match_id):
	cursor.execute('insert into pyton_master.matches values ({1}, \'{0}\');'.format(database, max_match_id+1))
	os.system('clear')
	print '---------------------------'
	print 'Choose teams---------------'
	print '-- (coming soon) ----------'
	teamA = parse_team_json('team1.json')
	teamB = parse_team_json('team2.json')
	ground = 'SCG'
	match = Match(max_match_id+1, ground, [teamA, teamB])
	match_json = {"matchid":max_match_id+1,"match_day":0,"match_session":0,"match_session_over":0,
					 "match_innings":0,"match_innings_over":0,"match_ground":ground,"teams":[teamA._id,teamB._id],
					 "scorecard":[[0,0]],"scorecard_declared":["False"],"scorecard_followon":["False"],
					 "scorecard_is_over":"False"}
	with open('matches/match'+str(max_match_id+1)+'.json','w') as outfile:
		json.dump(match_json, outfile)					 
	return match

def choose_match(conn, cursor, database):
	cursor.execute('select distinct match_id from {0}.ball_history;'.format(database))
	os.system('clear')
	print '---------------------------'
	print '---MATCH--------Type-------'
	for match in cursor.fetchall():
		print '---match{0}------({0})-------'.format(str(match[0]))
	match_choice = raw_input('---------------------------\nChoose a match-------------')
	return match_choice

if __name__ == '__main__':
	master_conn = pymysql.connect(host='localhost',port = 3306, user='root')
	master_cursor = master_conn.cursor()
	logging.basicConfig(filename = 'events.log', level = logging.INFO)

	max_ids = game_init(master_conn, master_cursor)
	user_choice = main_menu()
	if user_choice == 'n':
		database = new_game(master_conn, master_cursor)
		database_init(database, master_conn, master_cursor)
		is_new = True
	elif user_choice == 'l':
		database = load_game(master_cursor)
		is_new = False
	elif user_choice == 'h':
		print_help()
	if database is None:
		print 'No such file saved. Exiting game.'
		sys.exit()
	master_conn.commit()

	user_choice = choose_mode(is_new)
	if user_choice == 'n':
		match = new_match(master_conn, master_cursor, database, max_ids["match"])
		max_ids["match"] += 1
	elif user_choice == 'c':
		match_choice = choose_match(master_conn, master_cursor, database)
		match = parse_match_json('match'+str(match_choice)+'.json')[0]
	want_exit = False
	while not want_exit:
		want_exit = game_loop(match, database, master_conn, master_cursor)
	master_conn.close()




