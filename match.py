from player import *
from tabulate import tabulate
import numpy as np
import json
from ball import Ball
import random

class MatchScore(object):

    def __init__(self, scorecard = [[0,0]], declared = [False], is_follow_on = [False], is_over = False):
        self._scorecard = scorecard
        self._declared = declared
        self._is_follow_on = is_follow_on
        self._is_over = is_over

    def wicket_taken(self):
        before_wicket = self._scorecard
        innings_number = len(before_wicket) - 1
        wickets = before_wicket[innings_number][0]
        runs = before_wicket[innings_number][1]
        # if self._declared[innings_number] == False:
        #   wickets += 1
        #   self._scorecard[innings_number][0] = wickets
        # else:
        #   self._declared[innings_number][0] = True
        #   self._scorecard.append([0,0])
        #   self._declared.append(False)
        #   self._is_follow_on.append(False)
        if wickets < 10:
            self._scorecard[-1][0] += 1

    def declare(self):
        self._declared[-1] = True
        self._declared.append(False)
        self._scorecard.append([0,0])
        self._is_follow_on.append([False])

    def runs_scored(self, runs):
        #innings_number = len(self._scorecard)
        self._scorecard[-1][1] += runs

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
        #print innings_number
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
                        total_first = sum([match._teams[0]._players[i].batsman()._runs[0] for i in range(0, 11)])
                    else:
                        total_first = str(self._scorecard[0][0])+'/'+str(sum([match._teams[0]._players[i].batsman()._runs[0] for i in range(0, self._scorecard[0][0] +1)]))+' (d)'
                    batting_stats_table.append(['Aus (1st inn.)', total_first             , '','' ,''  ,''])
                    batting_stats_table.append(['--------------','--------------','R','B','4s','6s'])
                    for i in range(0, self._scorecard[0][0] + 1):
                        batting_stats_table.append([match._teams[0]._players[i].batsman()._name, match._teams[0]._players[i].batsman()._how_out[0],match._teams[0]._players[i].batsman()._runs[0],match._teams[0]._players[i].batsman()._deliveries[0],match._teams[0]._players[i].batsman()._fours[0],match._teams[0]._players[i].batsman()._sixes[0] ])
                if innings_number > 1:
                    if self._scorecard[1][0] == 10:
                        total_second = sum([match._teams[1]._players[i].batsman()._runs[1] for i in range(0, 11)])
                    else:
                        total_second = str(self._scorecard[1][0])+'/'+str(sum([match._teams[1]._players[i].batsman()._runs[1] for i in range(0, self._scorecard[1][0] +1)]))+' (d)'
                    batting_stats_table[0]+= ['Eng (1st inn.)',total_second,'','','','']
                    batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
                    for j in range(0, self._scorecard[1][0] + 1):
                        try:
                            batting_stats_table[j+2] += [match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[1], match._teams[1]._players[j].batsman()._runs[1], match._teams[1]._players[j].batsman()._deliveries[1], match._teams[1]._players[j].batsman()._fours[1], match._teams[1]._players[j].batsman()._sixes[1]]                            
                        except:
                            batting_stats_table.append(['','','','','','',match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[1], match._teams[1]._players[j].batsman()._runs[1], match._teams[1]._players[j].batsman()._deliveries[1], match._teams[1]._players[j].batsman()._fours[1], match._teams[1]._players[j].batsman()._sixes[1]])
                if innings_number > 2:
                    if self._scorecard[2][0] == 10:
                        total_third = sum([match._teams[0]._players[i].batsman()._runs[2] for i in range(0, 11)])                   
                    else:
                        total_third = str(self._scorecard[2][0]) +'/' +str(sum([match._teams[0]._players[i].batsman()._runs[2] for i in range(0, self._scorecard[2][0] +1)]))+' (d)'
                    batting_stats_table[0] += ['Aus (2nd inn.)', total_third, '', '','','']
                    batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
                    for j in range(0, self._scorecard[1][0] + 1):
                        try:
                            if len(batting_stats_table[j+2]) == 6:
                                batting_stats_table[j+2] += ['','','','','','',match._teams[0]._players[j].batsman()._name, match._teams[0]._players[j].batsman()._how_out[2], match._teams[0]._players[j].batsman()._runs[2], match._teams[0]._players[j].batsman()._deliveries[2], match._teams[0]._players[j].batsman()._fours[2], match._teams[0]._players[j].batsman()._sixes[2]]
                            elif len(batting_stats_table[j+2]) == 12:   
                                batting_stats_table[j+2] += [match._teams[0]._players[j].batsman()._name, match._teams[0]._players[j].batsman()._how_out[2], match._teams[0]._players[j].batsman()._runs[2], match._teams[0]._players[j].batsman()._deliveries[2], match._teams[0]._players[j].batsman()._fours[2], match._teams[0]._players[j].batsman()._sixes[2]]
                        except:
                            batting_stats_table.append(['','','','','','','','','','','','',match._teams[0]._players[j].batsman()._name, match._teams[0]._players[j].batsman()._how_out[2], match._teams[0]._players[j].batsman()._runs[2], match._teams[0]._players[j].batsman()._deliveries[2], match._teams[0]._players[j].batsman()._fours[2], match._teams[0]._players[j].batsman()._sixes[2]])
                if innings_number > 3:
                    if self._scorecard[3][0] == 10:
                        total_fourth = sum([match._teams[1]._players[i].batsman()._runs[3] for i in range(0, 11)])                                      
                    else:
                        total_fourth = str(self._scorecard[3][0])+'/'+str(sum([match._teams[1]._players[i].batsman()._runs[3] for i in range(0, self._scorecard[3][0] +1)]))
                    batting_stats_table[0] += ['Eng (2nd inn.)',total_fourth,'','','','']
                    batting_stats_table[1] += ['--------------','--------------','R','B','4s','6s']
                    for j in range(0, self._scorecard[1][0] + 1):
                        try:
                            if len(batting_stats_table[j+2]) == 6:
                                batting_stats_table[j+2] += ['','','','','','','','','','','','',match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[3], match._teams[1]._players[j].batsman()._runs[3], match._teams[1]._players[j].batsman()._runs[3], match._teams[1]._players[j].batsman()._deliveries[3], match._teams[1]._players[j].batsman()._fours[3], match._teams[1]._players[j].batsman()._sixes[3]]
                            elif len(batting_stats_table[j+2]) == 12:   
                                batting_stats_table[j+2] += ['','','','','','',match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[3], match._teams[1]._players[j].batsman()._runs[3], match._teams[1]._players[j].batsman()._deliveries[3], match._teams[1]._players[j].batsman()._fours[3], match._teams[1]._players[j].batsman()._sixes[3]]
                            elif len(batting_stats_table[j+2]) == 18:
                                batting_stats_table[j+2] += [match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[3], match._teams[1]._players[j].batsman()._runs[3], match._teams[1]._players[j].batsman()._deliveries[3], match._teams[1]._players[j].batsman()._fours[3], match._teams[1]._players[j].batsman()._sixes[3]]
                        except:
                            batting_stats_table.append(['','','','','','','','','','','','','','','','','','',match._teams[1]._players[j].batsman()._name, match._teams[1]._players[j].batsman()._how_out[3], match._teams[1]._players[j].batsman()._runs[3], match._teams[1]._players[j].batsman()._deliveries[3], match._teams[1]._players[j].batsman()._fours[3], match._teams[1]._players[j].batsman()._sixes[3]])


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


class Match(object):

    def __init__(self, match_id, ground, teams):
        self._id = match_id
        self._day = 0
        self._session = 0
        self._session_over = 0
        self._innings_number = 0
        self._innings_over = 0
        self._innings_runs = 0
        self._innings_wickets = 0
        self._over_ball = 0
        self._over_runs = 0
        self._ground = ground
        self._match_score = MatchScore()
        self._teams = teams
        self._batting_team = random.choice(teams)
        self._batsman_on_strike = self._batting_team._players[0].batsman()
        self._batsman_off_strike = self._batting_team._players[1].batsman()
        self._bowling_team = [team for team in teams if team != self._batting_team][0]
        self._bowler = self._bowling_team._players[-1].bowler()

    def new_innings(self):
        self._innings_number += 1
        self._innings_over = 0
        self._innings_runs = 0
        self._innings_wickets = 0
        self._over_ball = 0
        self._over_runs = 0

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

    def to_json(self):
        match_json = {"matchid":self._id,"match_day":self._day,"match_session":self._session,"match_session_over":self._session_over,
                         "match_innings":self._innings,"match_innings_over":self._innings_over,"match_ground":self._ground,"teams":[self._teams[0]._id, self._teams[1]._id],
                         "scorecard":self._match_score._scorecard,"scorecard_declared":self._match_score._declared,"scorecard_followon":self._match_score._is_follow_on,
                         "scorecard_is_over":self._match_score._is_over}
        with open('matches/match'+str(self._id)+'.json','w') as outfile:
            json.dump(match_json, outfile)      

    def wicket_taken(self, wickets):
        self._innings_wickets += wickets
        # innings_number = len(before_wicket) - 1
        # wickets = before_wicket[innings_number][0]
        # runs = before_wicket[innings_number][1]
        # # if self._declared[innings_number] == False:
        # #   wickets += 1
        # #   self._scorecard[innings_number][0] = wickets
        # # else:
        # #   self._declared[innings_number][0] = True
        # #   self._scorecard.append([0,0])
        # #   self._declared.append(False)
        # #   self._is_follow_on.append(False)
        # if wickets < 10:
        #     self._scorecard[-1][0] += 1

    def declare(self):
        self._scorecard.declare()
        self._batsman_off_strike._how_out[len(match._match_score._scorecard)-1] = 'not out'
        self._batsman_on_strike._how_out[len(match._match_score._scorecard)-1] = 'not out'      
        self._batting_team = self._teams[(self._teams.index(self._batting_team) +1)%2]
        self._batsman_on_strike = self._batting_team._players[0].batsman()
        self._batsman_off_strike = self._batting_team._players[1].batsman()
        self.new_innings()
        return None

    def over(self):
        if self._over_runs == 0:
            self._bowler._maidens[self._innings_number] += 1    
        self._batsman_on_strike, self._batsman_off_strike = self._batsman_off_strike, self._batsman_on_strike
        self._innings_over += 1
        self._over_ball = 0
        self._session_over += 1

    def all_out(self):
        self._batsman_off_strike._how_out[self._innings_number] = 'not out'
        self._batting_team = self._teams[(self._teams.index(self._batting_team) +1)%2]
        self.new_innings()
        self._batsman_on_strike = self._batting_team._players[0].batsman()
        self._batsman_off_strike = self._batting_team._players[1].batsman()
        if len(self._match_score._scorecard) < 4:
            self._match_score._scorecard.append([0,0])
            self._match_score._scorecard.append(False)
            self._match_score._scorecard.append(False)

    def prompt_change_bowler(self):
        change_bowler = raw_input('change bowler? (y/n)...| ')
        if change_bowler == 'y':
            bowler_menu = ''
            index = 0
            sorted_bowlers = sorted(self._teams[(self._teams.index(self._batting_team) +1)%2]._players, key=lambda x:x.bowler()._skill_multiplier, reverse = True)
            for player in sorted_bowlers:
                bowler_menu = bowler_menu + player.bowler()._name + ' (' + str(player.bowler()._skill_multiplier) + '): ' + str(index) + '\n'
                index += 1
            new_bowler_index = raw_input('Choose the new bowler...' + '\n' + bowler_menu)
            try:
                self._bowler = sorted_bowlers[int(new_bowler_index)].bowler()
            except:
                pass

    def simulate_delivery(self, conn, database):
        delivery_result = []

        # Create delivery
        this_ball = Ball(self)
        delivery_result.append('{0} bowls to {1}..'.format(self._bowler._name, self._batsman_on_strike._name))

        wickets, runs = this_ball.deliver()

        # Assign runs
        self._over_runs += this_ball._runs_scored
        self._match_score.runs_scored(runs)
        self._batsman_on_strike._runs[self._innings_number] += runs
        self._batsman_on_strike._deliveries[self._innings_number] += 1
        self._batsman_on_strike._minutes[self._innings_number] += 3
        if this_ball._runs_scored == 4:
            self._batsman_on_strike._fours[self._innings_number] += 1
        if this_ball._runs_scored == 6:
            self._batsman_on_strike._sixes[self._innings_number] += 1   
        delivery_result.append('{0} scores {1} runs..'.format(self._batsman_on_strike._name, this_ball._runs_scored))

        # If even, swap ends
        if this_ball._runs_scored%2 == 1:
            self._batsman_on_strike, self._batsman_off_strike = self._batsman_off_strike, self._batsman_on_strike   

        # Assign bowler stats
        self._bowler._over[self._innings_number] += 1.0/6.0 
        # rest to-do

        if wickets > 0 and self._innings_wickets < 9:
            self.wicket_taken(wickets)
            delivery_result.append('WICKET! {0} is out {1}'.format(self._batsman_on_strike._name, this_ball._method_of_dismissal))
            self._batsman_on_strike._is_out[self._innings_number] = True
            self._batsman_on_strike._how_out[self._innings_number] = this_ball._method_of_dismissal
            self._batsman_on_strike = self._batting_team._players[min([i for i in range(0,len(self._batting_team._players))\
             if not self._batting_team._players[i].batsman()._is_out[self._innings_number] \
             if i != [player.batsman() for player in self._batting_team._players].index(self._batsman_off_strike)])].batsman()
            is_wickets = True
            dismissal = this_ball._method_of_dismissal
        elif wickets > 0 and self._innings_wickets == 9:
            self._innings_wickets += wickets
            #self._match_score.wicket_taken()
            self.all_out()
            delivery_result.append('=== INNINGS ' + str(self._innings_number) + ' complete.')
            is_wickets = True
            dismissal = this_ball._method_of_dismissal
        else:
            dismissal = ''
            is_wickets = False

        query = '''INSERT INTO {20}.ball_history (match_id, match_home_team, match_away_team, match_ground, match_start_date, match_end_date, match_day, match_innings, innings_wickets_down, innings_runs, innings_batting_team, innings_bowling_team, day_session, session_over, over_ball, batsman_on_strike, batsman_off_strike, bowler, keeper, field, ball_runs_scored, ball_extras_scored, ball_extras_reason, wicket_taken, wicket_reason, wicket_catcher)
                   VALUES ({21}, {0}, {1}, \'{2}\', \'{3}\',\'{4}\', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, \'{14}\', \'{15}\', \'{16}\', "", "", {17} , 0, "", {18}, \'{19}\', "");'''.format(self._teams[0]._id, self._teams[1]._id, 1, '2016-12-26', '2016-12-30', self._day, self._innings_number, self._match_score._scorecard[self._innings_number][0], self._match_score._scorecard[self._innings_number][1], self._batting_team._id, self._teams[(self._teams.index(self._batting_team)+1)%2]._id, self._session, self._session_over, self._over_ball, self._batsman_on_strike._name, self._batsman_off_strike._name, self._bowler._name, this_ball._runs_scored, is_wickets, dismissal, database, self._id)
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()

        if self._over_ball < 5:
            self._over_ball += 1
        else:
            self.over()
            self.prompt_change_bowler()

        if self._session_over == 30:
            if self._session == 0:
                delivery_result.append('-- Lunch break')
                self._session_over = 0
                self._session += 1
            elif self._session == 1:
                delivery_result.append('-- Tea break')
                self._session_over = 0
                self._session += 1
            else:
                delivery_result.append('-- Stumps')
                self._session_over = 0
                self._session += 1
                self._day += 1


        return '\n'.join(delivery_result)








