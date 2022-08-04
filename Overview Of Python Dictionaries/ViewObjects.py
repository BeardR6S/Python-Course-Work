#Need more time with this to fully understand it.

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}


player_names = list(players.copy().values())

# print(player_names)

# print(players.keys())

# print(list(players.values())[1])

# print(players.items())

teams = {
  "Astros" : ["Altuve", "Correa", "Bregman"],
  "Angels":  ["Trout", "Pujols"],
  "Yankees": ["Judge", "Stanton"],
  "Red Sox": ["Price", "Betts"],
}

"""
[
  ('Astros', ['Altuve', 'Correa', 'Bregman']), 
  ('Angels', ['Trout', 'Pujols']), 
  ('Yankees', ['Judge', 'Stanton']), 
  ('Red Sox', ['Price', 'Betts'])
]
"""

team_groupings = teams.items()

print(list(team_groupings)[1][1][0])
