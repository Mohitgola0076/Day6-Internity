'''
The most important object defined in NumPy is an N-dimensional array type called ndarray. It describes the collection of items of the same type. Items in the collection can be accessed using a zero-based index.
Every item in an ndarray takes the same size of block in the memory. Each element in ndarray is an object of data-type object (called dtype).
'''

            # Example 1

import numpy as np 
a = np.array([1,2,3]) 
print a

    # The output is as follows −
    
[1, 2, 3]


            # Example 2
    
# more than one dimensions 
import numpy as np 
a = np.array([[1, 2], [3, 4]]) 
print a

    # The output is as follows −

[[1, 2] 
 [3, 4]]

           # Example 3

# minimum dimensions 
import numpy as np 
a = np.array([1, 2, 3,4,5], ndmin = 2) 
print a

    # The output is as follows −

[[1, 2, 3, 4, 5]]

            # Example 4

# dtype parameter 
import numpy as np 
a = np.array([1, 2, 3], dtype = complex) 
print a 

    # The output is as follows −

[ 1.+0.j,  2.+0.j,  3.+0.j]
