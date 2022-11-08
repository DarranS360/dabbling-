import math

product_type = input("""Choose either 'investment' or 'bond' from the list below: \n
Investment \t - \t to calculate the amount of interest you'll earn on your investment
Bond \t\t - \t to calculate the amount you'll pay on a home loan\n""").lower().strip()

if product_type == "investment":
    deposit = float(input("How much would you like your initial deposit to be?\n"))
    interest_rate = float(input("What is your interest rate? (please enter the number without the % sign)\n"))
    invest_years = float(input("How many years will you save for?\n"))
    interest_type = input("Would you like 'simple' or 'compound' interest?\n").lower().strip()

    if interest_type == "simple":
        total_saved = deposit * (1 + (interest_rate / 100) * invest_years)
        total_interest = total_saved - deposit
        print(f"Your total amount saved is £{total_saved:.2f}, which includes interest of £{total_interest:.2f}.")

    elif interest_type == "compound":
        interest_corrected = interest_rate / 100
        total_saved = deposit * math.pow((1 + interest_corrected), invest_years)
        total_interest = total_saved - deposit
        print(f"Your total amount saved is £{total_saved:.2f}, which includes interest of £{total_interest:.2f}.")

elif product_type == "bond":
    house_value = int(input("How much is the house currently worth?\n"))
    interest_rate = float(input("What is your interest rate? (please enter the number without the % sign)\n"))
    repay_months = float(input("How many months will take to repay the bond?\n"))
    interest_corrected = (interest_rate / 100) / 12
    monthly_repayment = (interest_corrected * house_value) / (1 - (1 + interest_corrected) ** (- repay_months))
    print(f"""Your monthly repayments will be £{monthly_repayment:.2f}.
This is based on the value of the house being £{house_value}, your interest rate of {interest_rate}%, 
and with monthly repayments spread out over {repay_months} months""")

# The first part was straight forward for me using previous materials
# However the formula for bond took me a bit to get my head around:
# It wasn't clear that the interest had to be divided by 100 and then again by 12
# It also took me  a quick check on stack overflow to know ^ meant **, which may have been mentioned and I missed it
# Where would I use ^ in future, as it said it would not work with int or float
# I added the .strip() because if the user is like me, they automatically hit space bar for some strange reason lol
# Is there a way to take an input, like house price, and ignore a "," if someone says 315,000 rather than 315000?
