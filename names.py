roll_call = True    # This boolean seems to make the code tidier and allows me to end the loop by = False

students = 0
names_students = input("Please name each of your students. You can type 'stop' to finish: \n").lower()

while roll_call:    # Originally I had while roll_call == True, but quickly realised the == True is redundant
    students += 1   # To add to students each time it loops
    names_students = input("Please name each of your students. You can type 'Stop' to finish: \n").lower()
    if names_students == "stop":
        print(f"You have a total of {students} students.")
        roll_call = False

# This was nice and easy, I think I have done it the most succinct and elegant way I can
# Use while, booleans, and if statements 
