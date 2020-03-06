# linear search algorithm
pos = 0

def linear_search(nums, n):

    for i in range(len(nums)):
        if nums[i] == n:
            globals() ['pos'] = i
            return True

    else:
        return False            

nums = [4, 6, 7, 2, 3, 8, 9]
n = 7

if linear_search(nums, n):    
    print("Found", pos+1)

else:
    print("Not Found")   
