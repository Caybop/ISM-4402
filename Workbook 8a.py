#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "C:\Users\Caden Baucom\datasets\gradedata2.csv"
df = pd.read_csv(Location)
df.head()
df.hist(column="age", by="gender")

