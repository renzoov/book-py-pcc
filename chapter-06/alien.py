alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

print("\n------------------------------\n")

print(alien_0)

alien_0["x-position"] = 0
alien_0["y_position"] = 25
print(alien_0)

print("\n------------------------------\n")

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n------------------------------\n")

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print("\n------------------------------\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)