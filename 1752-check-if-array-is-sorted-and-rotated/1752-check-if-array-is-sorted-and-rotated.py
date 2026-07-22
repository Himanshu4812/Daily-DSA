class Solution:
    def check(self, nums: List[int]) -> bool:
        newNums = sorted(nums)
        arr = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr.append(nums[j])
            for k in range(0, i):
                arr.append(nums[k])
            if newNums == arr:
                return True
            else:
                arr = []
        return False

        