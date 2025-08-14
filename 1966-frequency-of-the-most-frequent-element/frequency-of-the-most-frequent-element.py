class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        l = 0
        total = 0  
        ans = 1

        for r, x in enumerate(nums):
            total += x
            
            while x * (r - l + 1) - total > k:
                total -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
