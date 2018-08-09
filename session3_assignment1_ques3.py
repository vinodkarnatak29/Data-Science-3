
# coding: utf-8

# #### Function longestWord() that takes a list of words and returns the longest one.

# In[7]:


## if a list contain only one longest word, then it will return the longest one else it will return the first longest word.
def longestWord(givenList):
    maxLength = 0
    longestWord = ''
    for item in givenList:
        if(len(item) > maxLength):
            maxLength = len(item)
            longestWord = item
    return longestWord

# list contain only one longest word
listOne = ["a","bb","ccc","weweewwe", "asas",]
print("Return Longest : ", longestWord(listOne))

listTwo = ["as","basss","qwe","qwerty","asdfgh"]
print("Return First Longest : ", longestWord(listTwo))


# In[10]:


# program to return the list of longest words

def longestWordList(givenList):
    maxLength = 0
    longestWordList = []
    for item in givenList:
        if(len(item) > maxLength):
            maxLength = len(item)
    for item in givenList:
        if(len(item) == maxLength):
            longestWordList.append(item)
    return longestWordList

# list contain only one longest word
listOne = ["a","bb","ccc","weweewwe", "asas",]
print("Return Longest word in list: ", longestWordList(listOne))

# list contain more than one longest word
listTwo = ["as","basss","qwe","qwerty","asdfgh"]
print("Return Longest words in list : ", longestWordList(listTwo))

