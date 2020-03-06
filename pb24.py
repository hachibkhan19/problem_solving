# Binary search
def binary_search(nums, n):
    l = 0
    u = len(nums)-1

    while l <= u:
        mid = (l+u) // 2        
        if nums[mid] == n:
            return True
        else:
            if nums[mid] < n:
                l = mid + 1
            else:
                u = mid -1
        
            
nums = [ 23, 45, 45, 56, 78, 90]
n = 23

if binary_search(nums, n):
    print("Found")
else:
    print("Not Found")
