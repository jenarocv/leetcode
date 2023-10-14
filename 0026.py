class Solution:
    def removeDuplicates(self, nums) -> int:
        l = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1
        return l


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(Solution().removeDuplicates([1, 1, 2]))
