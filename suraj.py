import numpy as  np
import pandas as pd


# a = np.array([
#     1,2,3],dtype='S')
# print(a,type(a),a.dtype)

# a = np.ones((6,2,3))
# print(a)

# a = np.arange(0,10,1)
# print(a)

# a = np.linspace(0,5,num=10)
# print(a)


#3d

# a = np.random.rand(3,4,4,)
# print(a)

# a =np.full((3,4),5)
# print(a)


a =np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
# print((a[2]
# print(a[2]+a[3])

# print(a[1,1,3])

# a =np.array([1,2,3,4,5,6,7,8,9,10])
# print(a[::-1])
# print(a[0:10])
# print(a[0:5:2])


# a =  np.array([[1,2,3,4,5],
#                [6,7,8,9,10]])
# print(a[0:2,1:3])


# a = np.array(
#     [
#         [[1,2,3,4,5],
#          [6,7,8,9,10]],
#         [[11,12,13,14,15],
#          [16,17,18,19,20]]
#     ]
# )
# print(a[1,0,3])


# a =np.array([1,2,3,4,5,6,7,8,9])
# x= a.copy()
# print(a)
# a[0]=50
# print(a)
# print(x)
# x = a.view()
# print(x)

# a=np.array([[1,2,3,4],[5,6,7,8]])

# print(a.shape)


#tranpose matrix

# a = np.array([[1,2,3,],[7,4,9],[7,4,19]])
# res = np.transpose(a)
# print(res)

# 

# a = np.array([[1,2,3],[4,5,6]])
             
# # res = np.append(a,[[7,8,9],[19,12,23]],axis = 1)
# # print(res)

# # res = np.insert(a,3,[11,12])



# a = np.array([1,2,3,4,5])
# a[1],a[4] = a[4],a[1]
# print(a)


# a = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])
# print(a)

# a[[0,1,2],:] = a[[2,0,1],:]
# print(a)

# a[:,[1,3]] = a[:,[3,1]]
# print(a)


# a = np.array([
#     [
#     [1,2,3],
#     [2,3,4]
#     ],
#     [
#     [11,12,13],
#     [14,15,16]
#     ],
#     [
#     [23,24,25],
#     [26,27,28]
#     ]
# ]) 
# print(a)
# a[[],:,:]=a[[],:,:]   
# print(a)


#misssing data

# a = np.array(
#     [1,2,np.nan,5,np.nan,8]
# )
# res =np.isnan(a)
# print(a)
# print(res)

# res = np.nan_to_num(a,nan=0)
# print(res)


# a = np.array(
#     [[1,2,3,4,5],[11,12,13,14,15]]
# )
# np.save('data.npy',a)
# res =np.load('data.npy')
# print(res)


with open('data.txt','w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")

data = np.loadtxt('data.txt')
print(data)