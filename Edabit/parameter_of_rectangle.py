def param_of_rectangle( length, breadth) :
    return 2 * (length + breadth)

length = 4
breadth = 9
param = param_of_rectangle( length, breadth)
print("Parameter of rectangle: ", param)

length = 51
breadth = 3
param = param_of_rectangle( length, breadth)
print("Parameter of rectangle: ", param)


# For desired numbers

length = input("Enter the length value: ")
breadth = input("Enter the breadth value: ")
param = 2 * (float(length) + int(breadth))
print("Parameter of rectangle: ", param)

