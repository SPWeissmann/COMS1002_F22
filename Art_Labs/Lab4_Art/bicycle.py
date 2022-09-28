#The bicycle module contains functions relating to bicycles 


def ride(loc, distance, direction):
    x,y = loc #list expansion. Assigns x = loc[0] and y = loc[1].
    
    if direction == "north":
        y += distance
    elif direction == "east":
        x += distance
    elif direction == "south":
        y -= distance
    elif direction == "west":
        x -= distance

    location = [x,y]
    return location
