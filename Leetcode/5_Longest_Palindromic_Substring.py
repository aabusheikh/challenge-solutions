class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l = r = i
            c = True
            while True:
                if s[l] != s[i] or s[r] != s[i]:
                    c = False
                p = s[l:r+1]
                if len(p) > len(res):
                    res = p
                #print(f"i: {i}, p: {p}, res: {res}")

                if r < len(s)-1 and l > 0:
                    if s[l-1] == s[r+1]:
                        l -= 1
                        r += 1
                        continue
                if r < len(s)-1:
                    if s[l] == s[r+1] and c:
                        r += 1
                        continue
                if l > 0:
                    if s[l-1] == s[r] and c:
                        l -= 1
                        continue

                break
        return res