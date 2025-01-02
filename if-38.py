A = -1
while(A < 0):
    A = int(input('Please enter your number: '))
    if(A < 0):
        print('Please insert number that is greater than zero or Equal')
    else:
        if(A < 50):
            print('Fail')
        else:
            print('Pass')
            break