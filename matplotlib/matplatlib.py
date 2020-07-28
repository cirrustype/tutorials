#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# ## Libraries

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# ### Basic Graph

# In[38]:


x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]

#resize graph
plt.figure(figsize=(5,3), dpi=100) #dpi is pix per inch

plt.plot(x,y, label = '2x',color = 'purple', linewidth = .8,
         marker = '.', markersize = 2, linestyle = '--') 
### if using variables, use (), #for legend

#or quickhand...look up doc for comands
#plt.plot(x,y, 'r.-', label = '2x') 

#line 2
x2 = np.arange(0,4.5,.5) #a-range

#prints first part of curve solid and projects dashes for the rest
plt.plot(x2[:5], x2[:5]**2, label = "x^2")
plt.plot(x2[4:], x2[4:]**2, 'b--')

#adding title and plot perameters
plt.title('Graph', fontdict = {'fontname': 'Georgia'}) #title
plt.xlabel('X', labelpad = 15, fontdict = {'fontname': 'Georgia'})
plt.ylabel('Y', rotation = 0, labelpad = 15, 
           fontdict = {'fontname': 'Georgia'}) 
## rotation to orientate the axis text and labelpad to push the text away

#tickmarks
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,7,7.5,8,10])

#adding legend
plt.legend()
plt.show() # only displays graph

#saving graph
plt.savefig('mygraph.png', dpi = 300)




###### Bar charts ######

lebels = ['A', 'B', 'C']
values = [1,4,2]

bars = plt.bar(lebels, values) #need to name for diff patterns
#to set patterns manually 
#bars[0].set_hatch('/')
#bars[1].set_hatch('-')
#bars[2].set_hatch('*')

#or...

patterns = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
    
    


plt.figure(figsize = (6,4))













# In[ ]:




