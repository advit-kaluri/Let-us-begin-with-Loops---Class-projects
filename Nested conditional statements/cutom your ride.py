print("Select the type of the ride \n 1. Normal \n 2. Premium ")

type = input("Enter the type:")

if type == 'Normal':

    print("Enter your choice of vehicle \n 1. Bike 2. Car")

    choice1 = input("Enter the vehical : ")

    if choice1 == 'Bike':

        print("You have choose the Normal ride with Bike. Hero Honda will be assigned")

    elif choice1 == 'Car':

        print("You have choose the Normal ride with Car. 4 seaters car will be assigned")

elif type == 'Premium':

    print("Enter your choice of vehicle \n 1. Bike 2. Car")

    choice2 = input("Enter the vehical : ")

    if choice2 == "Bike":

        print("You have choose the Premium ride with Bike. Royal Enenfield will be assigned")

    elif choice2 == 'Car':

        print("You have choose the Premium ride with Car. 7 seater will be assigned")

