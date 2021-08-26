#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd

from matplotlib import pyplot as plt


# In[10]:


so_tags = pd.read_csv("stackoverflowtags.csv")

so_tags = so_tags.sort_values("n_questions", ascending = False)

so_tags


# In[19]:


plt.barh(so_tags["tag"], so_tags["n_questions"])

plt.gca().invert_yaxis()

plt.savefig('so_tags.jpg',bbox_inches="tight", pad_inches = 1)


# In[7]:


vals = pd.read_csv("mentimeter_vote_I.csv",delimiter=";")["value"]

vals1 = [str(x)[0]+"."+str(x)[1] for x in vals]
binwidth = 2


def mybins(vals, binwidth):
    range(min(vals), max(vals) + binwidth, binwidth)

plt.hist(vals, bins = mybins(vals,2))

plt.axvline(x=38,color = "black")

plt.savefig('stand_CodinginGIS1.jpg',bbox_inches="tight")


# In[9]:


vals = pd.read_csv("mentimeter_vote_II.csv",delimiter=";")["value"]

vals1 = [str(x)[0]+"."+str(x)[1] for x in vals]
binwidth = 2


def mybins(vals, binwidth):
    range(min(vals), max(vals) + binwidth, binwidth)

plt.hist(vals, bins = mybins(vals,2))

plt.axvline(x=86,color = "black")

plt.savefig('stand_CodinginGIS2.jpg',bbox_inches="tight")


# In[14]:


from matplotlib import pyplot as plt 
import pandas as pd
import random

def offset_coordinate(old, distance = 100):
    new = old + random.normalvariate(0,distance)

    return(new)


x = 2600000
y = 1200000

n_points = 100000

fig = pd.DataFrame({"x":[offset_coordinate(x, 200) for rand in range(1,n_points)], "y": [offset_coordinate(y, 200) for rand in range(1,n_points)]}).plot.scatter("x","y", color = "red", alpha = 0.2)

plt.scatter(x,y, c = "red")
fig.set_aspect("equal", "box")
plt.show()   


  


# In[ ]:


from matplotlib import pyplot


# In[ ]:




