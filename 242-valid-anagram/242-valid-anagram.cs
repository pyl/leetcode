public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary <char, int> d = new Dictionary<char, int>();
        foreach (char c in s) {
            if (d.ContainsKey(c)) {
                d[c] += 1;
            } else {
                d[c] = 1;
            }
        }
        foreach (char c in t) {
            if (d.ContainsKey(c)) {
                d[c] -= 1;
            } else {
                return false;
            }
        }
        foreach (var (key, val) in d) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}