#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[3]:


df.head()


# In[4]:


df.tail(3)


# In[5]:


df.columns


# In[6]:


s = df['Name'][0:20]


# In[7]:


s


# In[8]:


len(s)


# In[11]:


s = df['Name'][0:10]


# In[12]:


l = ['sudh','b','c','d','e','f','g','h','i','j']


# In[13]:


s1 = pd.Series(list(s), index=l)


# In[14]:


s


# In[15]:


s1


# In[16]:


s1[0]


# In[17]:


s1['sudh']


# In[20]:


s4 = pd.Series([3,4,5,6,6] , index=[2,4,5,6,1])


# 

# In[21]:


s4


# In[22]:


s5 = pd.Series([34,345,45,45,454] , index=[9,4,5,6,7])


# In[23]:


s4*s5


# In[24]:


s4+s5


# # Part-> 4

# In[25]:


df.head()


# In[26]:


df.drop('PassengerId', axis=1, inplace=True)


# In[27]:


df


# In[28]:


df.drop(3,inplace=True)


# In[29]:


df


# In[30]:


df.set_index('Name', inplace=True)


# In[31]:


df


# In[32]:


df.reset_index()


# In[34]:


d ={
    'Key1' : [3,4,5,6,7],
    'Key2' : [5,6,7,8,9],
    'Key3' : [4,5,6,7,8]
}


# In[35]:


pd.DataFrame(d)


# In[36]:


df1 = pd.read_csv('taxonomy.csv (1).xls')


# In[37]:


df1


# In[38]:


df1.dropna()


# In[39]:


df1.dropna(inplace=True)


# In[40]:


df1


# In[41]:


df1.dropna(axis=1)


# In[42]:


df2 = pd.read_csv('taxonomy.csv (1).xls')


# In[43]:


df2


# In[44]:


df2.dropna(axis=1)


# In[45]:


df2.fillna('adnan')


# In[46]:


df


# In[47]:


df.reset_index(inplace=True)


# In[48]:


df


# In[49]:


g = df.groupby('Survived')


# In[50]:


g


# In[53]:


g.sum()


# In[54]:


g.mean()


# In[55]:


g1 = df.groupby('Pclass')


# In[56]:


g1.sum()


# In[57]:


df5 = df[['Name',	'Survived',	'Pclass']][0:5]


# In[58]:


df6 = df[['Name',	'Survived',	'Pclass']][5:10]


# In[59]:


df5


# In[60]:


df6


# In[61]:


pd.concat([df5,df6])


# In[62]:


df7 = pd.concat([df5,df6], axis=1)


# In[63]:


df7


# In[64]:


data1 = pd.DataFrame({'key1':[1,2,4,5,6],
                      'key2':[4,5,6,7,8],
                      'key3':[3,4,5,6,6]
}
)


# In[65]:


data2 = pd.DataFrame({'key1':[1,2,45,6,67],
                      'key4':[56,5,6,7,8],
                      'key5':[3,56,5,6,6]
}
)


# In[66]:


pd.merge(data1,data2)


# In[67]:


pd.merge(data1,data2, how='left')


# In[68]:


pd.merge(data1,data2,how = 'right')


# In[69]:


pd.merge(data1,data2,how = 'cross')


# In[70]:


df


# In[71]:


df['Fare_INR'] = df['Fare'].apply(lambda x: x*80)


# In[72]:


df


# In[73]:


df['Name_len'] = df['Name'].apply(len)


# In[74]:


df


# In[81]:


def Cat_fare(x):
    if x<10:
        return "Cheap"
    elif x>=10 and x<20:
        return "Mid"
    else:
        return "High"
    
df['Categ_Fare'] = df['Fare'].apply(Cat_fare)


# In[82]:


df['Categ_Fare'] = df['Fare'].apply(Cat_fare)


# In[83]:


df


# In[2]:


#Python Pandas - Date Functionality
import pandas as pd
date = pd.date_range(start='2023-04-23' , end = '2023-06-23')


# In[3]:


import numpy as np


# In[8]:


df_date = pd.DataFrame({'date':date})


# In[9]:


df_date


# In[10]:


df_date.dtypes


# In[11]:


df7 = pd.DataFrame({'date':['2023-06-23', '2023-06-22', '2023-06-20']})


# In[12]:


df7


# In[14]:


df7['Updated_date'] = pd.to_datetime(df7['date'])


# In[15]:


df7


# In[16]:


df7['Year'] = df7['Updated_date'].dt.year


# In[17]:


df7


# In[22]:


df7['Month'] = df7['Updated_date'].dt.month


# In[23]:


df7['Day'] = df7['Updated_date'].dt.day


# In[24]:


df7


# In[25]:


#Python Pandas - Categorical Data

data = ["sudh" , "krish" , "hitesh" , "navin","sudh" ,"sudh" ]


# In[26]:


categ = pd.Categorical(data)


# In[27]:


categ


# In[29]:


categ.value_counts()


# In[30]:


#Python Pandas – Visualization


# In[31]:


d = pd.Series([1,2,3,3,5,6,6,8])
d


# In[32]:


d.plot()


# In[33]:


df = pd.DataFrame({
    'a' : [3,4,5,6,7],
    'b' : [4,5,6,7,8]
})


# In[34]:


df


# In[35]:


df.plot(x='a', y='b')


# In[36]:


df.plot.scatter(x='a', y='b')


# In[37]:


df


# In[38]:


d = pd.Series([1,2,3,3,5,4,2,6,6,8,9,1])


# In[39]:


d


# In[40]:


d.plot.pie()


# In[41]:


d.value_counts(
)


# In[ ]:




