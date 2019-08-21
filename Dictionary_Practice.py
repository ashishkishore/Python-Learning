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


# In[3]:


dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]


# In[4]:


country_dish=dict(list(zip(countries,dishes)))
print(country_dish)
country_dish_list=list(country_dish.items())
cntry=[]
dish=[]
for i in country_dish_list:
    cntry.append(i[0])
    dish.append(i[1])
print(cntry,dish)


# In[5]:


print(country_dish_list)


# In[23]:


class Tab:

    menu={
        'red_wine':500,
        'signature_whisky':825,
        'bp_whisky':930,
        'old_monk_rum':450,
        'smirnoff_vodka':1025,
        'beer': 200,
        'chicken':400,
        'fish':625,
        'pron':550,
        'paneer':350,
        'salad':75,
        'peenut_masala':100,
        'king':150,
        'palak paneer':220
    }

    def __init__(self):
        self.total=0
        self.item=[ ]

    def add(self,item):
        self.item.append(item)
        self.total += self.menu[item]

    def print_bill(self,tax,service):
        tax_total=(tax/100)*self.total
        service_total= (service/100)*self.total
        total = self.total + tax_total + service_total
        for item in self.item:
            print(f'{item:20} Rs.{self.menu[item]}')
        print(f'{"Tax":20} Rs.{tax_total+service_total}')
        print(f'{"Total":20} Rs.{total}')


# In[25]:


table1=Tab()
print(list(table1.menu.keys()))
table1.add('fish')
table1.add('chicken')
table1.add('palak paneer')
table1.add('beer')
table1.print_bill(5,0)

