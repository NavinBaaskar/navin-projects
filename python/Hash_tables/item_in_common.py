def item_in_common(list1,list2):
    check_dict = {}
    for i in list1:
        check_dict[i] = True
    
    for j in list2:
        if j in check_dict:
            return True
    return False        




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""