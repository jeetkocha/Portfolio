#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import Libraries 

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)


# Read in the data 
df = pd.read_csv(r'/Users/jeetkocha/Desktop/movies.csv')


# In[4]:


# Lets take a look at the data 

df.head()


# In[8]:


# Let's look for any missing data 

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[9]:


# Kind of data types for our columns 

print(df.dtypes)


# In[10]:


df.sort_values(by=['gross'], inplace=False, ascending=False) 


# In[11]:


# Making the rows cleaner 

pd.set_option('display.max_rows', None)


# In[12]:


df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[13]:


# Dropping any duplicates 

df['company'].drop_duplicates().sort_values(ascending=False)


# In[16]:


# Scatter plot Budget vs gross earnings 


plt.scatter(x=df['budget'], y=df['gross']) 

plt.title('Budger vs Gross Earnings')

plt.xlabel('Gross Earnings')

plt.ylabel('Budget for the Flim')

plt.show()




# In[19]:


# Now going to plot budget vs gross earnings using seaborn

sns.regplot(x="gross", y="budget", data=df, scatter_kws={"color": "red"}, line_kws={"color": "blue"})


# In[20]:


# Let's start looking at the correlarion 


# In[27]:


df.corr(method= 'pearson') #As it is the default correlation set up


# In[24]:


# Hence, this proves there is a high correlation between the budget vs gross earnings 


# In[26]:


correlation_matrix = df.corr(method= 'pearson')

sns.heatmap(correlation_matrix, annot=True)

plt.title('Correltion matrix for Numeric Features')

plt.xlabel('Movie Features')

plt.ylabel('Movie Features')

plt.show


# In[28]:


# Look at company 

df.head()


# In[32]:


# Using factorize - this assigns a random numeric value for each unique categorical value

df.apply(lambda x: x.factorize()[0]).corr(method='pearson')


# In[33]:


# Let's visualise these factors 

correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[37]:


correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)


# In[38]:


sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)


# In[39]:


# We can now take a look at the ones that have a high correlation (> 0.5)

strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)


# In[ ]:


# Yearcorrect and the company have the higest correlation 
# My hypothesis was that budget has a correlation with the company

