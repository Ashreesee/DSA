def swap_a_and_b(a, b) :
    temp  = a
    a = b
    b = temp
    return [a, b]

a = 100
b = 200
logic = swap_a_and_b(a, b)
print(logic)

