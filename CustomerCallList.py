#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning in Pandas

# In[1]:


import pandas as pd


# In[3]:


df= pd.read_excel(r"/Users/mehtapbuyukguzel/Desktop/Customer Call List.xlsx")
df


# * We got handed this list of names and we need to clean it up and hand it off to people who are actually going to make these calls to this customer list.

# ## Removind Duplicates

# * df.drop_duplicates() : Yinelenenleri kaldırmak için kullanıyoruz. 

# In[4]:


df.drop_duplicates()


# After that, now just have one row of Anakin Skywalker and of course we want to save that so we're just going to say DF is equal to and DF so now it's going to save that to the data frame variable again and now when we run this our data frame Now does not have any duplicates. 
# 
# So write this: 
# 
# df= df.drop_dublicates()
# 
# df
# 
# RUN
# 

# In[5]:


df= df.drop_duplicates()
df


# ## Dropping Columns
# 

# * Remove any column we dont need

# Now we can delete this column 'Not_Useful_Column' ,
# 
# #### this code : df = df.drop(columns = 'Not_Useful_Column')
#               
# #### df
# 
# #### RUN

# In[6]:


df= df.drop(columns= 'Not_Useful_Column')
df


# ## Strip 

# * Now let's kind of go column by column and see what we need to fix. CustomerID is look good so we dont change it. 
# 
# * Specify the column that we're working with because we don't want to make these changes or strip all of these 

# In[12]:


df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.rstrip("/")
df


# #### Note!!!!! or we can use just this code:
# 
# df["last_name"]= str.strip("123._/")
# 
# df

# In[13]:


df


# ### Now we clean phone number section!!!

# In[14]:


#df["Phone_Number"]= df["Phone_Number"].str.replace('[^ a-zA-Z0-9]','')

df["Phone_Number"].apply


# ### Aşağıdaki şekilde kod yazarak, telefon numaraları arasına - işaretleri koyduk.

# In[17]:


#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# In[21]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' +x[6:10])

df


# In[25]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[26]:


df


# In[37]:


df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',2,expand=True)
df


# In[40]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')

df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')

df


# In[45]:


#df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
#df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')

df.fillna('')


# In[47]:


#df = df.replace('N/a','')
#df = df.replace('NaN','')

df.fillna('')


# #### Olmayan değerleri sadece bu kodu kullanarak heryerden silebiliriz. 
# 
# df.fillna('')

# In[48]:


##### DoNotContact kısmına Yes diyeleri siliyoruz:


# In[49]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace= True)
        
df


# In[50]:


##### Numarası olmayan kişileri silmek için; 
for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace= True)
        
df


# In[51]:


##index kısmındaki rakamları düzenliyoruz:

df.reset_index(drop=True)


# In[ ]:


#Another way to drop null values
#df.dropna(subset="Phone_Number"),inplace=True)

