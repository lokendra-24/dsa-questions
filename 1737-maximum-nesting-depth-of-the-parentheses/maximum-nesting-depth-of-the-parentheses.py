class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        ans = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > ans:
                    ans = depth
            elif ch == ')':
                depth -= 1
        return ans
        