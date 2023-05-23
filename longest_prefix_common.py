class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cnt = ''
        for i in zip(*strs):
            if(len(set(i))==1):
                cnt+=i[0]
            else:
                break
        return cnt