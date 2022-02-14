class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = 0
        merged = []
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += (1 if i < m else 0)
            else:
                merged.append(nums2[j])
                j += (1 if j < n else 0)
        while i < m:
            merged.append(nums1[i])
            i += (1 if i < m else 0)
        while j < n:
            merged.append(nums2[j])
            j += (1 if j < n else 0)
            
        l = m+n
        if l > 0:
            if l % 2 == 0:
                res = (merged[l//2]+merged[(l//2)-1]) / 2
            else:
                res = merged[l//2]
                
        return res
        