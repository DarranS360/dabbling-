start_year = int(input("What year do you want to start with? \n"))
check_year = int(input("How many years do you want to check? \n"))

for i in range(start_year, start_year + check_year + 1):    # adding the 1 to compensate for range
    if i % 4 == 0 and (i % 100 != 0):  # % == 4 will show leap years as 0 will be remainder
        print(f"{i} is a leap year.")   # these lines to check normal year is a leap year

    elif i % 400 == 0 and i % 100 == 0: # To check if a century year is a leap year
        print(f"{i} is a leap year.")

    else:
        print(f"{i} is not a leap year.")

# I wonder if there is a better/alternative way to compensate for the range to include the years inputted
# So if someone enters 10 year it does from 1 to 10 and not 1 to 9
# Originally just had % 4 == 0 to check leap year but then found out that century years work a bit differently
# Thus checking for division by 100 and 400
