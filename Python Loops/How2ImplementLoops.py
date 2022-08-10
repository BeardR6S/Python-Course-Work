#Lists/Tuples Version of Loops

# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# for player in players:
#     print(player)


#Dictionary Version of Loops
players = {
    '2B': 'Altuve',
    '3B': 'Bregman',
    'SS': 'Correa',
    'DH': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player Name', player)