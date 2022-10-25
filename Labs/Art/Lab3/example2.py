'''
author: Samuel Weissmann
uni: spw2136
2022-09-23

Example of a pattern incorporating both random and deterministic design 
to create a randomly alternating W/M theme.
'''
from random import choice
from random import seed
seed(88) #any number will do

for i in range(1000):
    print(choice(["M","W"]), sep="", end="")
    for j in range(3):
        print("┌┐","├┤", sep="", end = "")
