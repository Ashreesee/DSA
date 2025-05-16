def calc_fuel(distance) :
    if  distance * 10 > 100 :
        return distance * 10
    else :
        return 100
    
distance = 16
logic = calc_fuel(distance)
print("The fuel needed is", logic)

distance = 7
logic = calc_fuel(distance)
print("The fuel needed is", logic)

distance = 32
logic = calc_fuel(distance)
print("The fuel needed is", logic)