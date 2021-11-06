#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
import numpy as np
na_vals=['NA','Missing']
df=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_public.csv",na_values=na_vals)
schema_df=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_schema.csv",na_values=na_vals,index_col='Column')


# In[19]:


# df.schema()
# df.loc['YearsCode','MainBranch']
schema_df.loc['Column','QuestionText']


# In[29]:


schema_df.sort_index(inplace=True)


# In[30]:


schema_df


# In[25]:


schema_df.sort_index(inplace=True)


# In[27]:


schema_df.tail(20)


# In[ ]:




