class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        temp=dict()
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]]=[i]
            else:
                temp[nums[i]].append(i)
        for j in temp:
            if len(temp[j])>1:
                for z in range(len(temp[j])-1):
                    if temp[j][z+1]-temp[j][z] <=k:
                        return True
        return False