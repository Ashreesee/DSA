
def minutes_to_seconds(minutes) :
    return minutes * 60

minutes = 5
seconds = minutes_to_seconds(minutes)
print(f"{minutes} is equal to {seconds} seconds.")

minutes = 8
seconds = minutes_to_seconds(minutes)
print(f"{minutes} is equal to {seconds} seconds.")

# For desired number

minutes = input ("Enter the number: ")
seconds = int(minutes) * 60
print(f"{minutes} is equal to {seconds} seconds.")

## Convert hours into seconds 

def hours_to_seconds(hours) :
    return hours * 60 * 60

hours = 5
seconds = hours_to_seconds(hours)
print(f"{hours} is equal to {seconds} seconds.")

hours = 8
seconds = hours_to_seconds(hours)
print(f"{hours} is equal to {seconds} seconds.")

# For desired number

hours = input ("Enter the number: ")
seconds = int(hours) * 60 *60
print(f"{hours} is equal to {seconds} seconds.")