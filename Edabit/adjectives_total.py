def total_amount_adjectives(dict):
    return len(dict)

dict = "moron", "idiot", "stupid"
total = total_amount_adjectives(dict)
print(total) 

# greeting 

def greeting(name):
    if name == "Mubashir":
        return "Hello, Sir!"
    else:
        return "Hello, " + name + "!"
    
name = "ashree"
condition = greeting(name)
print(condition)

name = "Mubashir"
condition = greeting(name)
print(condition)

# Another greeting logic

def greet(name) :
    return f'"Hello {name}!"'

name =  "Anisha"
result = greet(name)
print(result)
