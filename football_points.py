def football_point( wins, draws, loses) :
    return ((wins * 3) + (draws * 1)) - (loses * 0.5)

wins = 4
draws = 2
loses = 1
point = football_point( wins, draws, loses)
print("The total football points are: ", point)

wins = 5
draws = 1
loses = 2
point = football_point( wins, draws, loses)
print("The total football points are: ", point)

wins = 7
draws = 4
loses = 3
point = football_point( wins, draws, loses)
print("The total football points are: ", point)

# basketball points

def basketball_points(threepointers, twopointers) :
    return (threepointers*3) + (twopointers*2)

threepointers = 4
twopointers = 18
total = basketball_points(threepointers, twopointers)
print("The total points are", total)

threepointers = 7
twopointers = 12
total = basketball_points(threepointers, twopointers)
print("The total points are", total)
