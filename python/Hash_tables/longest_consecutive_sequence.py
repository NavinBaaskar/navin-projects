def longest_consecutive_sequence(arr1):
    set1 = set(arr1)
    
    longest_sequence = 0
    
    for i in arr1:
        if i - 1 not in set1:
            current_num = i
            current_seq = 1
            
            while current_num + 1 in set1:
                current_seq += 1
                current_num += 1
            longest_sequence = max(longest_sequence,current_seq)
    return longest_sequence        

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""