class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        total=0
        res=float('inf')
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                res=min(res,right-left+1)
                total-=nums[left]
                left+=1
        return 0 if res == float('inf') else res
nums=[2,3,1,2,4,3]
target=7
s=Solution()
s.minSubArrayLen(target,nums)
        