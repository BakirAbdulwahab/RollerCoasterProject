print("Welcome to the rollercoaster!")

customerHeight = int(input("What is your height in cm? "))

bill = 0

if customerHeight >= 120:
    print("You can ride the rollercoaster!")
    ageOfCustomer = int(input("What is your age??"))
    if ageOfCustomer < 12:
        bill = 5
        print("Child Ticket Will Be, $5.")
    elif ageOfCustomer <= 18:
        bill = 7
        print("Youth Ticket Will Be, $7.")
    else:
        bill = 12
        print("Adult Ticket Will Be, $18.")
    photoRequest = input("Do you want your photo taken? Y or N?")
    if photoRequest == "Y":
        #Add $3 to their bill.
        bill += 3

    print(f"your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")