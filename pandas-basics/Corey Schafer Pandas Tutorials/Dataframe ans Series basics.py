#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[33]:


df={
    "first":"hemu",
    "last":"chelwani",
    "email": "phil@email.com"
}


# In[3]:


people={
    "first":["hema","kiru"],
    "last":["ch","ch"],
    "email":["hema.ch@email.com","kiru.ch@email.com"]
}


# In[5]:


df=pd.DataFrame(people)
df.email


# In[6]:


people["email"]


# In[7]:


df


# In[8]:


type(df)


# In[9]:


type(df["email"])


# In[10]:


df.email


# In[13]:


type(df[["last","email"]])


# In[14]:


df.columns


# In[15]:


df.iloc[0]


# In[16]:


type(df.iloc[0])


# In[34]:


res_df = pd.read_csv(r'C:\Users\chk93\Downloads\archive\survey_results_public.csv')
schema_df = pd.read_csv(r'C:\Users\chk93\Downloads\archive\survey_results_schema.csv')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[21]:


res_df.shape


# In[22]:


df.loc[[0,1]]


# In[28]:


df.loc[[0,1],['email']]


# In[31]:


df.iloc[[0,1],0]


# In[35]:


res_df['Hobbyist']


# In[36]:


res_df['Hobbyist'].value_counts()


# In[40]:


res_df.iloc[[0,1]]


# In[41]:


res_df.loc[[0,1]]


# In[42]:


res_df.columns


# In[59]:


res_df.loc[[0,1,2],'Respondent']


# In[61]:


# res_df.loc[0:2]
res_df.loc[[0,1,2],'MainBranch']


# In[62]:


res_df.loc[0:2]


# In[64]:


res_df.loc[0]


# In[66]:


res_df.loc[0:2,'']


# In[ ]:




