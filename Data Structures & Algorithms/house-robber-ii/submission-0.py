class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, robbed_first):
            if i >= len(nums):
                return 0

            if i == len(nums) - 1 and robbed_first:
                return 0

            if (i, robbed_first) in cache:
                return cache[(i, robbed_first)]

            rob = nums[i] + dfs(i + 2, robbed_first or i == 0)
            skip = dfs(i + 1, robbed_first)

            cache[(i, robbed_first)] = max(rob, skip)
            return cache[(i, robbed_first)]

        return dfs(0, False)