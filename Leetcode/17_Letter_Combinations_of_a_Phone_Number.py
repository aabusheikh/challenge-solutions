buttons = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        if len(digits) > 0:
            res = buttons[digits[0]]
            for d in digits[1:]:
                res = [s+l for l in buttons[d] for s in res]
                        
        return res