def largest_number(numbers) :
    int_numbers = [int(num) for num in numbers]
    return max(int_numbers)

numbers = ["273","32","372","754"]
largest = largest_number(numbers)
print("The largest number is: ", largest)

def smallest_number(numbers) :
    int_numbers = [int(num) for num in numbers]
    return min(int_numbers)

numbers = ["273","32","372","754"]
smallest = smallest_number(numbers)
print("The smallest number is: ", smallest)