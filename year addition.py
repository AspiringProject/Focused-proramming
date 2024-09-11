number = input("Enter a 4-digit number: ")
if len(number) != 4 or not number.isdigit():
    print("Invalid input. Please enter a 4-digit number.")
else:
    number = int(number)
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)

    print("Sum of the digits:", digit_sum)