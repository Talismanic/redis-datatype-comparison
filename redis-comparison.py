#!/usr/bin/env python
# coding: utf-8

# In[1]:


import redis

r = redis.Redis(
    host='localhost',
    port=6379, 
    password='')


# In[2]:


import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString(10) )


# In[7]:


# building a hash object and inserting to Redis

def setHashPack():
    pack1 = randomString(25);
    pack2 = randomString(25);
    pack3 = randomString(25);
    pack4 = randomString(25);
    pack5 = randomString(25);
    pack6 = randomString(25);
    pack7 = randomString(25);
    pack8 = randomString(25);
    pack9 = randomString(25);
    user = randomString(11);
    packDict = {"p1": pack1, "p2":pack2, "p3":pack3,"p4":pack4,"p5":pack5,"p6":pack6,"p7":pack7,"p8":pack8,"p9":pack9}
    r.hmset(user, packDict)
    return 1;


# In[8]:


#setting data as hash
import datetime as dt

strt = dt.datetime.now()

for i in  range(100):
    setHashPack()

endt = dt.datetime.now()

time_taken = endt - strt

print ("start time:", strt)
print ("end time:", endt)


# In[9]:


strt = dt.datetime.now()
keyname = 'fzvrqivsedg'
r.hgetall(keyname);
endt = dt.datetime.now()
differ = (endt - strt).microseconds


print ("start time:", strt)
print ("end time:", endt)


# In[3]:


def setZsetPack():
    pack1 = randomString(25)
    pack2 = randomString(25)
    pack3 = randomString(25)
    pack4 = randomString(25)
    pack5 = randomString(25)
    pack6 = randomString(25)
    pack7 = randomString(25)
    pack8 = randomString(25)
    pack9 = randomString(25)
    user = randomString(11)
    packDict = {pack1:1, pack2:2, pack3:3, pack4:4, pack5:5, pack6:6, pack7:7, pack8:8, pack9:9}
    r.zadd(user, packDict)
    
    return 1


# In[4]:


#setting data as zset
import datetime as dt

strt = dt.datetime.now()

for i in  range(100000):
    setZsetPack()

endt = dt.datetime.now()

time_taken = endt - strt


print ("start time:", strt)
print ("end time:", endt)


# In[12]:


strt = dt.datetime.now()
keyname = 'vjtyfircnxu'
r.zrange(keyname, 0, -1, withscores=True)
endt = dt.datetime.now()
differ = (endt - strt).microseconds


print ("start time:", strt)
print ("end time:", endt)


# In[13]:


# building a string object and inserting to Redis

def setStringPack():
    pack1 = randomString(25);
    pack2 = randomString(25);
    pack3 = randomString(25);
    pack4 = randomString(25);
    pack5 = randomString(25);
    pack6 = randomString(25);
    pack7 = randomString(25);
    pack8 = randomString(25);
    pack9 = randomString(25);
    user = randomString(11);
    pack = {"p1": pack1, "p2":pack2, "p3":pack3,"p4":pack4,"p5":pack5,"p6":pack6,"p7":pack7,"p8":pack8,"p9":pack9}
    packs = str(pack)
    r.set(user, packs)
    return 1;


# In[14]:


#setting data as string
import datetime as dt

strt = dt.datetime.now()

for i in  range(100):
    setStringPack()

endt = dt.datetime.now()

time_taken = endt - strt

print ("start time:", strt)
print ("end time:", endt)


# In[15]:


strt = dt.datetime.now()
keyname = 'iiwohzwfcqa'
print(r.get(keyname))
endt = dt.datetime.now()
differ = (endt - strt).microseconds


print ("start time:", strt)
print ("end time:", endt)


# In[18]:


# Storing MSISDN in SET

import datetime as dt

strt = dt.datetime.now()

for i in  range(1000000):
    msisdn = randomString(13)
    r.sadd ('cards_110', msisdn)

endt = dt.datetime.now()

time_taken = endt - strt


print ("start time:", strt)
print ("end time:", endt)


# In[ ]:




