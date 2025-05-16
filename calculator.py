def calculator(txt) :
    parts = txt.split()
    a, op, b = parts
    a = int(a)
    b = int(b)
    if op == '+' :
        return a + b
    elif op == '-' :
        return a - b 
    elif op == '*' :
        return a * b
    elif op == '/' :
        return a / b 
    else :
        return "Error"
    
txt = "4 + 8"
logic = calculator(txt)
print(logic)

txt = "9 * 0"
logic = calculator(txt)
print(logic)

