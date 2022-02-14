class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        m = n = 1
        while True:
            if x // (m*10) == 0:
                break
            m *= 10
            
        while m >= n:
            a = (x % (m*10)) // m
            b = (x % (n*10)) // n
            
            if a != b:
                return False
            
            m //= 10
            n *= 10
            
        return True