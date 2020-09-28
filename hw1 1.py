#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[4]:


a = 0.1
n = 25
I = np.zeros(n+1)
I[0] = math.log(1+a) - math.log(a)
for i in range(n):
    I[i + 1] = 1 / (i + 1) - a * I[i]
plt.plot(I)
print(I)


# In[5]:


a = 10
n = 25
N = 50
I = np.zeros(N)
for i in range(2, N):
    I[N - i] = 1 / a / (N - i) - I[N - i + 1] / a
plt.plot(I)
print(I)


# In[ ]:




