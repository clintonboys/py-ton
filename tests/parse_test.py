import pandas as pd
import yaml

with open('291352.yaml') as f:
	contents = yaml.load(f)

## features to extract
	# day_no
	# session_no
	# innings_no
	# innings_over_no
	# session_over_no
	# bowler
	# batsman_on_strike
	# batsman_off_strike
	# runs_scored
	# wickets_taken
	# extras
	# method_of_dismissal

print len(contents["innings"][0]["1st innings"]["deliveries"])

# delivery_data = pd.DataFrame(columns = ['day_no', 'session_no', 'innings_no',
# 										'innings_over_no','session_over_no','bowler',
# 										'batsman_on_strike','batsman_off_strike','runs_scored',
# 										'wickets_taken','extras','method_of_dismissal'])
# day_nos = []
# session_nos = []
# innings_nos = []
# innings_over_nos = []
# session_over_nos = []
# bowlers = []
# batsmen_on_strike = []
# batsmen_off_strike = []
# runs_scoreds = []
# wickets_takens = []
# extrass = []
# methods_of_dismissal = []
# for i in range(0,len(contents)):
# 	try:
# 		if contents[i].split(' ')[4] == 'innings:\n':
# 			innings_number = contents[i].split(' ')[3][0]
# 	except:
# 		pass