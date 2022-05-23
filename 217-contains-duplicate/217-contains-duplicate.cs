public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> hs = new HashSet<int>();
        foreach (int x in nums)
        {
            if (hs.Contains(x)) {
                return true;
            }
            hs.Add(x);
        }
        return false;
        
        
    }
}