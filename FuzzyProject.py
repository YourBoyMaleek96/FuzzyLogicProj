import numpy as np
import skfuzzy as sk
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# input vaariables
PassingYards = ctrl.Antecedent(np.arange(0,400,1), 'PassingYards')
RushYards = ctrl.Antecedent(np.arange(0,300,1), 'RushYards')
Sacks = ctrl.Antecedent(np.arange(0,6,0.1), 'Sacks')
Interceptions = ctrl.Antecedent(np.arange(0.4, 1.9, 0.1), 'Interceptions')
TravelDistance = ctrl.Antecedent(np.arange(0,4500,1), 'TravelDistance') 
Weather = ctrl.Antecedent(np.arange(0,1.8,0.1), 'Weather')
HomeField = ctrl.Antecedent(np.arange(0,1.8,0.1), 'HomeField')


# Output variable
WinningPercent = ctrl.Consequent(np.arange (0,1.8,0.1), 'WinningPercent') 



""" 
Input and Output Membership functions are defined below.
Inputs  are Passing Yards, Rushing Yards, Sacks, Interceptions,
TravelDistance, Weather, HomeField  and Historical Matches. 
Output is winning percentage.

"""

#Passing Yards 
PassingYards['low'] = fuzz.gaussmf(PassingYards.universe, 131,36)
PassingYards['average'] = fuzz.gaussmf(PassingYards.universe,218,36)
PassingYards['high'] = fuzz.gaussmf(PassingYards.universe, 289, 36)

#Rush Yards 
RushYards['low'] = fuzz.gaussmf(RushYards.universe,76,23)
RushYards['average'] = fuzz.gaussmf(RushYards.universe,121,23)
RushYards['high'] = fuzz.gaussmf(RushYards.universe, 177,23)

#Sacks
Sacks['low'] = fuzz.gaussmf(Sacks.universe, 1.2,0.6)
Sacks['average'] = fuzz.gaussmf(Sacks.universe, 2.4,0.6)
Sacks['high'] = fuzz.gaussmf(Sacks.universe, 3.9,0.6)

#Interceptions
Interceptions['low'] = fuzz.gaussmf(Interceptions.universe, 0.4, 0.2)
Interceptions['average'] = fuzz.gaussmf(Interceptions.universe, 0.8, 0.2)
Interceptions['high'] = fuzz.gaussmf(Interceptions.universe, 1.2, 0.2)

# TravelDistance
TravelDistance['low'] = fuzz.gaussmf(TravelDistance.universe, 380,711)
TravelDistance['average'] = fuzz.gaussmf(TravelDistance.universe,1056,711)
TravelDistance['high'] = fuzz.gaussmf(TravelDistance.universe,2320,711)

#Weather 
Weather['bad'] = fuzz.gaussmf(Weather.universe, 0,0.2)
Weather['ok'] = fuzz.gaussmf(Weather.universe, 0.5,0.2)
Weather['good'] = fuzz.gaussmf(Weather.universe, 1,0.2)

#Homefield 
HomeField['away'] = fuzz.gaussmf(HomeField.universe, 0,0.2)
HomeField['neutral'] = fuzz.gaussmf(HomeField.universe, 0.5,0.2)
HomeField['home'] = fuzz.gaussmf(HomeField.universe, 1.0,0.2)



#Winning percent
WinningPercent['Lose'] = fuzz.gaussmf(WinningPercent.universe, 0.2,0.1)
WinningPercent['Draw'] = fuzz.gaussmf(WinningPercent.universe, 0.5,0.1)
WinningPercent['Win'] = fuzz.gaussmf(WinningPercent.universe, 0.8,0.1)


team1_rules = [
    ctrl.Rule(
        PassingYards['high'] & RushYards['high'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['high'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['high'] & Sacks['low'] &
        Interceptions['average'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    )
]

team2_rules = [
    ctrl.Rule(
        PassingYards['low'] & RushYards['low'] & Sacks['high'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['average'] & Sacks['high'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['average'] & Sacks['high'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['low'] & Sacks['average'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['low'] & Sacks['high'] &
        Interceptions['average'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    )
]

# Combine all rules
rules = team1_rules + team2_rules

# Create control system
system = ctrl.ControlSystem(rules)



team1_input = {
    'PassingYards': 211,
    'RushYards': 63,
    'Sacks': 2,
    'Interceptions': 1,
    'TravelDistance': 280,
    'Weather': 0,
    'HomeField': 0,
}

team2_input = {
    'PassingYards': 297,
    'RushYards': 83,
    'Sacks': 3,
    'Interceptions': 1,
    'TravelDistance': 0,
    'Weather': 0,
    'HomeField': 1,
}


simulator = ctrl.ControlSystemSimulation(system)

# Pass input for team 1
for key, value in team1_input.items():
    simulator.input[key] = value

# Compute winning percentage for team 1
simulator.compute()

# Get winning percentage for team 1
winning_percent_team1 = simulator.output['WinningPercent']

# Reset the simulator for team 2
simulator.reset()

# Pass input for team 2
for key, value in team2_input.items():
    simulator.input[key] = value

# Compute winning percentage for team 2
simulator.compute()

# Get winning percentage for team 2
winning_percent_team2 = simulator.output['WinningPercent']


# Print winning percentages for both teams
print(f"Team 1 Winning Percentage: {winning_percent_team1:.2f}")
print(f"Team 2 Winning Percentage: {winning_percent_team2:.2f}")


# Determine the winner
if winning_percent_team1 > winning_percent_team2:
    winner = "Team 1"
elif winning_percent_team1 < winning_percent_team2:
    winner = "Team 2"
else:
    winner = "It's a draw"

print(f"The winner is: {winner}")

# Plot the membership functions


# Plot the membership functions
for var in [PassingYards, RushYards, Sacks, Interceptions, TravelDistance, Weather, HomeField, WinningPercent]:
    var.view()

plt.show()

