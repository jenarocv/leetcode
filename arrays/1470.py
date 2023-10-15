class Solution:
    def shuffle(self, nums, n):
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
