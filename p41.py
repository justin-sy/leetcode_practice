class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = nums + [0]
        for i in range(len(nums)):
            if nums[i] != "Present":
                index = nums[i]
                while  0 < index < len(nums) and nums[index] != "Present":
                    nums[index], index = "Present", nums[index]               

        for i in range(1,len(nums)):
            if nums[i] != "Present":
                return i
        return len(nums)