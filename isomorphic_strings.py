from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_map = defaultdict(str)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
           if s[i] in isomorphic_map:
               if isomorphic_map[s[i]] != t[i]:
                     return False

           elif t[i] in isomorphic_map.values():
               if list(isomorphic_map.values()).index(t[i]) != s[i]:
                   return False
           else:
                isomorphic_map[s[i]]= t[i]
            


        return True