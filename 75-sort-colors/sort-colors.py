class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_0=0
        count_1=0
        count_2=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_0+=1
            elif nums[i]==1:
                count_1+=1
            else:
                count_2+=1
        nums.clear()
        nums.extend([0]*count_0)
        nums.extend([1]*count_1)
        nums.extend([2]*count_2)
        



        