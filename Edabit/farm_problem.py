def calc_total_legs(chicken, cow, sheep) :
    return (chicken * 2) + (cow * 4) + (sheep * 4)

chicken = 4
cow = 2
sheep = 1
legs = calc_total_legs(chicken, cow, sheep)
print("The total number of legs: ", legs)

chicken = 2
cow = 5
sheep = 6
legs = calc_total_legs(chicken, cow, sheep)
print("The total number of legs: ", legs)

chicken = 4
cow = 8
sheep = 10
legs = calc_total_legs(chicken, cow, sheep)
print("The total number of legs: ", legs)