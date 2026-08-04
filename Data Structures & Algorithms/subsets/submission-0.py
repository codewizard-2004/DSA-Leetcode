class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # Add the number to subset
            curr.append(nums[i])
            dfs(i + 1)

            # Decision: Don't add the subset
            curr.pop()
            dfs(i + 1)
        
        dfs(0)

        return res
        