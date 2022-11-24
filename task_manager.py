from datetime import datetime       # Imported datetime to use today's date for task input later

now = datetime.now()        # Get today's date
date_now = now.strftime("%d/%m/%Y")     # format the date, so it is in the format of day/month/year

# Login section
while True:
    username = input("Please enter your username: \n").lower()
    password = input("Please enter your password: \n")
    user_pass = f"{username}, {password}"       # Combine username and password to match format in txt file

    with open("user.txt", "r") as user:
        for line in user:
            if user_pass in line:       # Checking if combined username password is in user.txt
                access = True
                break
            else:
                access = False

    if access:      # If access is true, welcome message printed and use allowed into programme menu
        print("\nWelcome")
        break
    elif not access:        # If access false, error message printed
        print("\nIncorrect Username or Password. Please try again.\n")

# Operation section
while True:
    if username != "admin":     # While loop for regular user
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
''').lower()

    elif username == "admin":       # While loop for admin with extra option ds (display stats)
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display stats
e - Exit
''').lower()

    # register user section
    if menu == 'r' and username == "admin":     # Access only if admin
        while True:
            new_user = input("What is the username of the new user?\n").lower()
            new_password = input("What will their password be?\n")
            password_check = input("Please confirm the new password... \n")
            if password_check != new_password:      # Added a check to confirm password
                print("Sorry, the passwords do not match. Please try again.")
            elif password_check == new_password:
                with open("user.txt", "a") as user:
                    user.write(f"\n{new_user}, {new_password}")     # Format info and print is (username, password)
                    print(f"New user: \"{new_user}\" confirmed.\n")
                    break

    elif menu == "r" and username != "admin":       # Error message if user is not admin
        print("You are not authorised to add a new user. Please select another option.\n")

    # add task section
    elif menu == 'a':
        while True:
            assigned_user = input("Which user is the task to be assigned to?\n").lower()
            with open("user.txt", "r") as user:
                check_user = user.read()    # Lines to ensure a user exists in user.txt to assign tasks to
                if assigned_user in check_user:
                    break
                else:
                    print("Sorry, no user exists. Please try again.\n")
        task = input("What is the new task?\n").capitalize().strip()
        task_description = input("Please give a brief description of the task:\n").capitalize().strip()
        date_due = input(f"When is the task \"{task}\" due? (please enter date in the format: dd/mm/yyyy)\n").strip()
        task_complete = "No"
        # Capitilse and strip before writing to file for formatting, more pleasing to the eye later on
        # File open below and info written, using today's date from string at beginning using datetime
        with open("tasks.txt", "a") as tasks:
            tasks.write(f"\n{assigned_user}, {task}, {task_description}, {date_now}, {date_due}, {task_complete}")
        print(f"Task \"{task}\" confirmed for user \"{assigned_user}\".\n")

    # view all tasks section
    elif menu == 'va':
        with open("tasks.txt", "r") as tasks_all:
            for line in tasks_all.readlines():      # Read line by line to gather info
                temp_view = line.strip().split(", ")  # Split lines at the "," to sep out user, task, etc. into list
                user = temp_view[0]
                task = temp_view[1]
                task_description = temp_view[2]
                date_assigned = temp_view[3]
                date_due = temp_view[4]
                task_complete = temp_view[5]
                # Above gets place in list of each type of info (user, task, etc.)
                view_all = "----------------------------------------------------------------------------------\n" \
                           f"Task: \t \t \t \t {task}\n" \
                           f"Assigned to: \t \t {user}\n" \
                           f"Date assigned: \t \t {date_assigned}\n" \
                           f"Due date: \t \t \t {date_due}\n" \
                           f"Task complete? \t \t {task_complete}\n"\
                           f"Task description: \t {task_description}\n" \
                           f"------------------------------------------------------------------------------------\n"
                # Above is format of output, \ stops the error message that would otherwise occur
                print(view_all)

    # View my tasks section
    elif menu == 'vm':
        with open("tasks.txt", "r") as tasks_all:
            for line in tasks_all.readlines():
                if username in line:        # This added line checks for the current user's tasks
                    temp_view = line.strip().split(", ")
                    user = temp_view[0]
                    task = temp_view[1]
                    task_description = temp_view[2]
                    date_assigned = temp_view[3]
                    date_due = temp_view[4]
                    task_complete = temp_view[5]

                    view_all = "----------------------------------------------------------------------------------\n" \
                               f"Task: \t \t \t \t {task}\n" \
                               f"Assigned to: \t \t {user}\n" \
                               f"Date assigned: \t \t {date_assigned}\n" \
                               f"Due date: \t \t \t {date_due}\n" \
                               f"Task complete? \t \t {task_complete}\n"\
                               f"Task description: \t {task_description}\n" \
                               f"------------------------------------------------------------------------------------\n"

                    print(view_all)
                    break
            else:
                print("You have no tasks to show.\n")       # Message if user does not exist in tasks.txt

    elif menu == "ds" and username == "admin":      # Line states will only show info if user is admin
        with open("user.txt", "r") as users_all:
            user_count = sum(1 for line in users_all if line.rstrip())  # Count number of lines in file for num of users
        with open("tasks.txt", "r") as tasks_all:
            tasks_count = sum(1 for line in tasks_all if line.rstrip()) # Count number of lines in file for num of tasks
            print(tasks_count)
            print(user_count)
            ds_print = "--------------------------------------\n" \
                       f"Number of Users: \t {user_count}\n" \
                       f"Number of Tasks: \t {tasks_count}\n" \
                       f"--------------------------------------\n"
            print(ds_print)

    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again.\n")
