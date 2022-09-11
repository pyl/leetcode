class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length;
        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] == target) {
                return m;
            }
            if (target < nums[m]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return -1;
    }
}