def inch_to_feet(num) :
    if num / 12 >= 12 :
        return num / 12
    else :
        return 0

num = 324
result = inch_to_feet(num)
print(result)

num = 3
result = inch_to_feet(num)
print(result)
