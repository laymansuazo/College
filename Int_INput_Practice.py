number = input('Please input an interger ')
if(number.isnumeric()): # only works for positive number
    number = int(number)
    if (number < 20):
        print('Your input'+ str(number) + ' < 20')
    if (number < 10):
        print('Your input'+ str(number) + ' < 10')
else:
    print ('Your input is not an interger or it is negative')