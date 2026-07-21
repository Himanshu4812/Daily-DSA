class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        arr = set()

        for i in nums:
            if k == 0:
                nums.remove(i)
                if i+k in nums:
                    arr.add((i,i+k))

            elif i+k in nums:
                arr.add((i,i+k))

        return len(arr)
        