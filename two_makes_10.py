def two_makes_10(num1, num2) :
    if num1 + num2 == 10 or num1 ==10 or num2 == 10:
        return True
    else : 
        return False
    
num1 = 10
num2 = 1
condition = two_makes_10(num1, num2)
print(condition)

num1 = 4
num2 = 2
condition = two_makes_10(num1, num2)
print(condition)

num1 = 7
num2 = 3
condition = two_makes_10(num1, num2)
print(condition)