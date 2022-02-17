class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs[0]) == 0:
            return res

        a = strs[0]
        for i in range(len(a)):
            for s in strs:
                if i >= len(s) or a[i] != s[i]:
                    return res
            res += a[i]
            
        return res