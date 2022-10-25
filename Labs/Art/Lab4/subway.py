# The subway module contains functions relating to subways
from random import choice #makes choice function from random module available
LINES = ["A","B","C","D"] #ALL CAPS indicates a variable is a constant

def ride(loc, line, direction): 
    x = loc[0]
    y = loc[1]
    #x,y = loc #list expansion. Assigns x = loc[0] and y = loc[1].

    if line == "A" or line == "D": #if an express line
        if direction == "up":
            y += 16
        elif direction == "down":
            y -= 16

    if line == "B" or line == "C": #if a local line
        if direction == "up":
            y += 8
        elif direction == "down":
            y -= 8
    
    location = [x,y] 
    return location
    #return [x,y] #a more succinct way to return the new location.

#randomly generates "next arriving train" and returns the new location
#after riding it
def next_train(loc):
    line = choice(LINES)
    direction = choice(["up","down"])
    new_location = ride(loc, line, direction)
    return new_location
    #return ride(loc, line, direction) #a more succinct return statement