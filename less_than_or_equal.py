def less_than_or_equal_to_zero(num) :
    if num <= 0:
        return True
    else :
        return False
    
num = 4 
condition = less_than_or_equal_to_zero(num)
print(condition)

num = 0 
condition = less_than_or_equal_to_zero(num)
print(condition)

num = -3 
condition = less_than_or_equal_to_zero(num)
print(condition)

# less than 100 

def less_than_100(num1, num2) :
    if num1 + num2 <= 100:
        return True
    else :
        return False
    
num1 = 60
num2 = 40
result = less_than_100(num1, num2)
print(result)

num1 = 85
num2 = 72
result = less_than_100(num1, num2)
print(result)

num1 = 36
num2 = 49
result = less_than_100(num1, num2)
print(result)