#import a function from another module

from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")



#Alternatively

import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
