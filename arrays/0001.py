class Solution:
    def two_sum(self, nums, target):
        prev_map = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i


print(Solution().two_sum([2, 7, 11, 15], 9))
