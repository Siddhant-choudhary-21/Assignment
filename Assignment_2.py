#!/usr/bin/env python
# coding: utf-8

# TASK 1: BASIC FUNCTION IMPLEMENTATION Write a function greet that takes two arguments: name (a string) and greeting (a string with a default value of "Hello"). The function should return a greeting message

# In[1]:


#creating a function as greet
def greet(name,greeting = "Hello"): #variable greeting have a default value "Hello"
    print(f"{greeting} {name}") #using string formatting
    
greet("Alice")
greet("Bob","Good morning")


# 
# TASK 2: NAMED ARGUEMENT Create a function create_profile that takes arguments for name, age, and city as named arguments. The function should return a string like "Name: Alice, Age: 25, City: New York". Ensure that the age argument has a default value of 18.

# In[2]:



#creating a function name as create_profile
def create_profile(name , city, age = 18): #age variable stores a default value 18
    print(f"Name: {name}, Age: {age}, City: {city}" )
    
create_profile(name ="John", city = "Chicago")
create_profile(name="Emma", age=22, city="Los Angeles")


# 
# TASK 3: Using args and kwargs Write a function sum_numbers that takes any number of positional arguments (args) and keyword arguments *(kwargs).* It should: Return the sum of all* args if they are numbers. Return a dictionary of all keyword arguments.*

# In[3]:


#creating a function "sum_numbers"
def sum_numbers(*args, **kwargs):
    # Filter and sum positional arguments that are numbers
    totalSum = sum(arg for arg in args if isinstance(arg, (int, float)))
    
    # Return only the sum if no keyword arguments are passed
    if not kwargs:
        return totalSum
    
    # Return the sum and the dictionary of keyword arguments if any
    return totalSum, kwargs

print(sum_numbers(1, 2, 3))             
print(sum_numbers(1, 2, x=4, y=5))


# TASK 4: LAMBDAS AND MAP: Write a function that uses map and a lambda to return a list where each element is squared.

# In[4]:


def square_list(numbers):
    squares= map(lambda x: x**2, numbers) #squaring the numbers present in the list
    return list(squares) #returning the squares of the number where the function was called

square_list([1, 2, 3, 4])


# 
# TASK 5: FILTER AND LAMBDAS: Write a function that filters out all odd numbers from a list using filter and a lambda function.

# In[5]:


#creating a function that takes list as an arguement
def filter_odd_numbers(numbers):
    odd_numbers = filter(lambda x: x%2 == 0, numbers) #checking whether the number in numbers are divisible by 2
    return list(odd_numbers)

filter_odd_numbers([1,2,3,4,5])


# 
# TASK 6: BASIC LIST COMPREHENSION: Create a list comprehension that takes a list of numbers and returns a list of their squares.

# In[6]:


squares = [x**2 for x in range(5)]
print(squares)


# 
# TASK 7: LIST COMPREHENSION WITH CONDITION: Use a list comprehension to create a list of even numbers from 1 to 20.

# In[7]:


evenNumbers = [x for x in range(1,21) if x%2 == 0]
print(list(evenNumbers))


# 
# TASK 8: USING OS AND TIME MODULES: Write a function file_operations that creates a directory named "test_folder" using os.makedirs(). Then, pause the execution for 3 seconds using time.sleep(), and finally, delete the directory using os.rmdir()

# In[8]:


#importing time and os modules
import os
import time

#creating non parametrized function, file_operations
def file_operations():
    
    #creating a new directory
    os.makedirs("test_folder") #cretaed a directory named as test_folder
    
    time.sleep(3) #using sleep function from time module to stop the execution for 3 sec
    
    #removing a directory
    os.rmdir("test_folder")
    
file_operations()


# 
# TASK 9: IMPORTING SPECIFIC FUNCTIONS: Write a Python script that imports only sleep from the time module and renames it to pause. Use it to pause execution for 2 seconds and print "Paused execution..."

# In[9]:


#importing the function, sleep from time module and rename as pause
from time import sleep as pause 
pause(2) #pauses the execution for 2 sec
print("Paused execution...")


# TASK 10: RECURSIVE FUNCTION WITH *ARGS and KWARGS (Flattening a List): Write a recursive function flatten_list that can flatten a nested list of any depth using *args and **kwargs
# 
# Explanation: Flattening a list means converting a nested list into a single-level list. If the list contains sub-lists, we recursively traverse them and extract their elements to form one flat list.

# In[10]:



#creating a function that converts nested list into simple list
def flatten_list(*args, **kwargs):
    #uses *args to handle any number of arguments
    flatten = []#creating an empty list
    
    for item in args:
        if isinstance(item, list): #cheking whether each element is a list or a simple number
            flatten.extend(flatten_list(*item, *kwargs))
            
        else:
            flatten.append(item) #directly adding the element in the list if its not a list
            
    return flatten

print(flatten_list([1, [2, 3], [[4, 5], 6]]))
print(flatten_list([[1, 2], [3, [4, [5]]]]))

