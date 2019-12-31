run = True
while run:  # Starting the loop
    current_principal = input("What is your up front current principal? (Type exit to quit) ")
    # Getting the users input for their starting balance
    if current_principal == 'exit':
        run = False
        # if the input string matches 'exit' then the program quits
    else:
        current_principal = int(current_principal)
        # Converts the input to an integer
        years = int(input("How many years are you going to leave this account? "))
        # Collects the input of years as an integer
        interest_rate = int(input("What is the interest rate yearly? ")) / 100
        # Collects the input of the interest rate as an integer and divides by 100 to get the 'percentage'
        one = (current_principal * (1 + interest_rate)**years)
        # compound interest formula
        one = round(one, 2)
        # rounding the integer to match a dollar amount
        one = str(one)
        # putting the total into a string to concatenate the $ sign
        print('your total savings is', '$' + one)
