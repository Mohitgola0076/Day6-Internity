'''
Contents of ndarray object can be accessed and modified by indexing or slicing, just like Python's in-built container objects.
Three types of indexing methods are available − field access, basic slicing and advanced indexing.
Basic slicing is an extension of Python's basic concept of slicing to n dimensions. A Python slice object is constructed by giving start, stop, and step parameters to the built-in slice function. This slice object is passed to the array to extract a part of array.
'''

            # Example 1

import numpy as np 
a = np.arange(10) 
s = slice(2,7,2) 
print a[s]

    # Its output is as follows −

[2  4  6]

            # Example 2

import numpy as np 
a = np.arange(10) 
b = a[2:7:2] 
print b

# Here, we will get the same output −

[2  4  6]

            # Example 3

# slice single item 
import numpy as np 

a = np.arange(10) 
b = a[5] 
print b

    # Its output is as follows −

5

            # Example 4

# slice items starting from index 
import numpy as np 
a = np.arange(10) 
print a[2:]

    # Now, the output would be −

[2  3  4  5  6  7  8  9]

            # Example 5

# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print a[2:5]

    # Here, the output would be −

[2  3  4] 


            # Example 6

import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print a  

# slice items starting from index
print 'Now we will slice the array from the index a[1:]' 
print a[1:]

    # The output is as follows −

[[1 2 3]
 [3 4 5]
 [4 5 6]]

    # Now we will slice the array from the index a[1:]
[[3 4 5]
 [4 5 6]]
