class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i+len(needle) > len(haystack):
                break
            if haystack[i: i + len(needle)] == needle:
                return i

        return -1