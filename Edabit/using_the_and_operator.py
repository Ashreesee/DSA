def and_operator(a, b) :
    if a == True and b == True or a == False and b == False :
        return True
    else :
        return False
      
a = True
b = False
result = and_operator(a, b)
print(result)

a = True
b = True
result = and_operator(a, b)
print(result)

a = False
b = False
result = and_operator(a, b)
print(result)
    