from collections import OrderedDict

ipl_teams = [('CSK',(11, 3)), ('MI', (12, 2)), ('KKR', (10, 4)),
('RCB', (7, 7)), ('SRH', (11, 3))]

# Sort teams accorfing to no. of wins
sorted_teams = sorted(ipl_teams, key=lambda t: t[1][0], reverse=True)
print(sorted_teams)

# Now use OrderedDict to maintain the order
teams = OrderedDict(sorted_teams)
print(teams)

# Pop the first item from OrderedDict object i.e the team with highest wins
team, win_loss = teams.popitem(False)
print(team, win_loss)
print(teams)

# Print top3 teams after MI
for i,v in enumerate(teams, start=1):
    print(i, v)
    if i == 3:
        break

# Test equality in OrderedDict
a = OrderedDict({'a': 1, 'b': 2})
b = OrderedDict({'a': 1, 'b': 2})
c = OrderedDict({'b': 2, 'a': 1})
print(a == b) # Returns true since order of a and b is the same
print(a == c) # Returns false since order is different
