class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or len(s) == 0 or s.isspace():
            return 0
        
        res = 0
        s = s.strip()

        m = 1
        if s[0] == "-":
            m = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for i in range(len(s)):
            if not s[i].isnumeric():
                s = s[:i]
                break

        m *= pow(10, (len(s)-1))
        for c in s:
            res += m*int(c)
            m //= 10
            
        max_int = pow(2, 31)-1
        min_int = pow(2, 31)*-1
        if res > max_int:
            res = max_int
        if res < min_int:
            res = min_int

        return res