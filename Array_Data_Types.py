'''
NumPy supports a much greater variety of numerical types than Python does. The following table shows different scalar data types defined in NumPy.
'''

            # Example 1

# using array-scalar type 
import numpy as np 
dt = np.dtype(np.int32) 
print dt

    # The output is as follows −

int32

            # Example 2

#int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc. 
import numpy as np 

dt = np.dtype('i4')
print dt 

    # The output is as follows −

int32

            # Example 3

# using endian notation 
import numpy as np 
dt = np.dtype('>i4') 
print dt
    # The output is as follows −

>i4

            # Example 4

# first create structured data type 
import numpy as np 
dt = np.dtype([('age',np.int8)]) 
print dt 
The output is as follows −

[('age', 'i1')] 

            # Example 5

# now apply it to ndarray object 
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print a

    # The output is as follows −

[(10,) (20,) (30,)]

            # Example 6

import numpy as np 

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print a

    # The output is as follows −

[('abc', 21, 50.0), ('xyz', 18, 75.0)]
