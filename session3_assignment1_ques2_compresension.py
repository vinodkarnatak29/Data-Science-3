
# coding: utf-8

# In[ ]:


# List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


# In[12]:


givenString = "ACADGILD"
listResult = [item for item in givenString]

print("ACADGILD : ",listResult)


# In[5]:


givenList = ['x','y','z']
listResult = [item*num for item in givenList for num in range(1,5)]
print("['x','y','z'] : ",   str(listResult))


# In[7]:


givenList = ['x','y','z']
listResult = [item*num for num in range(1,5) for item in givenList]
print("['x','y','z'] : " ,   listResult)


# In[8]:


givenList = [2,3,4]
listResult = [[item+num] for item in givenList for num in range(0,3)]
print("[2,3,4] : " ,  listResult)


# In[9]:


givenList = [2,3,4,5]
listResult = [[item+num for item in givenList] for num in range(0,4)]
print("[2,3,4,5] : ", listResult)


# In[11]:


givenList=[1,2,3]
listResult = [(b,a) for a in givenList for b in givenList]
print("[1,2,3] : ", listResult)

