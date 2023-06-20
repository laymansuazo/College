x=4
while (x<128):
    x=2*x
    print('x is now', x)
    
# 2 case    
passsword = ''
while passsword != 'Secret':
    passsword = input("Please enter the password ")
    if passsword == 'Secret':
        print('Welcome')
    else:
        print('wrong password, try again') 
# 3 case
x = 1
while x<= 10:
    if x == 5:
        break 
    print(x)
    x+=1
    
#
list=[]
for i in range (2): #0-1
    for j in range (1,3): # 1,2
        list.append(i*j)
        print(list)