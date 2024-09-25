global total1
global total2
total1 = 0
total2 = 0

def filmTimes():
    print("Beetlejuice Beetlejuice 12A: 15:20, 16:50, 17:50")
    print("Speak No Evil 15: 15:40, 18:20, 21:00")
    print("Interstellar (10th Anniversary) 12A: 19:00")
    print()

def bookTickets(child, adult, family, senior):
    global total2
    childPrice = 9.50
    adultPrice = 12.50
    familyPrice = 40.00
    seniorPrice = 10.00
    total2 = (child * childPrice) + (adult * adultPrice) + (family * familyPrice) + (senior * seniorPrice)
    print("Total cost: £", total2)

def orderFood(popcorn, drink, hotdog):
    global total1
    popcornPrice = 5.50
    drinkPrice = 2.50
    hotdogPrice = 4.00
    total1 = (popcorn * popcornPrice) + (drink * drinkPrice) + (hotdog * hotdogPrice)
    print("Total cost: £", total1)

go_again = True
print("Welcome to the Best Cinema!")
while go_again == True:
    choice = input("Enter option 1, 2, 3 or any other key to exit:\n1. Film times\n2. Book tickets\n3. Order food\n")
    if choice == "1":
        filmTimes()
    elif choice == "2":
        child = int(input("Enter number of child tickets: "))
        adult = int(input("Enter number of adult tickets: "))
        family = int(input("Enter number of family (2 Adult, 2 child, 2 Senior) tickets: "))
        senior = int(input("Enter number of senior tickets: "))
        bookTickets(child, adult, family, senior)
    elif choice == "3":
        popcorn = int(input("Enter number of popcorn (£5.50): "))
        drink = int(input("Enter number of drinks (£2.50): "))
        hotdog = int(input("Enter number of hotdogs (£4.00): "))
        orderFood(popcorn, drink, hotdog)
    else:
        go_again = False
        print("Your total cost is: £", total1 + total2)