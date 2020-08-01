#!/usr/bin/env python
# coding: utf-8

# Given a string, find the length of the longest substring without repeating characters.
# 
# 	Examples:
# 
# 	Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# 	Given "bbbbb", the answer is "b", with the length of 1.
# 
# 	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# In[87]:


def substring(string):
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


# In[88]:


st =['abcabcbb','pwwkew','bbbbb','bbbbbad']
for i in st:
    res = substring(i)
    Keymax = max(res, key= lambda x: res[x]) 
    print("string :  {}  ,   long_substring : {}".format(i,Keymax)) 


# In[4]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[72]:


def substring(string):
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


# In[86]:


st =['abcabcbb','pwwkew','bbbbb','bbbbbad']
for i in st:
    res = substring(i)
    Keymax = max(res, key= lambda x: res[x]) 
    print("string :  {}  ,   long_substring : {}".format(i,Keymax)) 


# In[ ]:




