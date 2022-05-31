public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        
        //list of character counts : list of strings
        var d = new Dictionary<string, List<string>>();
        var res = new List<IList<string>>();
        
        foreach (var str in strs) {
            string sorted = new string(str.OrderBy(x => x).ToArray());
            if (!d.ContainsKey(sorted)) {
                d.Add(sorted, new List<string>());
            }
            d[sorted].Add(str);
        }
        
        foreach (var item in d.Values)
            res.Add(item);
        
        return res;
    }
}