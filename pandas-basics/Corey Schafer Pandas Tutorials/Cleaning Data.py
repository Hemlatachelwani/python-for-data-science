#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


na_vals=['NA','Missing']


# In[6]:


df=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_public.csv",index_col='Respondent',na_values=na_vals)
schema=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_schema.csv",index_col='Respondent',na_values=na_vals)


# In[ ]:


pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',20)


# In[ ]:


df.head()


# In[9]:


pd.set_option('display.max_columns',80)
pd.set_option('display.max_rows',20)


# In[10]:


df.head()


# In[ ]:




