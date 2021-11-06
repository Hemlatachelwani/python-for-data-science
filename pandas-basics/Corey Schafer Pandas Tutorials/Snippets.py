#!/usr/bin/env python
# coding: utf-8

# In[1]:


people={
    1:"Hemlata",
    2:"Kiran",
    3:"sONA",
    4:"Kiran"
}


# In[7]:


import pandas as pd 
import numpy as np
na_vals=['NA','Missing']
df=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_public.csv",index_col='Respondent',na_values=na_vals)
schema=pd.read_csv(r"C:\Users\chk93\Downloads\archive\survey_results_schema.csv",index_col='Respondent',na_values=na_vals)


# In[4]:


pd.set_option('display.max_columns',80)
pd.set_option('display.max_rows',20)


# In[17]:


df.replace('NA',np.nan,inplace=True)
df.replace('Missing',np.nan,inplace=True)


# In[9]:


df


# In[43]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[44]:


df=pd.DataFrame(people)


# In[45]:


df


# In[46]:


df.dropna()


# In[47]:


df.dropna(axis='index',how='all',subset=['email','last'])


# In[48]:


df.isna()


# In[49]:


df.dtypes


# In[68]:


df.replace('Missing',np.nan,inplace=True)
df.replace('NA',np.nan,inplace=True)


# In[69]:


df['age']=df['age'].astype(float)


# In[70]:


df['age'].astype(float)


# In[71]:


df['age'].mean()


# In[53]:


df.dtypes()


# In[63]:


df.dtypes


# In[64]:


df['age'].mean()


# In[ ]:




