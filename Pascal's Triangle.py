#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
row=[1]
listn=[list(row)*i for i in range(1,n+1)]
for i in range(n):
    for j in range(i+1):
        if i==0 or j==0 or j==i:
            listn[i][j]=1
        else:
            listn[i][j]=int(listn[i-1][j-1])+int(listn[i-1][j])

print(listn[n-1])


# In[ ]:




