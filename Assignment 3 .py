#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')
Ans: Below are the advantages of functions in programming:

Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update. The main advantage of functions is code Reusability.
Increases program readability.
Divide a complex problem into simpler ones.
Reduces chances of error.
Modifying a program becomes easier by using function


# In[ ]:


get_ipython().set_next_input("2. When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')
Ans: The code in a function executes when the function is called, not when the function is specified. When a function is "called" the program "leaves" the current section of code and begins to execute the first line inside the function. Example is mentioned below:


# In[4]:


def test1 (name):
    return (name + " patel")


# In[5]:


test1("Akshay")


# In[ ]:


get_ipython().set_next_input('3. What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')

Ans: The def statement defines a function


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')
Ans: A function is a block of code that does a particular operation and returns a result. It usually accepts inputs as parameters and returns a result. The parameters are not mandatory. A function call is the code used to pass control to a function.


# In[6]:


# funtion 
def addition (a):
    return (a + 5)


# In[7]:


#fuction call 
addition (15)


# In[ ]:


get_ipython().set_next_input('5. How many global scopes are there in a Python program? How many local scopes');get_ipython().run_line_magic('pinfo', 'scopes')


# In[ ]:


Ans : When you use an unqualified name inside a function, Python searches three scopes—the local (L), then the global (G), and then the built-in (B)—and stops at the first place the name is found
    
    There is one global scope, and a local scope is created whenever a function is called. A variable created inside a function belongs to the local scope of that function, and can only be used inside that function whereas A variable created in the main body of the Python code is a global variable and belongs to the global scope.


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')

Ans: When a function returns, the local scope is destroyed, and all the variables in it are forgotten. A local variable becomes undefined after the function call completes


# In[ ]:


get_ipython().set_next_input('7. What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')

Ans: The Python return statement is a key component of functions and methods. We can use the return statement to make functions send Python objects back to the caller code. These objects are known as the function’s return value. A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')

Ans: If there is no return statement for a function, its return value is None. The function always returns None if explicit return is not written.


# In[ ]:


get_ipython().set_next_input('9. How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans: A global statement will force a variable in a function to refer to the global variable. If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.


# In[ ]:


get_ipython().set_next_input('10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')

Ans: The data type of None is NoneType.


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')

Ans: That import statement imports a module named areallyourpetsnamederic.


# In[ ]:


get_ipython().set_next_input('12. If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')

Ans: This function can be called with spam.bacon().


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')

Ans: We can place the line of code that might cause an error in a try clause and use except block to handle the error


# In[ ]:


get_ipython().set_next_input('14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')

ANS:The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.

