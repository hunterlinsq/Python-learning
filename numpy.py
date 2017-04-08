# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
arr1

data2=[[1,2,3,5],[5,6,7,8]]
arr2=np.array(data2)
arr2
arr2.ndim  
arr2.shape   #数据各维度的大小

arr1.dtype   #说明数据类型的对象 float64 浮点
arr2.dtype   #数据类型 int64  整数

np.zeros(10)  #创建全0的数组
np.ones(10)  #创建全1的数组
np.zeros((3,6))
np.empty((2,3,2)) #返回的是一些未初始化的垃圾值，并不会返回0值
np.arange(15)

#指定数组数据类型
arr1=np.array([1,2,3],dtype=np.float64)
arr1.dtype
arr2=arr1.astype(np.int64)  #转换数据类型
arr2.dtype
arr3=arr1.astype(np.string_)  #字符串格式
arr3.dtype
arr3

np.array(['1.3','2.5','3'],dtype=np.string_)
np.array(['a','b','c'],dtype=np.string_)

#数组和标量之间的运算
arr=np.array([[1,2,3],[4,5,6]],dtype=np.float64)
arr*arr
1/arr
arr*0.5
arr**0.5   #取根号

#取子集
arr=np.arange(10)
arr[5]   #第5个数，而数组是从0开始算
arr[5:8]
arr[5:8]=12
arr_slice=arr[5:8]   #取切片的一份视图
arr_slice[1]=123  #在视图上面的修改也会直接反映到原数组上
arr
arr_slice[:]=32
arr

arr=np.arange(10)
arr2=arr[5:8].copy()  #取切片的副本
arr2[1]=123
arr

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[0]
arr2d[0][2]
arr2d[0,2] #与上面等价

arr3d=np.array([[[1,2,3],[4,5,6]],[[2,4,5],[7,9,3]]])
arr3d
arr3d[0]  #是一个2*3的数组
arr3d[0]=[4,3,1]
arr3d[0,0,0] #检索

#高维的切片方式
arr2d   #注意python中数组是从0开始算的
arr2d[:2]  #第2行之前
arr2d[2:]  #第2行及其之后
arr2d[:2,:1] #第2行之前，第1列之前
arr2d[:2,1:] #第2行之前，第一列及其之后
arr2d[:2,2]  #第2行之前的第2列
#只有冒号表示选取整个轴
arr2d[:,:2]


##布尔型索引
names=np.array(['Bob','Joe','Will','Bob'])
data=np.random.rand(4,3)
data
data[names=='Bob']
data[names=='BOb',2:]
data[data<0]=0
data
data[names!='Joe']=7
data


##花式索引(Fancy indexing)
arr=np.empty((8,4))
for i in range(8):
    arr[i]=i

arr
arr[[4,3,0,6]]  #指定顺序的整数列表
arr[[-3,-5,-7]]  #从末尾开始选取

arr=np.arange(32).reshape((8,4))
arr
#区分以下
arr[1,3]
arr[(1,3)]  #与上面一样
arr[[1,3]] 
arr[[1,5,7,2],[0,3,1,2]] #此时返回的却是一个4个数一维数组，前面相当于第一轴，后面为第二轴

#想要从多维度选取指定顺序的列表：
arr[[1,5,7,2]][:,[0,3,1,2]]
#另一种方法np.ix_()
arr[np.ix_([1,5,7,2],[0,3,1,2])]
#注意花式索引总是将数据复制到新数组


#数组转置和轴兑换
arr.T #转置
np.dot(arr.T,arr) #矩阵内积
#对高维数组转置transose()
arr=np.arange(16).reshape((2,2,4))
arr.T  #转置为(4,2,2)
arr.transpose((1,0,2))  #这边不太懂是怎么转化的
arr.swapaxes(1,2)


#通用函数：快速的元素级数组函数
#ufunc
arr=np.arange(10)
np.sqrt(arr)  #开根号
np.exp(arr)   #exp(x)
arr1=np.random.rand(10)
np.max(arr)
np.maximum(arr,arr1)  
np.modf(arr1)  #分离小数部分和整数部分

#用数组表达式代替循环
#也被称为矢量化，速度更快
points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)  #这会生成两个数组，前者为维度a*b，后者维度为b*a




