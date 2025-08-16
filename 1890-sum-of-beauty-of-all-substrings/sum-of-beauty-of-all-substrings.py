class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0] * 26
            maxf = 0
            for j in range(i, n):
                k = ord(s[j]) - 97
                freq[k] += 1
                if freq[k] > maxf:
                    maxf = freq[k]
               
                minf = 10**9
                for c in freq:
                    if c > 0 and c < minf:
                        minf = c
                ans += maxf - minf
        return ans
        