#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[6]:


toronto_data=pd.read_csv(r'C:\Users\Hp-PC\Desktop\IBM course\Toronto Borough.csv')
df_toronto=pd.DataFrame(toronto_data)
df_toronto.head()


# In[8]:


df_toronto.shape


# In[ ]:




