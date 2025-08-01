class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        major=nums[0]
        for i in range(len(nums)):
            if count==0:
                major=nums[i]
                count=1
            elif nums[i]==major:
                count+=1
            else:
                count-=1
        return major



        