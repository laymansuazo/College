def square(x):
    y = x*x
    return y

result = square(10)
print(result)

def greater_than(x,y):
    if x > y:
        return True
    else:
        return False

a=2
b=3 
result = greater_than(2,3)
print("{} is greater than {}: {}".format(a,b,result))

def get_factors (x):
    factors=[]
    for i in range (1, x + 1):
        if(x%i == 0 ):
            factors.append(i)
    return factors

print (get_factors(21))
#
def vowel_counter(string):
    vowel_count= 0
    for char in string:
        if char in 'aeiou':
            vowel_count +=1
    return vowel_count

def main():
    while 1 == 1:
        input_string = input("enter a string; ")
        if input_string == '-1':
            break
        print (vowel_counter(input_string), "vowels in",input_string)
        
#to execute main
if __name__== '__main__':
    main()