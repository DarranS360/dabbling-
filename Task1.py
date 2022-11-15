number_input = int(input("Give me a number: \n"))

for y in range(1, 13):      # range is 1 - 13 so it counts up to 12
    print('{} * {} = {}'.format(number_input, y, number_input*y))   # same formula as the tables but altered the x
print("")
