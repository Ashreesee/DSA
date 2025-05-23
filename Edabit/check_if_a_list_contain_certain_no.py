def check_if_the_list_contains_this(list, item) :
    if item in list :
        return True
    else :
        return False
    
list = [1,4,2,6]
item = 1
logic = check_if_the_list_contains_this(list, item) 
print(logic)

list = [1,4,2,6]
item = 3
logic = check_if_the_list_contains_this(list, item) 
print(logic)