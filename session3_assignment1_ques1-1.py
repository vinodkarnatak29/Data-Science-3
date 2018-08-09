
# coding: utf-8

# ##### Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[11]:


from functools import reduce

#multiply all numbers in a list
# @listSet variable hold the list value

listSet = [2,4,5,6,8,12,13,15]
multiplyResult = reduce(lambda x,y: x*y, listSet)
print("Built in reduce method output:",multiplyResult)


# now myReduce()

def myReduce(listSet):
    result = 1
    for x in listSet:
        result *= x
    return result

print("myReduce method output:",myReduce(listSet))

