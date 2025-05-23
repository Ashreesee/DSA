def power_calc( voltage, current) :
    return voltage * current

voltage = 16
current = 2
power = power_calc( voltage, current)
print("The power is: ", power)

# power calc

def power_calculation( k , n) :
    if k ** k == n :
        return True
    else :
        return False

k = 2
n = 4
result = power_calculation( k , n)
print(result)

k = 9
n = 387420489
result = power_calculation( k , n)
print(result)

k = 6
n = 40
result = power_calculation( k , n)
print(result)