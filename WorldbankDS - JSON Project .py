#!/usr/bin/env python
# coding: utf-8

# # JSON examples and exercise
# ****
# + get familiar with packages for dealing with JSON
# + study examples with JSON strings and files 
# + work on exercise to be completed and submitted 
# ****
# + reference: http://pandas.pydata.org/pandas-docs/stable/io.html#io-json-reader
# + data source: http://jsonstudio.com/resources/
# ****

# In[1]:


import pandas as pd


# ## imports for Python, Pandas

# In[2]:


import json
from pandas.io.json import json_normalize


# ## JSON example, with string
# 
# + demonstrates creation of normalized dataframes (tables) from nested json string
# + source: http://pandas.pydata.org/pandas-docs/stable/io.html#normalization

# In[3]:


# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]


# In[7]:


# use normalization to create tables from nested element
json_normalize(data, 'counties')


# In[8]:


# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])


# ****
# ## JSON example, with file
# 
# + demonstrates reading in a json file as a string and as a table
# + uses small sample file containing data about projects funded by the World Bank 
# + data source: http://jsonstudio.com/resources/

# In[9]:


# load json as string
json.load((open('data/world_bank_projects_less.json')))


# In[10]:


# load as Pandas dataframe
sample_json_df = pd.read_json('data/world_bank_projects_less.json')
sample_json_df


# ****
# ## JSON exercise
# 
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
# 1. Find the 10 countries with most projects
# 2. Find the top 10 major project themes (using column 'mjtheme_namecode')
# 3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

# In[49]:


#Joe's work starts here
import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize


# In[50]:


json_project_df


# In[63]:


json_project_df = 'data/world_bank_projects.json'
json_df = pd.read_json(json_project_df)
print(json_df.shape)
print(json_df.columns)



# In[66]:


worldbank_data = json.load(open(json_project_df))


# In[67]:


#create DataFrame from nested elements with desired columns
d = json_normalize(worldbank_data, 'mjtheme_namecode',['project_name','countryname' ])
d.columns = ['code', 'theme', 'project_name', 'countryname']
d = d.sort_values(by=['countryname'])
type(d)
d


# In[70]:


# return top 10 value_counts on t.countryname
df1 = d.countryname.value_counts()
print('Number of countries with projects: ', df1.shape)
df1.head(10)


# In[71]:


# print top 10 project themes
#Null projects count for 122 so head=11. 
df2 = d.theme.value_counts()
df2.head(11)


# In[75]:


df3 = d.sort_values(by=['theme'])
df3


# In[76]:


blanks = df3[df3.theme=='']
blanks


# In[77]:


#identify code: theme pairs
pairs = set(zip(df3.code, df3.theme))
pairs = [pair for pair in pairs if pair[1]!='']
pairs = dict(pairs)
pairs


# In[78]:


df3.theme = df3.code.map(pairs)


# In[79]:


# An empty dataframe if all empty theme rows have been filled accordingly
blanks2 = df3[df3.theme == '']
print(blanks2.shape)
blanks2


# In[80]:


df3.theme.value_counts().head(10)


# In[ ]:


#Done!

