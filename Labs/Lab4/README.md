# Lab 4 Reference
Author: Sam Weissmann

Reference sheet for basic information about modules, functions, and imports.

TABLE OF CONTENTS  
[1. Functions](#1-functions)  
[1.1. Why Functions?](#11-why-functions)  
[1.2. Defining Functions](#12-defining-functions)  
[1.3. Parameters and Arguments](#13-parameters-and-arguments)  
[1.3.1. Default Arguments](#131-default-arguments)  
[1.4. Return Statements](#14-return-statements)  
[1.4.1 Print Vs. Return](#141-print-vs-return)  

[2. Modules](#2-modules)  
[2.1. Importing](#21-importing)  



## 1. Functions
In Python, functions allow you to run a predefined block of code simply by calling the function wherever you need that code to execute in your program. A function is able to recieve data to use and return some data back to the place where it was originally called. Python has many built-in functions, some of which you should already by familiar with such as `range` and `sum`. Python also allows users to write their own functions, which is what we'll be doing today. 

### 1.1. Why Functions?
Functions have many upsides, in particular: 
* Reusable 
* Improves division of labor 
* Abstraction:
  * Improves readability 
  * Frees up cognitive bandwidth 

### 1.2. Defining Functions
In Python, functions are defined using the `def` keyword. A function definition is comprised of a header and a body. The __function header__ includes the name of the function and a list of the parameters the function can take, if any. The function body contains code that will be executed and optionally a __return statement__. If no return statement is provided, the function will return `None` by default. 

```python
def my_function(par1, par2): #this line is the function header
    #body of code to execute here
    return None
```
### 1.3. Parameters and Arguments
As mentioned above, a function is able to take in data. A datum that a function takes in is called a __parameter__, while the actual value of that datum is called an __argument__. A function may take one, many, or no parameters at all.


In the code below, the parameters for `my_function()` are `par1` and `par2`. The arguments being passed in are the integers 10 and 20. `par1` and `par` will be available as variables with the values 10 and 20 respectively __within the function's body only__. 

```python
#function definition
def my_function(par1, par2): #header
    #Do something with par1 and par2 here
    return None #return statement

my_function(10, 20) #function_call
```

In short: __parameters__ are what is defined in the header of the function definition. __Arguments__ are the value of the data that gets passed into the function at runtime. 

Colloquially, parameter and argument are often used interchangeably, but it's still important to understand the difference. 

#### 1.3.1. Default Arguments
Arguments can be assigned default values in the function header. If a parameter has a default value and no argument is passed in for that parameter, it will use its default value instead. Default values are optional, and not every parameter needs or should have one.

In the code below, `par2` is given the default value of 25. In the function call, the argument 10 is passed in as the first parameter. Because no second argument is provided, the second parameter will default to a value of 25.

```python
#function definition
def my_function(par1, par2=25): #header
    #do something with par1 and par2
    return None #return statement

my_function(10) #function call
#10 is assigned to the first parameter. The second parameter defaults to 25
```

### 1.4. Return Statements 
Functions are able to return data back to the point in the program from where it was called. This is done using a __return statement__. Return statements use the `return` keyword followed by the data that will be returned. Not all functions need to return data, and in fact you can omit the return value or statement from the function body entirely. If you do, Python will have the function automatically return `None` by default. 

All three functions below will return `None`
```python
def my_function(para1,para2):
    #function body
    return None

def my_function2(para1, para2):
    #function body
    return

def my_function(para1, para2):
    #function body

#### 1.4.1. Print vs. Return
A common point of confusion for new programmers is the difference between the `print()` function and a return statement. Print will print out some specified data to the user. A return statement will return some data to the point in the code where the function was originally called. A return statement will not be visible to the user unless its data is additionally printed. 

## 2. Modules 
Imagine you've written a useful function and you want to reuse it between different projects. How could you best accomplish this? Go into an old project and copy and paste the code into your new project every time you want it? Keep a seperate list of all your useful function definitions that you can copy from? Neither of these are ideal solutions.

Fortunately, Python already has an easy way for us to do this using __modules__. A __module__ is a .py file that contains function definitions and statements. We can bring a module into our program using the `import` keyword, which allows us to access all of the functions it contains. You've already encountered this in Homework 2 with the `random` module. Python has an expansive standard library of modules (including `random`) that can be imported into your programs. In addition to this, we can also write and import our own modules, which is what we will do in this lab.

More information on modules can be found here: https://docs.python.org/3/tutorial/modules.html

### 2.1. Importing 
A module can be imported to a program using the `import` keyword. For modules that we write ourselves, as long as the module's .py file is in the same directory as the program importing it, it will import without any problems. See the code examples below for different ways of importing modules and functions. 

Import math and make all of its functions available:
```python
import math

math.sqrt(16) #returns 4
```

Renaming an imported module:
```python
import math as m #can access math as "m"

m.sqrt(16)
```

Importing only a specific function from a module:
```python
from math import sqrt 

sqrt(16) #no longer need to reference math module to call sqrt() function.
```

Calculating the square root of a random integer between 1 and 1,000:
```python
import random as r
from math import sqrt

rand_num = r.randint(1,1000)
rand_root = sqrt(rand_num)
```
