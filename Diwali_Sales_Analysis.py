#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


# import csv file
df = pd.read_csv(r'C:\Users\Tanay\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[7]:


df.info()


# In[8]:


#check for null values
pd.isnull(df).sum()


# In[10]:


# drop null values
df.dropna(inplace=True)


# In[12]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[13]:


df['Amount'].dtypes


# In[11]:


df.columns


# In[14]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[13]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[14]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# ### Gender

# In[15]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[16]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# *From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men*

# ### Age

# In[17]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# *From above graphs we can see that most of the buyers are of age group between 26-35 yrs female*

# ### State

# In[16]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[20]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# *From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively*
# 

# ### Marital Status

# In[21]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married (women) and they have high purchasing power*

# ### Occupation

# In[23]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# *From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector*

# ### Product Category

# In[25]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# *From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category*

# In[27]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[28]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion:
# 
# ### 

# *Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category*

# complete project on YouTube: https://www.youtube.com/@RishabhMishraOfficial
#     
# complete project on GitHub: https://github.com/rishabhnmishra/Python_Diwali_Sales_Analysis

# Thank you!
