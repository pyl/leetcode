public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> hs = new HashSet<int>(nums);
        int streak = 0;
        foreach (int x in hs) {
            Console.WriteLine("X is " + x);
            if (!hs.Contains(x - 1)) {
                //start of the streak
                int upper = x;
                int count = 1;
                while(hs.Contains(upper + 1)) {
                    upper += 1;
                    count += 1;
                }
                streak = Math.Max(streak, count);
            }
        }
        return streak;
    }
}