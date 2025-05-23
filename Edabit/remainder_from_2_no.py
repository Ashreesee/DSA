def remainder_from_the_num( dividend, divisor) :
    return dividend % divisor 

dividend = 17
divisor = 4
remainder = remainder_from_the_num( dividend, divisor)
print("The remainder is: ", remainder)

dividend = input("Enter the number: ")
divisor = input("Enter the number: ")
remainder = int(dividend) % float(divisor)
print("The remainder is: ", remainder)

# mod of numbers

def mod_of_numbers(num1, num2) :
    return num1 % num2

num1 = 55
num2 = 12
mod = mod_of_numbers(num1, num2) 
print("The mod is: ",mod)