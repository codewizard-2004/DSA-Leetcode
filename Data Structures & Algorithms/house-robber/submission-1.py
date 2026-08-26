class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in mem:
                return mem[i]
            
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)
            mem[i] = max(rob, skip)
            return mem[i]
        
        return dfs(0)
        