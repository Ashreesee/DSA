def sum_of_elements_in_list(list) :
    return sum(list)

list = [3, 7 ,1]
condition = sum_of_elements_in_list(list)
print("The sum of the elements in the list is", condition)

list = [3, 7, 5, 0, 2, 1]
condition = sum_of_elements_in_list(list)
print("The sum of the elements in the list is", condition)

# sum of elements in list is less than 100

def sum_of_elements(list) :
    if sum(list) < 100:
        return True
    else :
        return False

list = [30, 7 ,10]
condition = sum_of_elements(list)
print("The sum of the elements in the list is", condition)

list = [3, 70, 51, 0, 2, 10]
condition = sum_of_elements(list)
print("The sum of the elements in the list is", condition)