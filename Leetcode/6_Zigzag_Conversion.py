class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [""]*(min((numRows, len(s))))
        r = 0
        d = -1
        for c in s:
            rows[r] += c
            if r == 0 or r == len(rows)-1:
                d *= -1
            r += d
        
        return "".join(rows)