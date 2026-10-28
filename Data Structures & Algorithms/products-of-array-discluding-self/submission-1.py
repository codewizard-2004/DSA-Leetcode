class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        
        res = [1] * len(nums)
        left = 1
        right = 1

        for i in range(len(nums)):
            res[i] = left
            left = left * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
