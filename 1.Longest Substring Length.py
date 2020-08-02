#!/usr/bin/env python
# coding: utf-8

# Given a list of strings, find the longest substring with length without repeating characters.
# 
# 	Examples:
#     
#     string_list = ['abcabcbb','bbbbb','bbbbbad','pwwkew']
# 
# 	Given String1 : "abcabcbb", the answer is "abc", which the length is 3.
# 
# 	Given String2 : "bbbbb", the answer is "b", with the length of 1.
#     
#     Given String3 : "bbbbbad", the answer is "bad", with the length of 3. 
# 
# 	Given String4 : "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a 
#                     subsequence and not a substring.
#      

# In[1]:


def long_substr(string):
    i = 0
    char_str = []
    str_list = []
    str_dict = {}
    while(i<len(string)): 
        if string[i] not in char_str:
            char_str.append(string[i])
            
        else:
            s = "".join(char_str)
            str_dict[s] = len(char_str)
            str_list.append(char_str)
            char_str=[]
            char_str.append(string[i])
        if i == len(string)-1:
            str_list.append(char_str)  
            s = "".join(char_str)
            str_dict[s] = len(char_str)
        i += 1
    return str_dict


# In[2]:


string_list =['abcabcbb','bbbbb','bbbbbad','pwwkew']
for i in string_list:
    res = long_substr(i)
    max_key = max(res, key= lambda x: res[x]) 
    print("str :  {}    ,   long_substr : {}  ,  substr_len : {}".format(i,max_key,res[max_key])) 


# In[3]:


#Output

#str :  abcabcbb  ,   long_substr : abc  ,  substr_len : 3
#str :  bbbbb     ,   long_substr : b    ,  substr_len : 1
#str :  bbbbbad   ,   long_substr : bad  ,  substr_len : 3
#str :  pwwkew    ,   long_substr : wke  ,  substr_len : 3


# In[ ]:




