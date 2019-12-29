# this is the number it will start at
num = 1

# this is the end of the range of number it checks
fin = 90
run = True


while run:
    if num == 1: # checks if number is equal to 1
        print(num, 'is neither prime nor factorable')
        num += 1
    if num > 1:  # if the number is greater than one
        while run:  # runs the loop
            if num <= fin:  # checks if the number is lower than the final number
                for i in range(2, num): # checks if number is prime
                    if (num % i) == 0:
                        if num <= fin:
                            print(num, 'is not prime')
                            num = num + 1
                        else:
                            pass
                if num < fin:  # if the number is not prime and less than the final number
                    print(num, 'is prime')
                num = num + 1
            elif num > fin:  # if the number is larger than the final number this ends the loops
                run = False
