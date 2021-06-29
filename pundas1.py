#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


data = pd.read_csv('ratings.csv')
# data.info()
max_ = data['rating'].max()
data[(data['rating'] == max_)]['movieId'].value_counts().head(1)


# In[9]:


page_url = 'https://fortrader.org/quotes'
df = pd.read_html(page_url, attrs = {'class': 'tabl_quotes'}).head()


# In[ ]:




