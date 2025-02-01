class Solution(object):
    def lengthOfLongestSubstring(self, s:str):
        """
        :type s: str
        :rtype: int
        """
        substring_lengths={}
        for letter in s:
            splitted=s.count(letter)
            print(splitted)

sol=Solution()
sol.lengthOfLongestSubstring("abcabcbb")
        