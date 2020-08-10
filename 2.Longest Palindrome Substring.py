#!/usr/bin/env python
# coding: utf-8

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# 	Example 1:
# 
# 	Input: "babad"
# 	Output: "bab"
# 	Note: "aba" is also a valid answer.
# 	Example 2:
# 
# 	Input: "cbbd"
# 	Output: "bb"

# In[1]:


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1

        start, end = 0, 0
        for index in range(len(s)):
            even_len = expand(s, index, index+1)
            odd_len = expand(s, index, index)
            length = max(even_len, odd_len)
            if length > (end-start):
                start = index - (length-1)//2
            end = index +length//2

        return s[start:end+1]


# In[2]:


s = Solution()
s.longestPalindrome("babad")


# In[ ]:


#output
#'aba'

