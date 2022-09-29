'''
Sam Weissmann
spw2136 

A program that lets the user explore NYC 
'''
import subway
import bicycle as bike
#import new_transit as 

def main ():
    remaining_fare = 100 #decrease as one rides public transit 
    energy = 100 #decreases as one uses a bike, skateboard, etc
    location = [0,0] #starting location

    choice = 0 #controls the while loop
    while choice != 4:
        #print user status 
        print("You are located at: ", location, sep="")
        print("Remaining fare: $", remaining_fare, sep="")
        print("Remaining energy: ", energy, "%", sep="")

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
        elif choice == 2: #riding a bicycle
            distance = int(input("Enter the number of blocks to ride: "))
            direction = input("Pick a direction (n, s, e, or w): ")
            energy_expended = 0.5 * distance
            if energy_expended <= energy:
                energy -= energy_expended #deduct energy
                location = bike.ride(location, distance, direction)
            else:
                print("You are too tired to bike that far")

    return None

def display_menu():
    print("TRANSPORTATION OPTIONS")
    print("1) Ride subway")
    print("2) Ride bicycle")
    #add third transit option here
    print("4) Quit")
    return None

#call main function to run the program
main()