class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        if len(p) == 1 or p[1] != '*':
           
            if s and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        while s and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]): return True
            s = s[1:]
        return self.isMatch(s, p[2:])

