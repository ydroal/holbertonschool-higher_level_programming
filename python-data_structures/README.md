# Python - Data Structures: Lists, Tuples

This is the project with Python.  
learn about Python programming.


## General

* __What are lists and how to use them__  
Lists are used to store multiple items in a single variable.  
It's written with square brackets [] and items are separated by commas.
  

* __What are the differences and similarities between strings and lists__  
Similarities:

	* Both are ordered collections of items
	* Both can be iterated over
	* Both can be indexed and sliced
Differences:

	* Strings are used to store sequences of characters (e.g. words, sentences, etc.).  
	  Lists are used to store sequences of any type of data (e.g. numbers, strings, other lists, etc.).
	* Strings are immutable, meaning their contents cannot be changed after they are created.   
	  Lists are mutable, meaning their contents can be modified.
	* Strings can be concatenated using the + operator, but lists can be concatenated using  
	  the + operator or the extend() method.
	* Strings have many built-in methods for manipulation (e.g. upper(), lower(), replace(), etc.), whereas lists have more general methods for manipulation (e.g. append(), remove(), etc.)

  
* __What are the most common methods of lists and how to use them__
	* append(item): adds an item to the end of the list
	* insert(index, item): inserts an item at a specific position in the list
	* extend(iterable): adds all items from an iterable (such as another list) to the end of the list
	* remove(item): removes the first occurrence of an item from the list
	* pop(index): removes and returns the item at a specific position in the list (defaults to the last item if not specified)
	* clear(): removes all items from the list
	* index(item): returns the index of the first occurrence of an item in the list
	* count(item): returns the number of occurrences of an item in the list
	* sort(): sorts the items of the list in ascending order
	* reverse(): reverses the order of the items in the list
	* copy(): creates a shallow copy of the list


* __How to use lists as stacks and queues__  
as stack: append() and pop()  
as queues:  collections.deque (queue.append() and queue.popleft())  


* __When to use tuples versus lists__
tuples are immutable, meaning their contents cannot be modified after they are created.  
This makes them useful for storing data that should not be changed, such as a collection of constant values.  
A list is mutable, meaning its contents can be modified after it is created.  
This makes it useful for storing data that may change, such as a collection of user inputs.

* __What is a sequence__  
A sequence is a data structure that stores a collection of items in a specific order.  
The items in a sequence can be of any type, such as numbers, strings, or other objects.  
There are several types of sequences in Python,  
    * Lists: a mutable sequence that can store items of any type. 
    * Tuples: an immutable sequence that can store items of any type. 
              items cannot be added, removed, or modified.  
    * Strings: an immutable sequence of characters. 
    	       individual characters cannot be modified.  
    * Bytearrays: a mutable sequence of integers (representing bytes)  
		  All of these types of sequences share some common behaviors and methods, such as indexing, slicing and iteration.  


* __What is tuple packing__  
A feature to create a tuple without using parentheses.  
It is a shorthand way of creating a tuple by simply listing its elements separated by commas.  
```example;
t = 1, 2, 3
print(t)  # Output: (1, 2, 3)

It is equivalent to:
t = (1, 2, 3)

```
★ tuple packing only works when the elements are separated by commas.


* __What is sequence unpacking__  
Way to assign the elements of a sequence (such as a tuple or list) to multiple variables in a single assignment statement.  
It is the inverse of tuple packing, where we create a tuple by listing its elements separated by commas.


## Tasks

## Repo
* GitHub repository: holbertonschool-higher_level_programming 
* Directory: python-data_structures

