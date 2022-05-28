public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var d = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (d.ContainsKey(nums[i])) {
                return new int[2] {d[nums[i]], i};
            }
            d.TryAdd(target - nums[i], i);
        }
        return new int[2] {-1, -1};
    }
}