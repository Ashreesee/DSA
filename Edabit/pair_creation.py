def make_pair(num) :
    return list(num)

num = (32,1)
logic = make_pair(num)
print(logic)

# repeat first three character 3 times

def front(txt) :
    return (txt[0] + txt[1] + txt[2]) * 3

txt = "python"
condition = front(txt)
print(condition)
