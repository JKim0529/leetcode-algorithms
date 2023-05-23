def twoSum(nums, target):
    for i in range(len(nums)):
        for z in range(1,len(nums)):
            if (nums[i] == target - nums[z]) and (i != z):
                return [i,z]