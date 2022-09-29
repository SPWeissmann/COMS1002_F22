#The bicycle module contains functions relating to bicycles 

def ride(loc, distance, direction):
    x = loc[0]
    y = loc[1]
    #x,y = loc #list expansion. Assigns x = loc[0] and y = loc[1].

    #update x,y coordinates
    if direction == "north":
        y += distance
    elif direction == "east":
        x += distance
    elif direction == "south":
        y -= distance
    elif direction == "west":
        x -= distance

    #return the new location
    location = [x,y]
    return location
    