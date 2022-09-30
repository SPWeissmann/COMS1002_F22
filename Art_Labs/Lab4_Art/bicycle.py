#The bicycle module contains functions relating to bicycles 

def ride(loc, distance, direction):
    x = loc[0]
    y = loc[1]
    #x,y = loc #list expansion. Assigns x = loc[0] and y = loc[1].

    #update x,y coordinates
    if direction == "n":
        y += distance
    elif direction == "e":
        x += distance
    elif direction == "s":
        y -= distance
    elif direction == "w":
        x -= distance

    #return the new location
    location = [x,y]
    return location
    