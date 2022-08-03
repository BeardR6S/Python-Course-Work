teams = {
    "Astros": ["Altuve", "Correa", "Bregman"],
    "Angels": ["Trout", "Pujols"],
    "Yankees": ["Judge", "Stanton"],
    "Red Sox": ["Price", "Betts"],
}

# featured_team = teams["Astros"]

featured_team = teams.get("Mets", "No Featured Team") #Throws "No Featured Team"
# featured_team = teams.get("Yankees", "No Featured Team") #Throws Players Names

print(featured_team)