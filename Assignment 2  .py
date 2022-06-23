#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.What are the two values of the boolean data types? how do you write them ?

Ans : Two values of the boolen data types are True and False. We have to use capital T and F and with the rest of the word in lowercase.
      The type bool is built in, meaning it’s always available in Python and doesn’t need to be imported. However, the name itself isn’t a keyword in the language.


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans: Boolean operators form the basis of mathematical sets and database logic. They connect our search words together to either narrow or broaden our set of results.The three differnt types of Boolean operators in python are: are, and, not Example: a ==10 and b ==50  


# In[ ]:


3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate)
Ans: The Truth tables for the boolean tables are as follows:

Truth Table for and operator
True and True --> True
True and False --> False
False and True --> False
False and False --> False
Truth Table for or operator
True or True --> True
True or False --> True
False or True --> True
False or False --> False

Truth Table for not operator
True not --> False False not --> True


# In[ ]:


4. What are the values of the following expressions ?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Ans : 
False
False
True
False
False
True


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Ans: The Six Comparision Operators available in python are:
== , != , < , > , <= , =>


# In[ ]:



get_ipython().set_next_input('6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one');get_ipython().run_line_magic('pinfo', 'one')


Ans: == is the equal to operator that compares two values and evaluates to a Boolean, while = is that assignment operator that stores a value in a variable.
    
    EX=   A= "Akshay" - this is assignee value 
    
     A == "str"- this is compersion 
        


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans: In Python, code block refers to a collection of code that is in the same block or indent. This is most commonly found in classes, functions, and loops. Answer for the question is:

ham

spam

spam


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


# In[3]:


def spamCode(spam):
    if spam==1:
        print('Hello')
    elif spam==2:
        print('Howdy')
    else:
        print('Greetings')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

Ans: To stop a program stuck in an infinite loop, we press Ctrl-c.


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

Ans: The break statement will move the execution outside the loop if break condtion is satisfied whereas the continue statement will move the execution to the start of the loop.


# In[7]:


#break

a = "akshay"

for i in a:
    if i == "s":
        break
    print(i)


# In[8]:


#continue 
a = "akshay"

for i in a:
    if i == "s":
        continue
    print(i)


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans: The Differences are as follows:

The range(10) call range from 0 to 9 (but not include 10)
The range (0,10) explicitly tells the loop to start at 0
The range(0,10,1) explicitly tells the loop to increase the variable by 1 on each iteration


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop ?


# In[19]:



for i in range(1,11):
    print(i, end= " ")


# In[ ]:





# In[17]:


i =1 
while i <=10:
    print(i, end= " ")
    i = i+1


# In[ ]:


13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam ?


Ans: This function can be called with spam.bacon()

