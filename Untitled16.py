#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("C:\\Users\\megha\\Desktop\\data analysis\\covid19_italy_province.csv")


# In[16]:


data.shape


# In[17]:


data.head()


# In[8]:


data.columns


# In[18]:


data.tail()


# In[19]:


data.isnull().sum()


# In[24]:


data.describe()


# # relating the variables wit scatterplots
# 

# In[ ]:





# In[21]:


sns.relplot(x="Recovered",y="Deaths",data=data)


# In[26]:


sns.relplot(x="NewPositiveCases",y="Deaths",hue='Recovered',data=data)


# In[ ]:


sns.pairplot(data)


# In[ ]:


sns.relplot(x='HomeConfinement', y='TotalPositiveCases',kind='line',data=data)


# In[32]:


data.columns


# In[ ]:


sns.catplot(x='Recovered',y='NewPositiveCases',data=data)


# In[ ]:


dataframe1=pd.DataFrame({
    
    
    
})

