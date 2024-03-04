def rotate1(nums, k):
    
    for i in range(k):
        temp = nums[-1]
        for j in range(len(nums) - 2,-1,-1):
            
            nums[j + 1] = nums[j]
            
        nums[0] = temp
    
def rotate(nums, k):
    k = k % len(nums)
    print(k)
    nums[:] = nums[-k:] + nums[:-k]    


nums = [1, 2, 3, 4, 5, 6, 7]
k = -3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""