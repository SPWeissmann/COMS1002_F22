#Demonstrating basic argument and parameter behaviors

def print_args(para1, para2, para3, para4):
    # para3 and para4 have default values that will be used if no arguments 
    # are passed. Default values are indicated with the = operator in the 
    # function header

    print("First argument:", para1)
    print("Second argument:", para2)
    print("Third argument:", para3)
    print("Fourth argument:", para4)
    print() #add extra newline at end of function's print statements

    return None #redundant line.
    #Function will return None by default if there is no return statement

def main():
    arg1 = "Argument One"
    arg2 = "Argument Two"
    arg3 = "Argument Three"
    arg4 = "Argument Four"

    #arguments are assigned to parameters in order specified
    #compare the two different print statements to see the difference
    print_args(arg1, arg2, arg3, arg4)
    print_args(arg4, arg3, arg2, arg1)

    #default values will be used if no args are passed
    print_args(arg1, arg2)

    #can explicitly assign an argument to a particular parameter like this:
    print_args(arg1, arg2, para4=arg3)

    #you must provide an argument for every parameters without a default value.
    #the following line would throw an error:
    #print_args(arg1)

    #print VS return
    #What do you think this will print? Think about it before uncommenting
    # print(print_args(arg1, arg2, arg3, arg4))


main()
