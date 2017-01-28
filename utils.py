import json
from team import Team
from player import *
from match import *

def parse_team_json(json_filename, bats_first = False):
	# Parses a JSON file into a team class
	with open('teams/'+json_filename) as data_file:
		data = json.load(data_file)
	team_id = data[u'teamid']
	team_name = data[u'name']
	team_short_name = data[u'short_name']
	player_list = []
	for player in data[u'players']:
		player_list.append(Player(Batsman({"name": player[u'name'], "handedness": player[u'batsman'][u'handedness'], "skill_multiplier": player[u'batsman'][u'skill_multiplier']}),
								  Bowler({"name": player[u'name'], "style": player[u'bowler'][u'style'], "skill_multiplier": player[u'bowler'][u'skill_multiplier']})))
	return Team(team_id,team_name, team_short_name, player_list, bats_first)

def parse_match_json(json_filename):
	# Parses a JSON file into a match class and associated score class
	with open('matches/'+json_filename) as data_file:
		data = json.load(data_file)
	match_id = data[u'matchid']
	match_day = data[u'match_day']
	match_session = data[u'match_session']
	match_session_over = data[u'match_session_over']
	match_innings = data[u'match_innings']
	match_innings_over = data[u'match_innings_over']
	match_ground = data[u'match_ground']
	match_teamA = data[u'teams'][0]
	match_teamB = data[u'teams'][1]
	teamA = parse_team_json('team'+str(match_teamA)+'.json')
	teamB = parse_team_json('team'+str(match_teamB)+'.json')
	match_teams = [teamA, teamB]
	match_scorecard = data[u'scorecard']
	match_scorecard_declared = data[u'scorecard_declared']
	is_declared = []
	for innings in match_scorecard_declared:
		if innings == "True":
			is_declared.append(True)
		else:
			is_declared.append(False)		
	match_scorecard_followon = data[u'scorecard_followon']
	is_follow_on = []
	for innings in match_scorecard_followon:
		if innings == "True":
			is_follow_on.append(True)
		else:
			is_follow_on.append(False)
	match_scorecard_is_over = data[u'scorecard_is_over']
	if match_scorecard_is_over == "True":
		is_over = True
	else:
		is_over = False

	scorecard = MatchScore(match_scorecard, match_scorecard_declared, match_scorecard_followon, is_over)
	match = Match(match_id, match_day, match_session, match_session_over, match_innings, match_innings_over, match_ground, scorecard, match_teams)
	return match, scorecard

