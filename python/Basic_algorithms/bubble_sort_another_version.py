def bubble_sort(my_list):
    
    for i in range(len(my_list)-1):
        swapped = False
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j+1]:
                my_list[j],my_list[j + 1] = my_list[j+1],my_list[j]
                swapped = True
        if swapped == False:
            break
    return my_list  






          








my_list = [8,4,3,2,7,1]

bubble_sort(my_list)

print(my_list)