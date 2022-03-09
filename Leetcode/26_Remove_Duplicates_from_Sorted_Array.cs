public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int j, k = nums.Length, n = nums.Length;
        for (int i = 0; i < n; i++) {
            j = i;
            k = i+1;
            while (j+1 < n && nums[i] == nums[j+1]) {
                j += 1;
            }
            if (j == nums.Length - 1) break;
            if (j > i) {
                n -= j-i;
                for (int l = j; l < nums.Length; l++) {
                    nums[l-(j-i)] = nums[l];
                }
            }
        }
        
        return k;
    }
}