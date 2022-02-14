class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {}
        i = j = 0
        res = 0
        while i <= j and j < len(s):
            if s[j] in track:
                new_i = track[s[j]]+1
                while i < new_i:
                    track.pop(s[i])
                    i += 1
            track[s[j]] = j
            
            length = j - i + 1
            if length > res:
                res = length
                
            j += 1
                
        return res