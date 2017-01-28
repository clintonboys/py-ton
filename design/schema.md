## Store each ball from each game in a local MySQL instance 

Open game
-> Start at 1885 with first test between Australia and England
Load game
-> Load game, database

match_home_team
match_away_team
match_ground
match_start_date
match_end_date
match_day
match_innings
innings_wickets_down
innings_runs
innings_batting_team
innings_bowling_team
day_session
session_over
over_ball
batsman_on_strike
batsman_off_strike
bowler
keeper
field
ball_runs_scored
ball_extras_scored
ball_extras_reason
wicket_taken
wicket_reason
wicket_catcher

CREATE TABLE ball_history (match_home_team int, match_away_team int, match_ground int, match_start_date datetime, match_end_date datetime, match_day int, match_innings int, innings_wickets_down int, innings_runs int, innings_batting_team int, innings_bowling_team int, day_session int, session_over int, over_ball int, batsman_on_strike varchar(50), batsman_off_strike varchar(50), bowler varchar(50), keeper varchar(50), field varchar(1000), ball_runs_scored int, ball_extras_scored int, ball_extras_reason varchar(50), wicket_taken boolean, wicket_reason varchar(50), wicket_catcher varchar(50))