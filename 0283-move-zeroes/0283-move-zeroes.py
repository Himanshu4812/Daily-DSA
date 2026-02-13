class Solution(object):
    def moveZeroes(self, nums):
        new_nums = []
        for i in nums:
            if i!=0:
                new_nums.append(i)

        for i in range(len(nums)-len(new_nums)):
            new_nums.append(0)
        
        for i in range(len(nums)):
            nums[i] = new_nums[i]
        