#!/usr/bin/env python
# coding: utf-8

# In[4]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '1848c6af-a2fe-463b-840b-7f57d1048c32',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[5]:


type(data)


# In[6]:


import pandas as pd


pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)


# In[7]:


# Normalizes the dataframe

df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('today')
df


# In[8]:


df


# In[9]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e) 
    
    df2 = pd.json_normalize(data['data'])
    df2['Timestamp'] = pd.to_datetime('today')
    df = df.append(df2)
    
    


# In[10]:


# Running the API

import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[11]:


df


# In[12]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[13]:


df


# In[14]:


# Taking a look at coin trends 

df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[15]:


df4 = df3.stack()
df4


# In[16]:


type(df4)


# In[17]:


df5 = df4.to_frame(name='values')
df5


# In[20]:


df5.count() 


# In[34]:


# Since the data is not structed well let's not pass a column as an index instead i created a range and passed that as the data frame

index = pd.Index(range(90))


df6 = df5.reset_index()
df6 


# In[35]:


# Rename 

df7 = df6.rename(columns={'level_1': 'percent_change'})
df7


# In[39]:


# Change the values for better presentation 

df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h', '24h','7d','30d','60d','90d'])
df7


# In[37]:


# Now let's visualise this data

import seaborn as sns
import matplotlib.pyplot as plt


# In[40]:


sns.catplot(x='percent_change', y='values', hue='name', data=df7, kind='point') 


# In[ ]:




