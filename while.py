number = int(input("Please enter a number: \n"))
total = 0   # I will use total/count to give me the average
count = 0

while number > -1:
    number = int(input("Please enter a number (I wonder what happens when you enter '-1'?...): \n"))
    total += number
    count += 1

    if number == -1:
        total += 1              # Adding 1 to the total and -1 to the count is the easiest way I found to adjust
        count = count - 1
        average = total / count
        print(round(average))

# I wonder if there is a better way to adjust for the final -1 command to stop
# Any easier way to not count it?
# I think using lists may make this code smoother, but it works all the same
