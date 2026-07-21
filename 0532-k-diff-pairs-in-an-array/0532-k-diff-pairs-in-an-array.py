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



# Better Solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        freq = Counter(nums)
        count = 0

        if k == 0:
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            for num in freq:
                if num + k in freq:
                    count += 1

        return count
