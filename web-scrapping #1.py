#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
    from bs4 import BeautifulSoup


# In[6]:


wb='https://www.foxnews.com/entertainment'
url=requests.get(wb).text  
#requests.get()-> used to send an HTTP GET request to the specified website URL.


# In[7]:


soup=BeautifulSoup(url,'html.parser')


# In[8]:


def page(s):
    
    # Iterate over the tags and headlines together
    for heading in soup.find_all(["h1", "h2", "h4"]):
        print(heading.name + ' : ' + heading.text.strip())


# In[9]:


page(soup)

