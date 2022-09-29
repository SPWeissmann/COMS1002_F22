'''
Samuel Weissmann
spw2136 

A program that lets the user explore NYC
'''
import bicycle as bike

def main ():
    energy = 100 #expend 1 energy every two blocks biked.
    location = [0,0] #starting location

    choice = 0 #controls the while loop
    while choice != 4:
        #print user status 
        print("You are located at: ", location, sep="")
        print("Remaining energy: ", energy, "%", sep="")

        #get user choice
        display_menu()
        choice = int(input("Select an option: "))

        #use chosen transportation method
        if choice == 1: #riding bike
            distance = int(input("Enter the number of blocks to ride: "))
            direction = input("Pick a direction (n, s, e, or w): ")
            energy_expended = 0.5 * distance
            if energy_expended <= energy:
                energy -= energy_expended #deduct energy
                location = bike.ride(location, distance, direction) #FUNCTION CALL
            else:
                print("You are too tired to bike that far")

    return None #Not strictly required

#displays a menu of the different transportation options to the user
def display_menu():
    print("TRANSPORTATION OPTIONS: ")
    print("1) Ride Bicycle")
    print("4) Quit")
    return None

#call main function to run the program
main()
