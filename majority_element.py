class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num2 = {i:nums.count(i) for i in set(nums)}
        return max(num2, key = num2.get)  