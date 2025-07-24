class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[]
        for num in nums:
            if num!=0:
                arr.append(num)
        count=len(nums)-len(arr)
        arr.extend([0]*count)
        for i in range(len(nums)):
            nums[i]=arr[i]
        return nums

             
