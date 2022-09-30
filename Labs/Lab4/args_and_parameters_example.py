#Demonstrating basic argument and parameter behaviors

def print_args(para1, para2, para3 = "p3 default text", para4 = "p4 default text"):
    #para3 and para4 have default values that will be used if no arguments are passed
    #default values are indicated with the = operator in the function header
    print("First argument:", para1)
    print("Second argument:", para2)
    print("Third argument:", para3)
    print("Fourth argument:", para4)
    print() #add extra newline at end of function's print statements

    return None #redundant line.
    #Function will return None by default if there is no return statement

def main():
    arg1 = "One"
    arg2 = "Two"
    arg3 = "Three"
    arg4 = "Four"

    #arguments are assigned to parameters in order specified
    print_args(arg1, arg2, arg3, arg4)
    print_args(arg4, arg3, arg2, arg1) 

    #if no args are passed for parameters with default values, function
    #will use those default values instead
    print_args(arg1, arg2)

    #you must provide an argument for every parameters without a default value.
    #the following line would throw an error:
    #print_args(arg1)

    #can explicitly assign an argument to a particular parameter like this:
    print_args(arg1, arg2, para4=arg3)

    #print VS return
    #What do you think this will print? Think about it before uncommenting
    # print(print_args(arg1, arg2, arg3, arg4))

    return None
