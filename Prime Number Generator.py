num = 9999999
i = 1
run = True

while run:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, 'is not prime')
                num = num + 1
        else:
            print(num, 'is prime')
        num = num + 1
