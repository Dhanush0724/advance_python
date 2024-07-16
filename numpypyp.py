import numpy as np

# x = [2,4,5,6,9,8]
# num_array = np.array(x)
# sum = np.sum(num_array)
# product = np.prod(num_array)
# print(sum,product)

# num_array = np.arange(9)
# matrix = num_array.reshape(3,3)
# print(num_array)
# print(matrix)

# list = [1,2,3,4,5,6,7,8,9]
# num_array = np.array(list)
# print(np.mean(num_array),np.median(num_array),np.std(num_array))


# list = [7,5,2,4,1,3,6,9]
# num_array = np.array(list)
# print(np.sort(num_array))


# list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# array_2d = np.array(list)
# row_sum = np.sum(array_2d, axis=1)
# col_sum = np.sum(array_2d,axis=0)
# print(row_sum)
# print(col_sum)

# random_array = np.random.randint(1,100,size=10)
# print(np.max(random_array))
# print(np.min(random_array))

# arr = [2,4,6,8]
# num_array = np.array(arr)
# print(np.square(num_array))

# arr = [2,4,6,8]
# num_array = np.array(arr)
# print(np.dot(num_array,num_array))


# matrix = np.array([[1,2],
#                    [3,4]])
# inverse = np.linalg.inv(matrix)
# print(inverse)

array = np.array([[1,2,3],
                  [4,5,6]])
transposed = np.transpose(array)
print(transposed)

