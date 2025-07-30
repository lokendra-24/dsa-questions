class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,max_count=0,0
        for num in range(len(nums)):
            if nums[num]==1:
                count+=1
            else:
                count=0
            max_count=max(count,max_count)
        return max_count
             
