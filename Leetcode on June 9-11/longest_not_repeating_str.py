class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        maxLen = 0
        left = 0
        for right in range(len(s)):
			# to skip consecutive repeating characters
            while s[right] in store:
                store.remove(s[left])
				# lower window size
                left += 1
            store.add(s[right])
            maxLen = max(maxLen,right - left + 1)
        return maxLen