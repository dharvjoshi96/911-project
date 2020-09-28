#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np


# In[5]:


from pandas import DataFrame, Series


# In[6]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


df = pd.read_csv('C:\\Users\\18623\\Documents\\Python\\911.csv')


# In[12]:


df.head()


# In[14]:


df = df.rename(columns={'lat':'Latitude', 'twp':'Township',  'lng': 'Longitude', 'addr': 'Address',
                        'title' : 'Title', 'timeStamp': 'TimeStamp', 'descerption': 'Description'})


# In[15]:


df.head()


# In[16]:


df.info()


# # 1. What are the top 5 zip code for 911 calls?
# 

# In[17]:


df['zip'].head()


# In[18]:


df['zip'].value_counts().head()


# # 2. what are the top 5 townships for 911 calls? 

# In[19]:


df['Township'].head()


# In[20]:


df['Township'].value_counts().head()


# # 3. how many unique title codes are there in the 'Title' column?

# In[21]:


df['Title'].head()


# In[22]:


df['Title'].unique()


# In[23]:


df['Title'].nunique()


# # In the titles column there are "Reasons/Departments" specified before the title code. These are'EMS', 'Fire' and 'Traffic'.
# # Separate the Reasons in the new column Reasons.

# In[24]:


df['Title'].head()


# In[25]:


df['Reasons'] = df['Title'].apply(lambda a:a.split(':')[0])


# In[26]:


df['Reasons'].head()


# In[27]:


df.head()


# #   what is the most common reason for 911 calls based of this new column?

# In[28]:


df['Reasons'].value_counts()


# In[29]:


sns.countplot(x ='Reasons',data=df,palette= 'viridis')


# In[30]:


type(df['TimeStamp'].iloc[0])


# In[31]:


df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])


# # Grab specific attribute from datetime object by calling them and create 3 new colums Hour, Month and Day of Week
# # from TimeStamp Column

# In[32]:


Time = df['TimeStamp'].iloc[0]


# In[33]:


Time.hour


# In[34]:


Time


# In[35]:


df['Hour'] = df['TimeStamp'].apply(lambda time:time.hour)


# In[38]:


df.head()


# In[37]:


df['Month'] = df['TimeStamp'].apply(lambda Time:Time.month)


# In[39]:


df['Day of week'] = df['TimeStamp'].apply(lambda Time:Time.dayofweek)


# In[41]:


df.head()


# In[42]:


dmap = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}


# In[43]:


df['Day of week'] = df['Day of week'].map(dmap)


# In[45]:


df.head()


# # Create a countplot of Reasons based on day of week.

# In[81]:


plt.figure(figsize=(12,6))
sns.countplot(x='Day of week', data = df, hue='Reasons' ,palette = 'mako' )


# In[80]:


plt.figure(figsize=(12,6))
sns.countplot(x='Month', data= df, hue= 'Reasons', palette = 'viridis')


# In[49]:


ByMonth = df.groupby('Month').count()


# In[50]:


ByMonth.head()


# In[51]:


ByMonth['Latitude'].plot()


# In[82]:


plt.figure(figsize=(10,4))
sns.countplot(x='Month', data=df, palette= 'viridis')


# In[107]:


ByMonthdata = ByMonth.reset_index()
ByMonthdata


# # Create new column called 'Date' that contains the date from 'TimeStamp' column

# In[55]:


Date = df['TimeStamp'].iloc[0]


# In[56]:


Date


# In[57]:


df['Date'] = df['TimeStamp'].apply(lambda Date:Date.date())


# In[58]:


df.groupby('Date').count()


# # Groupby this Date column with count() aggregate and create a plot of counts of 911 calls.

# In[59]:


df.groupby('Date').count()['Latitude'].plot(figsize=(12,5))
plt.tight_layout()


# In[ ]:





# # Recreate a plot and aslo separate 3 plots with each plots reprensting Reasons for 911 calls.

# In[64]:


df[df['Reasons']== 'Traffic'].groupby('Date').count()['Latitude'].plot(figsize=(12,5))
plt.title('Traffic')
plt.tight_layout()


# In[65]:


df[df['Reasons']== 'Fire'].groupby('Date').count()['Latitude'].plot(figsize=(12,5))
plt.title('Fire')
plt.tight_layout()


# In[66]:


df[df['Reasons']== 'EMS'].groupby('Date').count()['Latitude'].plot(figsize=(12,5))
plt.title('EMS')
plt.tight_layout()


# In[75]:


DayHour = df.groupby(by=['Day of week','Hour']).count()


# In[77]:


DayHour


# # Restructur the dataframe so that columns becomes Hour and Index becomes Day of Week. create heatmaps with seaborn on data.

# In[91]:


DayHour = df.groupby(by=['Day of week','Hour']).count()['Reasons'].unstack()


# In[92]:


DayHour


# In[95]:


plt.figure(figsize=(12,6))
sns.heatmap(DayHour, cmap = 'viridis')
plt.title('Heatmap for Reasons')


# In[97]:


sns.clustermap(DayHour, cmap = 'viridis')
plt.title('Clustermap for call Reasons during week days')


# In[100]:


DayMonth = df.groupby(by=['Day of week','Month']).count()['Reasons'].unstack()


# In[101]:


DayMonth


# In[104]:


plt.figure(figsize=(12,6))
sns.heatmap(DayMonth, cmap='coolwarm')


# In[105]:


sns.clustermap(DayMonth, cmap='coolwarm')


# In[ ]:




