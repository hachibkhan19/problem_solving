def selection_sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        

nums = [5, 6, 3, 2, 7, 8, 3, 2, 1]
selection_sort(nums)
print(nums)
