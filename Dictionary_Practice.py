#!/usr/bin/env python
# coding: utf-8

# In[33]:


en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print('*********************************\nColour names in German and French \n*********************************')
#print(en_de.popitem())
for i in en_de:
    print('{} is known as {} in german and {} in french.'.format(i,en_de[i],de_fr[en_de[i]]))
    
print(en_de.get('black','Black not found.'))


# In[34]:


trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }


# In[48]:


trainings['course1']['title']
for seq,i in enumerate(trainings,1):
    print('Course {}:'.format(seq),trainings[i]['title'],'at',trainings[i]['location'],'by',trainings[i]['trainer'])


# In[49]:


dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]


# In[63]:


country_dish=dict(list(zip(countries,dishes)))
print(country_dish)
country_dish_list=list(country_dish.items())
cntry=[]
dish=[]
for i in country_dish_list:
    cntry.append(i[0])
    dish.append(i[1])
print(cntry,dish)

