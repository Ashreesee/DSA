def difference_between_smallest_and_biggest(numbers) :
    int_number = [int(num) for num in numbers]
    return max(int_number) - min(int_number)

numbers = ["273","100","372","754"]
diff = difference_between_smallest_and_biggest(numbers)
print("The difference between smallest and largest numbers is",diff)