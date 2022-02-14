class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height)-1
        while i < j:
            a = abs(j-i)*min((height[i], height[j]))
            if a > res:
                res = a
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res