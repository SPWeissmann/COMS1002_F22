'''
author: Samuel Weissmann
uni: spw2136
2022-09-23

Example of deterministically generated pattern incorporating a W theme.
Appearance of output will differ depending on machine and window size. 
'''
for i in range(10000):
    print('| ', end ='')
    print('\\', end ='') #escape the \ character with \
    print('/', end ='')
    print('\\', end ='') #escape the \ character with \
    print('/', end ='') 
    print(' |', end ='')

