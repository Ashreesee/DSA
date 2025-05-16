#string to integer

string_number = "699"
integer_number = int(string_number)
print((integer_number))
print(type(integer_number))


# boolean to string

def bool_to_str(flag):
    return str(flag)

flag = True

print(bool_to_str(flag))            
print(type(bool_to_str(flag)))  

#----------2nd approch

bool = False
string = str(bool)
print((string))
print(type(string))

# int to string

integer_number2 = 65
string_number2 = str(integer_number2)
print(string_number2)                 
print(type(string_number2))

# string to int

def string_int(num) :
    return int(num)

num = "12"
logic = string_int(num)
print(logic)
print(type(logic))