#!/usr/bin/env python
# coding: utf-8

# In[9]:


1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
*,'hello', -87.8,-,/,+,6

Ans: There are a total of 4 Operators and 3 Expressions, They are:
Operators: *,-,/,+
Expressions: 'hello', 87.8, 6


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Ans: A Variable is used to store of information, and a String is a type of information you would store in a Variable. A variable is created the moment you first assign a value to it. Example: x = 10, y = "Akshay". Here x and y are variables.

A String is a group of characters or a single character usually enclosed in Double quotes " " or single quotes ' '. Even triple '''  '''. quotes can be used in Python


# In[ ]:



3. Describe three different Data Types ?
Ans: Three fundamental Data types in python are int, float, complex.

int data type: We can use int data type to represent whole numbers (integral values) Example: int_num=100
        
float data type: We can use float data type to represent floating point values (decimal values) Example: flo_num=5.55
        
complex data type: Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j. Example: com_num=10+3.8j


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Ans: An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If we ask Python to print an expression, the interpreter evaluates the expression and displays the result. An expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first.


# In[ ]:


get_ipython().set_next_input('5.This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Ans: An expression is a combination of values, variables, and operators.When we type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression.An expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first.
    
 A statement is a unit of code that has an effect, like creating a variable or displaying a value.When we type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values. A statement is an instruction that a Python interpreter can execute. There are mainly four types of statements in Python, Print statements, Assignment statements, Conditional statements and Looping statements.   


# In[ ]:


get_ipython().set_next_input('6.After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1

Ans: The variable bacon is set to 22 .The expression bacon + 1 does not reassign the value in bacon (that would the case if the expression is like bacon = bacon + 1 instead of bacon + 1)


# In[ ]:


get_ipython().set_next_input('7.What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam'+'spamspam'
'spam'*3

Ans: Both expressions evaluate to the string 'spamspamspam' Where as the first expression follows String Concatentation and the second expression follows String Multiplication


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
Ans: As per python,Variable names cannot begin with a number. The python rules for naming a variable are :-

Variable name must start with a letter or the underscore character.
Variable name cannot start with a number.
Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
Variable names are case-sensitive (name, AKSHAY and akshay are three different variables).
The reserved words(keywords) cannot be used naming the variable.


# In[ ]:


get_ipython().set_next_input('9.What three functions can be used to get the integer,floating-point number,or string version of a value');get_ipython().run_line_magic('pinfo', 'value')
Ans: The int(),float(),and str() functions will evaluate to the integer,floating-point number,string version of the value passed to them.

