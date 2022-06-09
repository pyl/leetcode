public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] res = new int[nums.Length];
        int temp = 1;
        
        //get product from left
        for (int i = 0; i < nums.Length; i++) {
            res[i] = temp;
            temp *= nums[i];
        }
        temp = 1;
        
        
        //get product from right
        for(int i = nums.Length - 1; i >= 0; i--) {
            res[i] *= temp;
            temp *= nums[i];
        }
        return res;
    }
}