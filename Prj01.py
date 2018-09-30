
# coding: utf-8

# In[1]:


#Project 1.1
import math as mt
#Find out the primes
def is_prime(n):
    for i in range(2, int(mt.sqrt(n))):
        if n % i == 0:
            return False
    return True
#Count the number for twin primes
#For even can not be prime
count = 0
for n in range(999,1000001,2):
    if is_prime(n) is True and is_prime(n + 2) is True:
        count += 1
print('The total number of twin primes between 1000 and 1000000 is %d' %count)


# In[2]:


#Project 1.2


# In[3]:


#To find the largest twin prime under 1 million,just reverse.


# In[4]:


list = []
for n in range(1000001,999,-2):
    if is_prime(n) is True and is_prime(n + 2) is True:
        list.append(n)
        break
print('The largest twin primes between 1000 and 1000000 is',list)

