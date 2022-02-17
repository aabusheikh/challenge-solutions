D = {
    'M':  1000,
    'CM': 900,
    'D':  500,
    'CD': 400,
    'C':  100,
    'XC': 90,
    'L':  50,
    'XL': 40,
    'X':  10,
    'IX': 9,
    'V':  5,
    'IV': 4,
    'I':  1
}

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        while len(s) > 0:
            k = s[:2]
            if k in D:
                res += D[k]
                s = s[2:]
            else:
                k = s[:1]
                if k in D:
                    res += D[k]
                    s = s[1:]
        return res
            