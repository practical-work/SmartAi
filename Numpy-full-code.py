import numpy as np

# array creation

arr0 = np.array([1,3,5,4])
#print(arr0)
arr1 = np.zeros((2,3))
#print(arr1)
arr2 = np.ones((3,5))
# print(arr2)
arr3 = np.full((3,4),7)
# print(arr3)
arr4 = np.arange(2,10,2)
# print(arr4)
arr5 = np.linspace(1,5,10)
# print(arr5)

# Identity matrix creation
arr6 = np.eye(3)
# print(arr6)

# Know space,size,data type , change type, no. of dimensions

# print(np.shape(arr3))
# print(np.size(arr3))
# print(np.ndim(arr3))
# print(arr3.dtype)
# arr7 = arr3.astype(float)
# print(arr7)

# Arthimetic operations +,-,*,**,%,//,/ etc.- Broadcasting and vectorisation
# arr4 = [2,4,6,8]

# print(arr4 + 3)
# print(arr4 ** 2)
# print(arr4 % 2)
# print(arr4 * 2)
# print(arr4 // 3)  # firstly divide element with 3 then take GIF
# print(arr4 / 3)

# aggregation functions - min,max,sum,prod,std,var,mean,median,argmin,argmax
#arr4 = [2,4,6,8]

# print(arr4.sum())
# print(np.sum(arr4))
# print(np.prod(arr4))
# print(arr4.std()) #standard deviation
# print(np.var(arr4)) #variance
# print(arr4.mean())
# print(arr4.max())
# print(arr4.min())
# print(np.median(arr4))
# print(np.argmax(arr4))
# print(arr4.argmin())

#Some usefull function in numpy

# print(np.sqrt(arr4)) 
arr8 = np.array([2.467,-7.634,3.66624,1,0.536,-14.63173])
# print(np.sort(arr8))
# print(np.abs(arr8)) 
# print(np.ceil(arr8))
# print(np.round(arr8,3))
# print(np.floor(arr8))
# print(np.exp(arr8))
# print(np.log(arr8))

#indexing (same as in list) and slicing (same as in list ) ,fancy indexing (Select multiple elements from array using indexes) & boolean masking (filterout elements from array based on condition )
#arr4 = [2,4,6,8]

# print(arr4[2]) # if array of 2 dimensions use arr[row no.,col no.]
# print(arr4[[0,2]]) # boolean masking
# print(arr4[1:3])  #arr4[start:stop:step]

# print(arr4[arr4>4]) # boolean masking
# print(arr4[arr4 % 2 == 0])
# print(arr4[(arr4 > 4) & (arr4 < 8)])
# print(arr4[(arr4 > 4) | (arr4 < 8)])
# print(arr4[~(arr4 > 4)])
# print(arr4[~((arr4 > 4) & (arr4 < 8))])

# Reshaping and manupulating array
arr9 = np.array([[2,3],[4,5],[6,7]])
# print(arr9)

# print(arr9.reshape(2,3)) # reshape - view change in original array

''''ravel - convert ndim to 1 dimension and view change in original
  array but using flatten provide copy no change in original array
''' 
# print(arr9.flatten())
# print(arr9.ravel())

# insert,concatenation,delete,append,stacking,splitting
''' use arr4 = [2,4,6,8] and arr9 = [[2 3]
                                     [4 5]
                                     [6 7]] '''

# arr10 = np.insert(arr4,1,3,axis=None) # axis - 0 for row-wise,1 for column-wise & none for flattend array or 1 dimentional array
# # print(arr10)
# arr11 = np.insert(arr9,2,(12,9),axis=0)
# arr12 = np.insert(arr9,1,(1,2,3),axis=1)
# print(arr11,arr12)

# arr13 = np.append(arr4,5)
# print(arr13)
# arr14 = np.append(arr9,[43,22])
# print(arr14)

# arr15 = np.concatenate((arr4,arr0),axis=0)
# print(arr15)

# arr16 = np.delete(arr9,1,axis=0)
# print(arr16)

# arr17 = np.split(arr4,2)
# print(arr17)

# print(np.hsplit(arr4,2))
# print(np.vsplit(arr9,3)) # vertical split
# print(np.hsplit(arr9,2)) # horizontal split

# print(np.hstack((arr4,arr0))) # horizontal stack
# print(np.vstack((arr4,arr0))) # vertical stack

# linear algebra - dot product, matrix multiplication, inverse, determinant, eigen values and eigen vectors
arr18 = np.array([[1,2],[3,4]])
# print(np.dot(arr18,arr18)) # dot product
# print(np.matmul(arr18,arr18)) # matrix multiplication
# print(np.linalg.inv(arr18)) # inverse
# print(np.linalg.det(arr18)) # determinant
# print(np.linalg.eig(arr18)) # eigen values and eigen vectors
# print(np.linalg.solve(arr18,[5,11])) # solve linear equations
# print(np.linalg.norm(arr18)) # norm of a matrix
# print(np.trace(arr18)) # trace of a matrix
# print(np.transpose(arr18)) # transpose of a matrix

# sorting and searching - sort, argsort, searchsorted, unique, where
arr19 = np.array([3,1,4,2,5]) 
# print(np.sort(arr19))
# print(np.argsort(arr19))
# print(np.searchsorted(arr19,3))
# print(np.unique(arr19))
# print(np.where(arr19>3))  

# random number generation - rand, randn, randint, choice, seed
# print(np.random.rand(3,4)) # uniform distribution 
# print(np.random.randn(3,4)) # normal distribution 
# print(np.random.randint(1,10,(3,4))) # random integers between 1 and 10
# print(np.random.choice(arr4,3)) # random choice from an array 
# print(np.random.seed(42)) # set seed for reproducibility
# print(np.unique(np.random.randint(1,10,(3,4)))) # unique random integers between 1 and 10
# print(np.random.shuffle(arr4)) # shuffle an array in place
# print(np.count_nonzero(arr4)) # count non-zero elements in an array

# Handling missing values - nan, isna, fillna, dropna
arr20 = np.array([-4,56,np.nan,3,-np.nan,-np.inf,435,np.inf])
# print(arr20)
# #(np.nansum(arr20))
# print(np.isnan(arr20))
# print(np.isnan(arr20).sum())
# print(np.isinf(arr20))
# print(np.isfinite(arr20))

arr21 = np.nan_to_num(arr20,nan=7,posinf=10,neginf=-10)
# print(arr21)
