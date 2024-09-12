def convert_miles(miles):
    km = miles * 1.6 
    return km

def convert_km(km):
    miles = km / 1.6
    return miles

while True:
    unit = input("Enter the unit you want to convert to (miles or km): ")
    distance = float(input("Enter the distance: "))
    if unit.lower() == "miles":
        print(convert_miles(distance),"km")

    elif unit.lower() == "km":
        print(convert_km(distance),"miles")

    else:
        print("Invalid unit")