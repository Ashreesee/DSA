def area_tri( base, height) :
    return base * height / 2

base = 4
height = 9
area = area_tri( base, height)
print("Area of triangle: ", area)

base = 51
height = 3
area = area_tri( base, height)
print("Area of triangle: ", area)


# For desired numbers

base = input("Enter the base value: ")
height = input("Enter the height value: ")
area = float(base) * int(height) / 2
print("Area of triangle: ", area)

#area of rectangle

def area_of_rec(length, width) :
    return length * width

length = 3
width = 7
arearec = area_of_rec(length, width)
print(arearec)