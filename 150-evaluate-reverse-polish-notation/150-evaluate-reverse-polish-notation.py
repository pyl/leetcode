class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        
        for x in tokens:
            if x == "+":
                s.append(int(s.pop()) + int(s.pop()))
            elif x == "*":
                s.append(int(s.pop()) * int(s.pop()))
            elif x == "/":
                s2 = float(s.pop())
                s1 = float(s.pop())
                s.append(int(s1 / s2))
            elif x == "-":
                s2 = int(s.pop())
                s1 = int(s.pop())
                s.append(s1 - s2)
            else:
                s.append(x)
        return s.pop()
                
