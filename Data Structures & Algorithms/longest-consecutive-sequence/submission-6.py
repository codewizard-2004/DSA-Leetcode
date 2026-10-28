class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in store:
            if (num - 1) not in store:
                streak = 1
                while (num + streak) in store:
                    streak += 1
                res = max(res, streak)

        return res