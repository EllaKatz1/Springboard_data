#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


#Data loading:
Phenotypes = pd.read_csv(r"C:\Users\Ella Katz\Desktop\Post-doc\Personal\Springboard\git_hub_projects\Second_capstone\Datasets\All_Data_emmeans_info_V1.csv")
Classifications = pd.read_csv(r"C:\Users\Ella Katz\Desktop\Post-doc\Personal\Springboard\git_hub_projects\Second_capstone\Datasets\Seeds_classification.csv")
Environmental_data = pd.read_csv(r"C:\Users\Ella Katz\Desktop\Post-doc\Personal\Springboard\git_hub_projects\Second_capstone\Datasets\Environmental_data.csv")


# In[11]:


print(Phenotypes.shape)
print(Classifications.shape)
print(Environmental_data.shape)


# In[13]:


print(Phenotypes.head())
print(Classifications.head())
print(Environmental_data.head())


# In[14]:


for col in Phenotypes.columns:
    print(col)


# In[18]:


#Data joining:
Data = pd.merge(Phenotypes, Classifications, how="left", on="CS_number")
Data_1 = pd.merge(Data, Environmental_data, how="left", on="CS_number")

print(Phenotypes.shape)
print(Environmental_data.shape)
print(Data_1.shape)


# In[19]:


for col in Data_1.columns:
    print(col)


# In[21]:


#Data Organization:
#Deleting duplicated and unnecessary columns:
Data_2 = Data_1
Data_2 = Data_2.drop(["name_x", "country_x", "collector", "seq_by", "lng", "lat", "name_y", "country_y"], axis=1)


# In[31]:


Data_2.head()


# In[36]:


#Data Definition:
print(Data_2.iloc[:, 0:50].dtypes)


# In[41]:


#Changing floats to objects:
Data_2 = Data_2.astype({"N_concentration": 'object', "id": 'object'})
print(Data_2.iloc[:, 0:50].dtypes)


# In[42]:


print(Data_2.info())


# In[48]:


Data_2.iloc[:, 7:45].describe()


# In[55]:


Data_2['CS_number'].describe()


# In[52]:


Data_2['N_treatment'].describe()


# In[61]:


print(Data_2['Seeds_classification'].value_counts())


# In[63]:


print(Data_2['Experiment'].value_counts())


# In[69]:


#Calculating some statistics for different phenotypes by treatments:
Data_2[["N_treatment", "Leaf_Area", "Total_roots", "PR_length", "Total_GSL"]].groupby("N_treatment").mean()


# In[82]:


#Count missing values in relevant columns:
print(Data_2.iloc[:, 0:10].isnull().sum())
print("Number of samples without GSL data:", Data_2['Total_GSL'].isnull().sum())


# In[94]:


#Finding CS_numbers of missing values in latitude and longitude:
Data_2.loc[Data_2['latitude'].isnull()]


# In[ ]:


#Filling the missing values:

