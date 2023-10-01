import numpy as np
import skfuzzy as sk
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# input vaariables
PassingYards = ctrl.Antecedent(np.arange(0,200,1), 'PassingYards')
RushYards = ctrl.Antecedent(np.arange(0,150,1), 'RushYards')
Sacks = ctrl.Antecedent(np.arange(0,3.0,1), 'Sacks')
Interceptions = ctrl.Antecedent(np.arange(0,1.0,1), 'Interceptions')
TravelDistance = ctrl.Antecedent(np.arange(0,2500,1), 'TravelDistance') 
Weather = ctrl.Antecedent(np.arange(0,1.1,0.1), 'Weather')
HomeField = ctrl.Antecedent(np.arange(0,1.1,0.1), 'HomeField')
HistoricalMatches = ctrl.Antecedent (np.arange (0,1.1,0.1),'HistoricMatches')

#Output variable
WinningPercent = ctrl.Antecedent(np.arange(0,1.1,0.1), 'WinningPercent')

""" 
Membership functions are defined below.
They are Passing Yards, Rushing Yards, Sacks, Interceptions,
TravelDistance, Weather, HomeField  and Historical Matches. 
"""

#Passing Yards 
PassingYards['low'] = fuzz.trimf(PassingYards.universe, [0, 0, 100])
PassingYards['average'] = fuzz.trimf(PassingYards.universe, [50, 100, 150])
PassingYards['high'] = fuzz.trimf(PassingYards.universe, [200, 200, 300])

#Rush Yards 
RushYards['low'] = fuzz.trimf(RushYards.universe, [0, 0, 130])
RushYards['average'] = fuzz.trimf(RushYards.universe, [100, 130, 160])
RushYards['high'] = fuzz.trimf(RushYards.universe, [130, 200, 200])

#Sacks
Sacks['low'] = fuzz.trimf(Sacks.universe, [0, 0, 3])
Sacks['average'] = fuzz.trimf(Sacks.universe, [2, 3, 4])
Sacks['high'] = fuzz.trimf(Sacks.universe, [3, 5, 5])

#Interceptions
Interceptions['low'] = fuzz.trimf(Interceptions.universe, [0, 0, 1])
Interceptions['average'] = fuzz.trimf(Interceptions.universe, [0.5, 1, 1.5])
Interceptions['high'] = fuzz.trimf(Interceptions.universe, [1, 2, 2])

# TravelDistance
TravelDistance['low'] = fuzz.trimf(TravelDistance.universe, [0, 500, 1000])
TravelDistance['medium'] = fuzz.trimf(TravelDistance.universe, [1000, 1500, 2000])
TravelDistance['high'] = fuzz.trimf(TravelDistance.universe, [2000, 2500, 2500])

#Weather 
Weather['bad'] = fuzz.trimf(Weather.universe, [0, 0, 0.5])
Weather['ok'] = fuzz.trimf(Weather.universe, [0.25, 0.5, 0.75])
Weather['good'] = fuzz.trimf(Weather.universe, [0.5, 1, 1])

#Homefield 
HomeField['away'] = fuzz.trimf(HomeField.universe, [0, 0, 0.5])
HomeField['neutral'] = fuzz.trimf(HomeField.universe, [0.25, 0.5, 0.75])
HomeField['home'] = fuzz.trimf(HomeField.universe, [0.5, 1, 1])

#Historic matches 
HistoricalMatches['negative'] = fuzz.trimf(HistoricalMatches.universe, [0, 0, 0.5])
HistoricalMatches['even'] = fuzz.trimf(HistoricalMatches.universe, [0.25, 0.5, 0.75])
HistoricalMatches['positive'] = fuzz.trimf(HistoricalMatches.universe, [0.5, 1, 1.1])

#Fuzzy Rules 

