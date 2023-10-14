class Solution:
    def removeElement(self, nums, val) -> int:
        l = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


print(Solution().removeElement([3,2,2,3], 3))
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
