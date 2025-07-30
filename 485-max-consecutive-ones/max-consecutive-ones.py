class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,maxi_count=0,0
        for num in range(len(nums)):
            if nums[num]==1:
                count+=1
            else:
                count=0
            maxi_count=max(count,maxi_count)
        
        return maxi_count