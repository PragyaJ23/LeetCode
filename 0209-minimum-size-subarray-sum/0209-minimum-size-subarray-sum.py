class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] > len(nums) // 2:
                return num

nums = [3, 2, 3]

s = Solution()
print(s.majorityElement(nums))

nums=[3,2,3]
s=Solution()
s.majorityElement(nums)
        