#!/usr/bin/env python
# coding: utf-8

# In[1]:


var1=set("This is an example")
print(var1)


# In[22]:


languages=['sql','plsql','python','java','sql']
language_set=set(languages)
language_set


# In[23]:


language_set.add('c')
language_set
#language_set.append('c++') => AttributeError: 'set' object has no attribute 'append'


# In[24]:


fix_language=frozenset(language_set)
print(fix_language)
#fix_language.add('.Net') => AttributeError: 'frozenset' object has no attribute 'add'
language_set.clear()
print(language_set)
language_set=set(fix_language)
print(language_set)
language_set.add('c++')
print(language_set)
print(fix_language)


# In[28]:


cities = {'bangalore','chennai','pune','delhi','kolkata'}


# In[27]:


# Assignments creates a Pointer
cities_backup=cities
print(cities_backup)
cities.clear()
print(cities_backup)


# In[29]:


# shallow copy
cities_backup=cities.copy()
print(cities_backup)
cities.clear()
print(cities_backup)


# In[42]:


set1={1,2,3,4,5}
set2={4,5,6,7,8,9}


# In[43]:


print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)
print(set1.isdisjoint(set2))
set2.discard(9)
set1.remove(1)
print(set1)
print(set2)


# In[18]:


#Reading a file and counting the Unique words in it

import re
reseq_doc = open("C:/Users/AS2814/Desktop/ZBR_SOA_INFRA_TABLE_LOAD_PKG_BKP.sql").read().lower()
words = re.findall(r"\b[\w-]+\b", reseq_doc)
print("The Document contains " + str(len(words))+' words.')
unique_words=set(words)
print('Unique word count is '+str(len(unique_words)))
print(unique_words)

