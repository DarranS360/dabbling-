countdown_num = 20

while countdown_num > 0:
    print(countdown_num)
    countdown_num -= 1  # Print -= to print an int one less than previous from 20 down

print("\n")     # Used this to seperate lines of code, wonder if there is better way?...

for i in range(1, 21):  # range goes to 21 to compensate and print the 20 and not 21
    if i % 2 == 0:  # modulus 2 w/ remainder of 0 means is even
        print(i)

print("\n")

star_rows = 5       #
for i in range(0, star_rows):
    for j in range(0, i + 1):   # Inner loop deals with the number of *, or columns
        print("*", end="")      # telling python to print * in each place and end="" so that the end is whitespace
    print("")

print("\n")

first_num = int(input("Give me the first number: \n"))
second_num = int(input("Give me the second number: \n"))
for i in range(1, second_num + 1):  # loop will check number from 1 to the second number, +1 to compensate
    if first_num % i == 0 and second_num % i == 0:  # loop checking that the i is divisible into both nums
        hcf = i
print(f"The highest common factor of {first_num} and {second_num} is {hcf}.")

# StackOverflow helped me find the way to tell python to print * in place, and also the end=" "
# Which I understand to mean the end is defined by whitespace rather than a new line
