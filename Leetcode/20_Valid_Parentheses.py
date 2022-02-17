pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0 or c not in pairs or pairs[c] != stack[-1]:
                stack.append(c)
            elif c in pairs and pairs[c] == stack[-1]:
                stack.pop()
        return len(stack) == 0