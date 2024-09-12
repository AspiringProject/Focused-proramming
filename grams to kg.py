def gtokg(g):
    return g / 1000

def kgtog(kg):
    return kg * 1000

choice = input("Enter '1' to convert g to kg or '2' to convert kg to g: ")

if choice == '1':
    g = float(input("Enter the value in g: "))
    kg = gtokg(g)
    print(f"{g} g is equal to {kg} kg.")
elif choice == '2':
    kg = float(input("Enter the value in kg: "))
    g = kgtog(kg)
    print(f"{kg} kg is equal to {g} g.")
else:
    print("Invalid choice. Please enter either '1' or '2'.")