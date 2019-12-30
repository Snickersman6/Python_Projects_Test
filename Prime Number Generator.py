def number_range():
    #  Defining the function

    num = int(input("Where should we start? "))
    # this is the number it will start at

    fin = int(input("Where should we finish? "))
    # this is the end of the range of number it checks

    run = True
    while run:  # Starting the loop
        if num == 1:  # checks if number is equal to 1
            print(num, 'is neither prime nor factorable')
            num += 1
        if num > 1:  # if the number is greater than one
            while run:  # runs the loop
                if num <= fin:  # checks if the number is lower than the final number
                    for i in range(2, num):  # checks if number is prime
                        if (num % i) == 0:
                            if num <= fin:
                                is_prime = 'no'
                                print(num, 'is not prime')
                                num = num + 1
                            else:
                                pass
                    if num < fin:  # if the number is not prime and less than the final number
                        is_prime = 'yes'
                        print(num, 'is prime')
                    num = num + 1
                elif num > fin:  # if the number is larger than the final number this ends the loops
                    run = False


number_range()  # calling the function
