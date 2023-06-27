#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


wb='https://www.foxnews.com/entertainment'
url=requests.get(wb).text  
#requests.get()-> used to send an HTTP GET request to the specified website URL.


# In[11]:


soup=BeautifulSoup(url,'html.parser')


# In[20]:


for heading in soup.find("h2"):
        print(heading.text)


# In[32]:


#Finding h2 and h4 headings now
for heading in soup.find_all(["h2", "h4"]):
    print(heading.text)


# Creating the function

# In[33]:


def page(s):
    
    # Iterate over the tags and headlines together
    for heading in soup.find_all(["h1", "h2", "h4"]):
        print(heading.name + ' : ' + heading.text.strip())        


# In[34]:


page(soup)

