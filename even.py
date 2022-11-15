user_num = int(input("Please enter a number: \n"))
number = 0                                          # we want this to be 1 and not 0 so it prints from 2 and not 0

while number <= user_num:                           # While loop set up to run till we reach the user input number
    if number % 2 == 0:                             # Using modulus to indicate the even numbers
        print("{0}".format(number))
    number = number + 1

# I found the vey useful {0}.format() on StackOverflow
# I used it above to tell python to print each number that is even, replacing the {0} with the number each time
# Loop terminates when number == user_num
