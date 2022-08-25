class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i == 4:
                    print(s[i-len(word): i])

                if i - len(word) >= 0 and s[i - len(word) : i] == word and dp[i - len(word)] == True:
                    dp[i] = True
        print(dp)
        return dp[len(s)]
                   
                    
                    
                    