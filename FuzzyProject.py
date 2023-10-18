import numpy as np
import skfuzzy as sk
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['average'] & Sacks['average'] &
        Interceptions['average'] & TravelDistance['average'] & Weather['ok'] & HomeField['neutral'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['low'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['high'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['ok'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['average'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['ok'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['average'] & Sacks['low'] &
        Interceptions['average'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['low'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['ok'] & HomeField['home'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['neutral'],
        WinningPercent['Win']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['low'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['neutral'],
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
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['high'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['ok'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['high'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['good'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['average'] & Sacks['low'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['low'] & RushYards['average'] & Sacks['low'] &
        Interceptions['high'] & TravelDistance['high'] & Weather['ok'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['high'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['bad'] & HomeField['away'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['high'] & Sacks['high'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['ok'] & HomeField['neutral'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['average'] & RushYards['low'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['bad'] & HomeField['neutral'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['high'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['bad'] & HomeField['neutral'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['average'] & Sacks['low'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['bad'] & HomeField['neutral'],
        WinningPercent['Lose']
    ),
    ctrl.Rule(
        PassingYards['high'] & RushYards['low'] & Sacks['average'] &
        Interceptions['low'] & TravelDistance['low'] & Weather['bad'] & HomeField['neutral'],
        WinningPercent['Lose']
    )
]

# Combine all rules
rules = team1_rules + team2_rules

# Create control system
system = ctrl.ControlSystem(rules)
# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('fuzzy.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open('FuzzyData')  # Replace with the name of your Google Sheet

# Get the first (or specific) worksheet
worksheet = sheet.get_worksheet(0)  # Replace with the index of your worksheet if needed

# Get all values from the worksheet as a list of lists
input_data = worksheet.get_all_values()

# Assuming the first row contains column headers, convert to a pandas DataFrame
input_data = pd.DataFrame(input_data[1:], columns=input_data[0])

for week in range(1, 10):
    week_data = input_data[input_data['Week'] == str(week)]

    print(f"{'Week':<10}{'Team1':<15}{'Team2':<15}{'Team 1 win %':<20}{'Team 2 win %':<20}{'Winner':<15}")
    for _, row in week_data.iterrows():
        team_name = row['Team']
        team_input = {
            'PassingYards': float(row['PassingYards']),
            'RushYards': float(row['RushYards']),
            'Sacks': float(row['Sacks']),
            'Interceptions': float(row['Interceptions']),
            'TravelDistance': float(row['TravelDistance']),
            'Weather': float(row['Weather']),
            'HomeField': float(row['HomeField']),
        }

    # Create control system and simulator
    system = ctrl.ControlSystem(rules)
    simulator = ctrl.ControlSystemSimulation(system)

    # Pass input for the team
    for key, value in team_input.items():
        simulator.input[key] = value

    # Compute winning percentage
    simulator.compute()
    winning_percent_team = simulator.output['WinningPercent']

    # Determine the opponent
    opponent = input_data.loc[(input_data['Week'] == str(week)) & (input_data['Team'] != team_name)]['Team'].values[0]

    # Determine the winner
    winner = team_name if winning_percent_team > 0.5 else opponent

    print(f"{week:<10}{team_name:<15}{opponent:<15}{winning_percent_team:<20}{(1 - winning_percent_team):<20}{winner:<15}")
   

# Add code to handle the last week if needed







# Plot the membership functions


# Plot the membership functions
""" for var in [PassingYards, RushYards, Sacks, Interceptions, TravelDistance, Weather, HomeField, WinningPercent]:
    var.view()

plt.show() """ 

