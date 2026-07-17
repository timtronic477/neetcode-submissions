class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        value = [0] *26
        for i in range(0, len(s)):
            value[ord(s[i])-ord("a")] += 1
            value[ord(t[i]) - ord("a")] -= 1
        
        for i in value:
            if i != 0:
                return False
        return True

