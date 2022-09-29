'''
Sam Weissmann
spw2136 

A program that lets the user explore NYC
'''
import subway

def main ():
    remaining_fare = 100 #decreases as one rides public transportation
    location = [0,0] #starting location

    choice = 0 #controls the while loop
    while choice != 4:
        #print user status 
        print("You are located at: ", location, sep="")
        print("Remaining fare: $", remaining_fare, sep="")

        #get user input
        display_menu()
        choice = int(input("Select an option: "))

        #use chosen transportation method
        if choice == 1: #riding subway
            line = input("Pick a line to ride (A, B, C, or D): ")
            direction = input("Pick a direction to ride (up or down): ")
            if remaining_fare >= 2.75:
                remaining_fare -= 2.75 #deduct fare
                location = subway.ride(location, line, direction) #update location
            else:
                print("Insufficient fare")

    return None

def display_menu():
    print("TRANSIT OPTIONS: ")
    print("1) Ride subway")
    print("4) Quit")
    return None

#call main function to run the program
main()
