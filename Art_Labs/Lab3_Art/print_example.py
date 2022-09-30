'''
author: Samuel Weissmann
uni: spw2136
2022-09-23
'''
#Compare these print statements to see the effects produced with different
#arguments, and consider how these may affect your lab assignment

#default
print("default:")
print("One big string")
print("Multiple","strings")
print("This is one big string.","This","is","not") 

#compare sep
print("\n\nmodifying sep:")
print("One big string")
print("Multiple","strings",sep="")
print("This is one big string.","This","is","not",sep="")

#compare end
print("\n\nmodifying end:")
print("One big string")
print("Multiple","strings",end="")
print("This is one big string.","This","is","not",end="")
