def find_max_min(arr1):
    max_ele = arr1[0]
    min_ele = arr1[0]
    
    for val in arr1:
        if val > max_ele:
            max_ele = val
        if val < min_ele:
            min_ele = val
    return (max_ele,min_ele)        


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""