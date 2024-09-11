def milliliters_to_liters(ml):
    return ml / 1000

def liters_to_milliliters(l):
    return l * 1000

choice = input("Enter '1' to convert milliliters to liters or '2' to convert liters to milliliters: ")

if choice == '1':
    ml = float(input("Enter the value in milliliters: "))
    liters = milliliters_to_liters(ml)
    print(f"{ml} milliliters is equal to {liters} liters.")
elif choice == '2':
    l = float(input("Enter the value in liters: "))
    milliliters = liters_to_milliliters(l)
    print(f"{l} liters is equal to {milliliters} milliliters.")
else:
    print("Invalid choice. Please enter either '1' or '2'.")