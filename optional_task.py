user_number = int(input("Please enter a number of 100 or less: \n"))

while user_number > 100:    # Loop set up to keep going if the number is greater than 100
    user_number = int(input("Try again. Please enter a number of 100 or less: \n"))

if user_number % 2 == 0:    # Using modulus to see if the remainder is 0, therefore even
    result = user_number * 2
    print(f"Your result is {result}.")
else:
    result = user_number * 3    # Simple else statement to multiply odd numbers by 3
    print(f"Your result is {result}.")

# Initially it would do nothing when I entered 100, but this was down to the if/else statements being nested
