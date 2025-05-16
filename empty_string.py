def empty_string(string) :
    if len(string) == 0:
        return True
    else :
        return False

string = ""
logic = empty_string(string)
print(logic)

string = "gfk"
logic = empty_string(string)
print(logic)

# repeat a string

def repeat_a_string(string, n) :
    return string * n

string = "abs"
n = 2
logic = repeat_a_string(string, n)
print(logic)

string = "a"
n = 7
logic = repeat_a_string(string, n)
print(logic)