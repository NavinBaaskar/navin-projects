def find_longest_string1(string_list):
    if string_list == []:
        return ""
    long_str = string_list[0]
    j = 0
    i = 1
    count = 0
    while i < len(string_list):
        count += 1
        if len(string_list[i]) > len(string_list[j]):
            long_str = string_list[i]
            j = i 
            i += 1
        else:
            i += 1
    print(count)
    return long_str

def find_longest_string(string_list):
    longest_string = ""
    count = 0
    for string in string_list:
        count += 1
        if len(string) > len(longest_string):
            longest_string = string
    print(count)        
    return longest_string    

string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""