def concat_two_list( list1, list2) :
    return list1 + list2

list1 = [1, 3, 5]
list2 = [2, 6, 8]
concat = concat_two_list(list1, list2)
print(concat)

# Return the last element of the list

def last_element(list) :
    return list[-1]

list = [7, 2, 5]
result = last_element(list)
print(result)

list = [7, 2, 5, 1, 9]
result = last_element(list)
print(result)

# concat name

def concat_name(first, last) :
    return f'"{last},{first}"'

first = "John"
last = "Doe"
logic = concat_name(first, last)
print(logic)

# concat first aand last character

def concat_character(name) :
    return name[0] + name[-1]

name = ("ashree")
condition = concat_character(name)
print(condition)