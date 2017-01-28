sqls = {"first_play_queries": ['create database pyton_master;',
							  'use pyton_master;',
							  'create table matches (match_id int, file varchar(50));',
							  'create table teams (team_id int, file varchar(50));',
							  'create table grounds (ground_id int, file varchar(50));',
							  'create table players (player_id int, file varchar(50));'],

		"get_max_ids": ['select case when max_match_id is null then 0 else max_match_id end as max_match_id from (select max(match_id) as max_match_id from matches) as max_id;',
			   'select case when max_team_id is null then 0 else max_team_id end as max_team_id from (select max(team_id) as max_team_id from teams) as max_id',
			   'select case when max_ground_id is null then 0 else max_ground_id end as max_ground_id from (select max(ground_id) as max_ground_id from grounds) as max_id',
			   'select case when max_player_id is null then 0 else max_player_id end as max_player_id from (select max(player_id) as max_player_id from players) as max_id'],
			   
		"init_database": '''CREATE TABLE ball_history 
					  ( 
					  	 match_id			  INT,
					     match_home_team      INT, 
					     match_away_team      INT, 
					     match_ground         INT, 
					     match_start_date     DATETIME, 
					     match_end_date       DATETIME, 
					     match_day            INT, 
					     match_innings        INT, 
					     innings_wickets_down INT, 
					     innings_runs         INT, 
					     innings_batting_team INT, 
					     innings_bowling_team INT, 
					     day_session          INT, 
					     session_over         INT, 
					     over_ball            INT, 
					     batsman_on_strike    VARCHAR(50), 
					     batsman_off_strike   VARCHAR(50), 
					     bowler               VARCHAR(50), 
					     keeper               VARCHAR(50), 
					     field                VARCHAR(1000), 
					     ball_runs_scored     INT, 
					     ball_extras_scored   INT, 
					     ball_extras_reason   VARCHAR(50), 
					     wicket_taken         BOOLEAN, 
					     wicket_reason        VARCHAR(50), 
					     wicket_catcher       VARCHAR(50),
					     insertion_time       DATETIME
					  ) '''	   					  }