def max_edge_of_triangle( a, b) :
    return (a + b) - 1
a = 4
b = 8
edge = max_edge_of_triangle( a, b)
print("The maximum edge of the triangle: ", edge) 

a = 12
b = 21
edge = max_edge_of_triangle( a, b)
print("The maximum edge of the triangle: ", edge)

a = 11
b = 5
edge = max_edge_of_triangle( a, b)
print("The maximum edge of the triangle: ", edge)

# For desired value

a = input("The value for side 1: ")
b = input("The value for side 2: ")
edge = (int(a) + int(b)) -1
print(f"The max edge for {a} and {b} are: ", edge)