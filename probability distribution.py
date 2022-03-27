#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3.Normal Distribution
from statistics import NormalDist
value1 = int(input("Enter mu value : "))
value2 = int(input("Enter sigma value : "))
nd = NormalDist(mu = (value1), sigma = (value2))
value3 = int(input("Enter x value : "))    # z = (x-mu)/sigma
value4 = int(input("Enter x value2 : "))
if(value3==-1 or value4==-1):
    if value3:
        print(0-nd.pdf(value4))
    else:
        print(0-nd.pdf(value3))
else:
    print(nd.pdf(value4)-nd.pdf(value3))

