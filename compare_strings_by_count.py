def compare_string_by_count_of_characters(string1, string2) :
    if len(string1) == len(string2) :
        return True
    else :
        return False

string1 = "AUBVF"
string2 = "VBHFD"
result = compare_string_by_count_of_characters(string1, string2)
print(result)

string1 = "hello"
string2 = "vccvcvcaca"
result = compare_string_by_count_of_characters(string1, string2)
print(result)