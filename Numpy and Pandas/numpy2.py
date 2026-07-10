import numpy as np
#print(np.__version__)

#array creation
array = np.array([1, 2, 3, 4, 5])
#print(array)
array = array + 1
#print(array)

#print(type(array))

#multi-dimensional array
array2 = np.array([[[1 , 2 ,3],[4,3,1],[5,6,7]],
                [[1,6,3],[4,3,1],[5,0,7]]])
#print(type(array2))
#print(array2.shape)
#print(array2[1][0][0])#chain indexing
#print(array2[0,2,0])#fancy indexing
word = array2[0,1,1] + array2[1,2,2] * array2[0,0,1]
#print(f"word = {word}")


#slicing

array3 = np.array([[1,2,3,4],
                    [4,3,1,5],
                    [5,6,7,6],
                   [1,6,3,1]])

#array [start:stop:step]
#print(array3[0:2])
#print(array3[0:4:3])
#print(array3[0:4:3, 0:4:2]) 
#print(f"Reversed array:\n{array3[::-1]}")
#print(array3[:,0])#column 0
#print(array3[0, :])#row 0
#print(array3[:, 0:3])
#print(array3[:, 1:3])
#print(array3[2:, 0:3])
#print(array3[0:2, 0:3])
#print(array3[0:2, 1:3])



#arthemictic operations
#scalar operations - means single value operations

'''array4 = np.array([1,2,3,4])
print(array4 + 1)                
print(array4 - 1)
print(array4 * 2)   
print(array4 / 2)
print(array4 ** 2)#power'''

#vectorized operations - means operations on arrays
'''array5 = np.array([1.9, 2.1, 3, 4.5])
print(np.sqrt(array5))
print(np.floor(array5))
print(np.ceil(array5))
print(np.round(array5))'''

radi = np.array([1,2,3,4])
#print(np.pi * radi ** 2) #area of circle = pi * r^2

'''print(array5 - radi)
print(array5 * radi)
print(array5 / radi)
print(array5 + radi)
print(array5 ** radi)'''

#comparison operations
'''scores = np.array([80, 90, 70, 60, 50])
print(scores == 100)
print(scores > 70)
print(scores < 70)
scores[scores < 60] = 0
print(scores)'''


#broadcasting
array6 = np.array([[1,2,3,4]])
array7 = np.array([[1],[2],[3],[4]])
'''print(array6.shape)
print(array7.shape)
print(array6 + array7)
print(array6 * array7)'''
#eg : (1,4)etheir rows and columns has to match or 1
     #(3,1)

#aggregate functions

'''print(np.sum(radi))
print(np.mean(radi))
print(np.max(radi))
print(np.min(radi))
print(np.std(radi))# std = standard deviation
print(np.var(radi))# var = variance
print(np.median(radi))
print(np.percentile(radi, 50))#50th percentile
print(np.argmax(radi))#index of max value
print(np.argmin(radi))#index of min value
print(np.argsort(radi))#index of sorted array   
print(np.unique(radi))#unique values
print(np.isin(radi, [1, 3]))#check if values are present in array
print(np.where(radi > 2))#index of values greater than 2
print(np.count_nonzero(radi > 2))#count of values greater than 2
'''



#filtering
filtered = radi[(radi > 2) & (radi < 4)]
nap = radi[(radi <= 1)]
odd = radi[radi % 2 != 0]
even = radi[radi % 2 == 0]
'''print(filtered)
print(nap)
print(odd)
print(even)
napp = np.where(radi < 1 )
print(napp)'''

#random numbers

rng = np.random.default_rng()# seed used to generate same random numbers every time
#remove seed to generate different random numbers every time
print(rng.integers(1, 5))#5 random integers between 0 and 1
print(rng.integers(low = 1, high = 105 , size = 2))
print(rng.integers(low = 1, high = 105 , size = (2, 3)))#
rng.shuffle(radi)
print(radi)

