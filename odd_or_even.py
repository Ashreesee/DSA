def is_the_string_odd_or_even(string) :
    if len(string) % 2 == 0:
        return True
    else :
        return False

string = "apples"
length = is_the_string_odd_or_even(string)
print(length)

string = "les"
length = is_the_string_odd_or_even(string)
print(length)

string = "bles"
length = is_the_string_odd_or_even(string)
print(length)

# given no. is odd or not

def is_odd(num) :
    if num % 2 !=  0 :
        return True
    else :
        return False
    
num = 6
logic = is_odd(num)
print(logic)

num = 25 
logic = is_odd(num)
print(logic)

num = 0 
logic = is_odd(num)
print(logic)

# sum of elements in list is even or odd

def sum_of_element_is_even_or_odd(list) :
    if sum(list) % 2 == 0 :
        return '"Even"'
    else :
        return '"Odd"'
    
list = []
result = sum_of_element_is_even_or_odd(list)
print(result)

list = [9, 0]
result = sum_of_element_is_even_or_odd(list)
print(result)
    
list = [1,3,6]
result = sum_of_element_is_even_or_odd(list)
print(result)