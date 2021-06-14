'''
A new ndarray object can be constructed by any of the following array creation routines or using a low-level ndarray constructor.
'''

numpy.empty
 # It creates an uninitialized array of specified shape and dtype. It uses the following constructor −
numpy.empty(shape, dtype = float, order = 'C')

            # Example 1
 # The following code shows an example of an empty array.

import numpy as np 
x = np.empty([3,2], dtype = int) 
print x

    # The output is as follows −

[[22649312    1701344351] 
 [1818321759  1885959276] 
 [16779776    156368896]]

#############################################

numpy.zeros
 # Returns a new array of specified size, filled with zeros.
numpy.zeros(shape, dtype = float, order = 'C')

            # Example 2

# array of five zeros. Default dtype is float 
import numpy as np 
x = np.zeros(5) 
print x

    # The output is as follows −

[ 0.  0.  0.  0.  0.]

            # Example 3

import numpy as np 
x = np.zeros((5,), dtype = np.int) 
print x

    # Now, the output would be as follows −

[0  0  0  0  0]

###############################

numpy.ones
    # Returns a new array of specified size and type, filled with ones.
numpy.ones(shape, dtype = None, order = 'C')


            # Example 4

# array of five ones. Default dtype is float 
import numpy as np 
x = np.ones(5) 
print x
The output is as follows −

[ 1.  1.  1.  1.  1.]


            # Example 2

import numpy as np 
x = np.ones([2,2], dtype = int) 
print x
    # Now, the output would be as follows −

[[1  1] 
 [1  1]]
