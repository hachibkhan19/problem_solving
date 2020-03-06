# Calculate perfect square number.
from math import sqrt
for i in range(1, 501):    
    sq = sqrt(i)
    if i % sq == 0:        
        print(i)


