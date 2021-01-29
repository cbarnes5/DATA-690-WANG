# Notes for Lesson 1
**Author**: Crista Barnes

**Date**: 1/28/2021

**Focus on code writing preperation and environment/file type familiarity** 

[Text Book](https://github.com/chenomg/CS_BOOKS/blob/master/Python%20for%20Data%20Analysis%2C%202nd%20Edition.pdf)

## Important terms
ipynb
: interactive python notebook 

pwd
 : present working directory
 
ls
 : list files

## Code writing ediquitte
- Every Github repository should have a README.md
- Include a title, author, and date in markdown file

## How to's
### Github
To add a new folder to Github use a forward slash when adding a new file 

### Deepnote
 - To add an interactive python notebook to Github, download the notebook to your local machine, then upload on Github profile 
 - Notebooks can run from the same page on which they are edited, while .py files must run from the terminal (a feature in deepnote) 
 
 ## Code Writing Basics 
 
# Notes from Text Book Chapters 1 & 2

## Essential Python Libraries

**NumPy**
 - Cornerstone of Numerical comupting in Python
 - Provides the data structures, algorithms, and library glue for most scientific applications involving numerical data in Python
 - NumPy arrays are more effeciant than Python data structures for storing and manipulating data

**Pandas**
 - For working with tabular data
 - DataFrame = tabular, column-oriented data structure with rows and column labels
 - Series = one-dimensional labeled array object
 - Best for data manipulation, preparation, and cleaning

**matplotlib**
 - To create plots suitable for publication 
 
##IPython Basics
**Tab**
 - While entereing expressions in the shell, press the Tab key to search for the namespace for any variables matching the characters you have typed so far
 
**Introspection**
 - Using a question mark (?) before or after a variable will display general inormation about the object
 
**The %run Command**
 - Run any file as a Python program by ussing the %run command
 
**Interrupting running code** 
 - Pressing Ctrl-C while code is running will cause a KeyboardInterrupt to be raised 

## Python Language Basics 
**Indentation**
 - Python uses whitespace to structure code
 - Always use 4 spaces, as is standard 

**Comments**
 - text preceded by # is ignored by Python interpreter
 - Hashtag is normally used to comment 
 - Comments can go on the same line of code (behind it), or on the line preceding the code 
 
**Argument Passing**
 - When assigning a variable in Python, you are creating a reference, see Practice-01.ipynb for example
 
**Dynamic reference, strong types**
 - Python is considered a strongly typed language, which means that every object has a specific type (or class), and implicit conversions will occur only in certain obvious circumstances
 
**Binary operations**
| Operation | Description |
| ----------- | ----------- |
| a + b | Add |
| a - b | Subtract |
| a * b | Multiply |
| a / b | Divde |
| a // b | Floor-divide a by b, dropping any fractional remainder |
| a** b | Raise a to the b power |
| a & b | True if both a and b are True |
| a &#124; b | True if either a or b is True | 
| a ^ b | For booleans, True if a or b is True, but not both |
| a == b | True if a equals b |
| a != b | True is a is not equal to b |
| a <= b, a < b | True if a is less than (less than or equal) to b |
| a > b, a >= b | True if a is greater than (greater than or equal) to b |
| a is b | True if a and b reference the same Python object |
| a is not b | True if a and b reference different Python objects |

 **Mutable and immutable objects**
  - Most objects in Python (lists, dicts, NumPy arrays, and most user-defined types (classes), are mutable
  - strings and tuples are immutable
 
 **Scalar Types**
 "Single Value" types refered to as scalars
| Type | Description |
| ----------- | ----------- |
| None | The Python “null” value (only one instance of the None object exists) |
| str | String type; holds Unicode (UTF-8 encoded) strings |
| bytes | Raw ASCII bytes (or Unicode encoded as bytes) |
| float | Double-precision (64-bit) foating-point number |
| bool | A True or False value |
| int | Arbitrary precision signed integer |

**Numeric types**
 - int (integer) can store arbitarily large numbers
 - float are floating-point numbers that can also be expressed with scientific notation 
 
**Strings**
 - Can write string literals using either single quotes ' or double quotes "
 - Multiline strings with line breaks can be written with triple quotes
 - Strings are immutable
 - Strings are a sequence of Unicode characters and therefore can be treated like other sequences, such as lists and tuples
 - The backslash character is an escape character, to write a string literal with backslashes you need to escape them with \\
