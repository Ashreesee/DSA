def profitable_gamble(prob, prize, pay) :
    if prob * prize > pay :
        return True
    else :
        return False 
    
prob = 0.2
prize = 50
pay = 9
result = profitable_gamble(prob, prize, pay)
print(result)

prob = 0.9
prize = 3
pay = 2
result = profitable_gamble(prob, prize, pay)
print(result)

prob = 0.9
prize = 1
pay = 2
result = profitable_gamble(prob, prize, pay)
print(result)