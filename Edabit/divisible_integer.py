def if_the_integer_is_divisible_by_five(num) :
    if num % 5 == 0:
        return True
    else :
        return False
    
num = -55
condition = if_the_integer_is_divisible_by_five(num)
print(condition)

num = 64
condition = if_the_integer_is_divisible_by_five(num)
print(condition)

num = 5
condition = if_the_integer_is_divisible_by_five(num)
print(condition)

#divisible by 100

def if_the_integer_is_divisible_by_100(num) :
    if num % 100 == 0:
        return True
    else :
        return False
    
num = 800
condition = if_the_integer_is_divisible_by_100(num)
print(condition)

num = 6
condition = if_the_integer_is_divisible_by_100(num)
print(condition)

num = -100
condition = if_the_integer_is_divisible_by_100(num)
print(condition)

# divides evenly
def if_the_integer_is_divisible(num1, num2) :
    if num1 % num2 == 0:
        return True
    else :
        return False

num1 = 85
num2 = 4
condition = if_the_integer_is_divisible(num1, num2)
print(condition)

num1 = 98
num2 = 7
condition = if_the_integer_is_divisible(num1, num2)
print(condition)