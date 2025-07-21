#!/usr/bin/env python
# coding: utf-8

# # PANDAS
# 

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('services (1).csv')


# In[3]:


df.head()


# In[4]:


df.tail(3)


# In[5]:


type(df)


# In[6]:


list(df.columns)


# In[7]:


df['status']


# In[8]:


df['eligibility']


# In[9]:


df[['eligibility']]


# In[10]:


type(df[['eligibility']])


# In[12]:


df.columns


# In[14]:


df[['email', 'keywords', 'name']]


# In[15]:


df.dtypes


# In[16]:


df1 = pd.read_excel('LUSID Excel - Setting up your market data (2).xlsx')


# In[17]:


df.head()


# In[18]:


df1.columns


# In[19]:


df1[['Unnamed: 6', 'Unnamed: 8']]


# In[20]:


df2 = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[21]:


df2.head()


# In[22]:


df2.columns


# In[23]:


df2.dtypes


# In[25]:


df2[['PassengerId']]


# In[26]:


df2[['PassengerId', 'Survived', 'Pclass', 'Name']]


# In[27]:


df2.tail()


# In[29]:


df2.describe(
)


# In[31]:


df2[['Name','Sex','Ticket','Cabin','Embarked']]


# In[32]:


df2.dtypes == 'object'


# In[34]:


df2.dtypes[df2.dtypes == 'object'].index


# In[36]:


df2[df2.dtypes[df2.dtypes == 'object'].index].describe()


# In[37]:


df2[df2.dtypes[df2.dtypes == 'float64'].index]


# In[38]:


df2[df2.dtypes[df2.dtypes == 'int64'].index]


# In[40]:


df2.columns


# In[44]:


df2[['Ticket', 'Cabin']][2:20:2]


# In[46]:


df2['new_col'] = 0


# In[48]:


df2.head(2)


# In[49]:


df2['New_col1'] = df2['PassengerId'] + df2['Pclass']


# In[50]:


df2


# In[51]:


pd.Categorical(df2['Pclass'])


# In[52]:


pd.Categorical(df2['PassengerId'])


# In[53]:


df2['Cabin'].unique()


# In[55]:


df2[df2['Age']>18]


# In[56]:


df2[df2['Fare']>32.20]


# In[57]:


df2[df2['Fare'] ==0]


# In[58]:


df2[df2['Sex'] == 'male']


# In[59]:


df2['Sex'] == 'male'


# In[60]:


df2[df2['Survived'] == 1 ]


# In[61]:


df2[(df2['Sex'] =='female') & (df2['Fare'] >32)]


# In[65]:


df2[(df2['Sex'] == 'female')  | (df2['Fare'] > 32 )]


# In[66]:


df2[(df2['Sex'] =='male') & (df2['Fare'] >32)]


# In[69]:


df2[df2['Fare'] == max(df2['Fare'])]['Name']


# In[74]:


df2[257:258]


# In[75]:


df2[['PassengerId','Survived','Pclass']][0:2]


# In[78]:


df2.iloc[0:10,[0,1,2,4,5]]


# In[80]:


df2.loc[0:2,['PassengerId','Survived','Pclass', 'Age']]


# In[82]:


df.iloc[0:12, [2,3,4,5]]


# In[ ]:




