class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        s = str(x)
        m = 1
        if s[0] == '-':
            m *= -1
            s = s[1:]

        for c in s:
            res += m*int(c)
            m *= 10
            
        if res < -1*pow(2, 31) or res > (pow(2, 31)-1):
            res = 0
            
        return res