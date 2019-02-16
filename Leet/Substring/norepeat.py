class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxSub = 0
        curr = 0
        last = 0
        dic = {}
        for i in range(len(s)):
            curr+=1
            if s[i] in dic:
                if curr - 1 > maxSub:
                    maxSub = curr - 1
                index = dic[s[i]]
                if last <= index:
                    curr = curr - (index - last) - 1
                    last = index + 1
            dic[s[i]] = i

        if curr > maxSub:
                    maxSub = curr

        return maxSub      

a = Solution()

print a.lengthOfLongestSubstring("abababbaba") 
