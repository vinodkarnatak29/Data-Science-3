
# coding: utf-8

# ##### Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[4]:


# get the data from the list which is greater than 10.
# @listSet variable hold the list value

listSet = [2,44,5,56,8,12,13,15]
result = list(filter(lambda x: x > 10, listSet))

print("Built in filter method output:",result)

# now myReduce()

def myFilter(listSet):
    result = []
    for x in listSet:
        if(x > 10):
            result.append(x)
    return result

print("myFilter method output:",myFilter(listSet))

