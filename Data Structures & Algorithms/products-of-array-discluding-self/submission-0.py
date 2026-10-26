class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        #first prefix, forward pass
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #second suffix, backward pass
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res