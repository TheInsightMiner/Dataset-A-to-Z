#!/usr/bin/env python
# coding: utf-8

# # Mysteries on your dataset

# ## Pandas got your back
# 

# In[65]:


import pandas as pd
df= pd.read_csv("/Users/namansisodia/Downloads/nba (1).csv")
# How Does Your Data Look?
df.head()


# In[66]:


#What are The Datatype ?
df.info()


# In[67]:


# How Big your Data Is?
df.shape


# In[68]:


# Got to Know about missing value in each columns ?
df.isnull().sum()


# In[69]:


# How About a Statical Summary?
df.describe()


# In[70]:


# To Know About Duplicated Value?
df.duplicated().sum()


# In[27]:


# Finally Curises About Column Co-realtion ?
df.corr


# In[ ]:




