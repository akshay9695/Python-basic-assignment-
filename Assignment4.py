{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddf7e908",
   "metadata": {},
   "outputs": [],
   "source": [
    "1.What exactly is [ ]?\n",
    "\n",
    "Ans : The empty list represented by [] is a list that contains no items. This is similar to '' which represents an empty string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18721edc",
   "metadata": {},
   "outputs": [],
   "source": [
    "2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)\n",
    "\n",
    "Ans : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "84ef7ac8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 'hello', 8]\n"
     ]
    }
   ],
   "source": [
    "spam = [2,4,6,8]\n",
    "spam[2]= \"hello\"\n",
    "print(spam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "23da12b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "Let's pretend the spam includes the list ['a','b','c',d'] for the next three queries.\n",
    "3. What is the value of spam[int(int('3'*2)//11)] ?\n",
    "\n",
    "Ans : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "32be8549",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam = ['a','b','c','d']\n",
    "spam[int(int('3'*2)//11)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "667c0762",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2354258632.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [12]\u001b[1;36m\u001b[0m\n\u001b[1;33m    4. What is the value of spam[-1]?\u001b[0m\n\u001b[1;37m       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "4. What is the value of spam[-1]?\n",
    "\n",
    "Ans : ['d']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e774118e",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. What is the value of spam[:2]?\n",
    "\n",
    "Ans : ['a', 'b']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7b6975a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Let's pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three question\n",
    "6. What is the value of bacon.index('cat')?\n",
    "\n",
    "Ans :  The value of bacon.index('cat') is 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "30960c4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "bacon = [3.14,'cat',11,'cat',True] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5d4d9e5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon.index('cat')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d9fadd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "7. How does bacon.append(99) change the look of the list value in bacon?\n",
    "\n",
    "Ans : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4108edf4",
   "metadata": {},
   "outputs": [],
   "source": [
    "bacon.append(99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8eb10347",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 'cat', 11, 'cat', True, 99]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f21dcea0",
   "metadata": {},
   "outputs": [],
   "source": [
    "8. How does bacon.remove('cat') change the look of the list in bacon?\n",
    "\n",
    "Ans : "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3da9c12d",
   "metadata": {},
   "outputs": [],
   "source": [
    "bacon.remove(\"cat\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7e9baa0f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 11, 'cat', True]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2c97684",
   "metadata": {},
   "outputs": [],
   "source": [
    "9.what are the list concatenation and list replication operations?\n",
    "\n",
    "Ans : \n",
    "    The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "5e527e54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aa', 'bb', 'cc', 'xx', 'yy', 'zz']"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 = [ 'aa','bb','cc']\n",
    "list2 = ['xx','yy', 'zz']\n",
    "\n",
    "list1 + list2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "57c46db5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['xx', 'yy', 'zz', 'xx', 'yy', 'zz']"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list2*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9adbf6c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "10.what is the difference between the list method append() and insert()?\n",
    "\n",
    "Ans : While append() will add values only to the end of a list, insert() can add them anywhere in the list.\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "40f3e11e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['aa', 'bb', 'cc', 99]\n",
      "['aa', 'bb', 'cc', 99, 99]\n"
     ]
    }
   ],
   "source": [
    "print(list1)\n",
    "list1.append(99)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "de27a868",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['aa', 'bb', 'patel', 99, 99]\n",
      "['aa', 'bb', 'my', 'patel', 99, 99]\n"
     ]
    }
   ],
   "source": [
    "print(list1)\n",
    "list1.insert(2, \"my\")\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67b2295a",
   "metadata": {},
   "outputs": [],
   "source": [
    "11. What are the two methods for removing items from a list?\n",
    "\n",
    "Ans : \n",
    "    The del statement and the remove() method are two ways to remove values from a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "ba0e2cdd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aa', 'bb', 'my', 99, 99]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del list1[3]\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ba59c968",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1.remove(99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "9a2685fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aa', 'bb', 'my', 99]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63bc3041",
   "metadata": {},
   "outputs": [],
   "source": [
    "12. Describe how list values and string values are identical.\n",
    "\n",
    "\n",
    "Ans : \n",
    "    The similarity between Lists and Strings in Python is that both are sequences. The differences between them are that firstly, Lists are mutable but Strings are immutable. Secondly, elements of a list can be of different types whereas a String only contains characters that are all of String type.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2d3931a",
   "metadata": {},
   "outputs": [],
   "source": [
    "13. What's the difference between tuples and lists?\n",
    "\n",
    "Ans: Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed. Tuples are Immutable but Indexable and Slicable. the tuple values cannot be changed at all. Also, tuples are represented using parentheses, (), while lists use the square brackets, [].\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3244d7d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "14. How do you type a tuple value that only contains the integer 42?\n",
    "\n",
    "Ans:(42,) (The trailing comma is mandatory. otherwise its considered as a int by python Interpreter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2f04eea",
   "metadata": {},
   "outputs": [],
   "source": [
    "15. How do you get a list value's tuple form? How do you get a tuple value's list form?\n",
    "Ans: The tuple() and list[] functions, respectively are used to convert a list to tuple and vice versa\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ba95a232",
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8b8bde32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5)\n"
     ]
    }
   ],
   "source": [
    "A = tuple(l)\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "b43287a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list[1, 2, 3, 4, 5]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list[A]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f587e17",
   "metadata": {},
   "outputs": [],
   "source": [
    "16. Variables that \"contain\" list values are not necessarily lists themselves. Instead, what do they contain?\n",
    "\n",
    "\n",
    "Ans: They contain references to list values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b74a2687",
   "metadata": {},
   "outputs": [],
   "source": [
    "17. How do you distinguish between copy.copy() and copy.deepcopy()?\n",
    "\n",
    "Ans : \n",
    "    The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "44901aa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3,4,[3,5,8],5,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "e3bd3d12",
   "metadata": {},
   "outputs": [],
   "source": [
    "import copy\n",
    "l1 = copy.copy(l)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "44c6d5e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, [3, 5, 8], 5, 6]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "9fd2e990",
   "metadata": {},
   "outputs": [],
   "source": [
    "import copy \n",
    "l2 = copy.deepcopy(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "2afd9366",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, [3, 5, 8], 5, 6]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d1ec445",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
