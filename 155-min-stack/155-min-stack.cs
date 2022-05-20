public class MinStack {
    List<int> s;

    public MinStack() {
        s = new List<int>();
       
    }
    
    public void Push(int val) {
        s.Add(val);
        
    }
    
    public void Pop() {
        s.RemoveAt(s.Count-1);
    }
    
    public int Top() {
        return s[s.Count-1];
        
    }
    
    public int GetMin() {
        int min = s[0];
        foreach (int x in s)
        {
            if (x < min)
            min = x;
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */