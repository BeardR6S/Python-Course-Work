teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# del teams['astros'] #works when the item exists in the code.
# del (teams['mets']) #throws error due to not existing.

# teams.pop('astros', 'No team found by that name') #removes the astros

removed_team = teams.pop('rays', 'No team found by that name')

print(teams)
print(removed_team)