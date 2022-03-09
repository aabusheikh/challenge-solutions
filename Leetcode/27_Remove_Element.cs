public class Solution {
    public int RemoveElement(int[] nums, int val) {
        if (nums.Length == 0) return 0;
        
        int i, j = nums.Length-1;

        for (i = 0; i < j; i++) {
            while (j > i && nums[j] == val) {
                j -= 1;
            }
            
            if (nums[i] == val) {
                nums[i] = nums[j];
                nums[j] = val;
            }
        }
        
        return nums[j] == val ? j : j+1;
    }
}