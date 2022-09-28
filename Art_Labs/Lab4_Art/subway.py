# The subway module contains functions relating to subways
from random import choice #makes choice function from random module available
LINES = ["A","B","C","D"] 

def ride(loc, line, direction):
    x,y = loc #list expansion. Assigns x = loc[0] and y = loc[1].

    if line == "A" or line == "D": #A and D are express lines
        if direction == "up":
            y += 16
        elif direction == "down":
            y -= 16
    if line == "B" or line == "C": #B and C are local lines
        if direction == "up":
            y += 8
        elif direction == "down":
            y -= 8
    
    location = [x,y]
    return location

def next_train(loc):
    line = choice(LINES)
    direction = choice(["up","down"])
    return ride(loc, line, direction)