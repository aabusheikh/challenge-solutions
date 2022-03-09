public class Solution {
    public int StrStr(string haystack, string needle) {
        if (needle.Length == 0) return 0;
        
        int i = -1, j = 0;
        
        for (int si = 0; si < haystack.Length; si++) {
            //Console.WriteLine($"haystack[si]: {haystack[si]}, needle[j]: {needle[j]}");
            if (haystack[si] == needle[j]) {
                if (i == -1) i = si;
                j++;
                if (j >= needle.Length) {
                    return i;
                }
            }
            else {
                if (i >= 0) si = i;
                i = -1;
                j = 0;
            }
        }
        
        if (j < needle.Length) {
            i = -1;
        }
        return i;
    }
}