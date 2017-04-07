#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:31:04 2017

@author: macbook
"""

import pandas as pd
from matplotlib.pyplot import *
import numpy as np
matplotlib.style.use('ggplot')
#---------------IO Tools--------------------
'''
#读写csv文件
#pd.read_csv(filepath,header,names,skiprows,encoding)
#pd.to_csv(filepath,encoding)
len(pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv'))
pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv',header=0)
pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv',names=['qianchen1','qianchen2'])
len(pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv',skiprows=10))
pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv',encoding='utf-8')  #会出现乱码
pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv',encoding='utf-8')
'''

'''
#读写xlsx文件
wen2 = pd.read_excel('C:/Users/hunterlin/Documents/Python Scripts/sq.xlsx')
wen2
wen3 = pd.read_excel('C:/Users/hunterlin/Documents/Python Scripts/sq.xlsx',sheetname= u'非商圈')
wen3
'''


#---------------IO Tools--------------------

#---------------Intro to basic data structures------------- 

#Series对象创建
'''
pd.Series([1,2,3,4,5,6])
pd.Series({'a':'1','b':'2'})  #字典型，a,b是索引

pd.Series(np.array(np.random.randn(100)))
pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv')['zhuzhiaweizhi']
'''
#Series对象基本操作
'''
pd.Series(np.array(np.random.randn(100))).mean()
pd.Series(np.array(np.random.randn(100)))*2
np.exp(pd.Series(np.array(np.random.randn(100))))
'''
#Series对象基本属性
'''
pd.Series(np.array(np.random.randn(100))).drop_duplicates()
#drop_duplicates()去掉重复值,序列型去重
pd.Series(np.array(np.random.randn(100))).size
'''
k = pd.DataFrame({'a':pd.Series(np.array(np.random.randn(100))),
                  'b':pd.Series(np.array(np.random.randn(100)))})
k
k['a']
#del k['a'] 去掉某列
#print k
k['c'] = pd.Series(np.array(np.random.randn(100)))
k
k.size  #数据量
k.columns  #列名生成一个列表返回
k.T   #转置
k.sum(axis=0)
k.sum(axis=1)
type(k.values)
#分类问题
wen = pd.read_csv('C:/Users/hunterlin/Documents/Python Scripts/xm.csv')
wen.columns
grouped = wen.groupby('chaoxiang')
grouped.groups.keys()
cx1 = np.array(grouped.get_group('1')['unitprice'])
cx2 = np.array(grouped.get_group('2')['unitprice'])
cx3 = np.array(grouped.get_group('3')['unitprice'])
cx4 = np.array(grouped.get_group('4')['unitprice'])
cx5 = np.array(grouped.get_group('5')['unitprice'])
cx6 = np.array(grouped.get_group('6')['unitprice'])
cx7 = np.array(grouped.get_group('7')['unitprice'])
cx8 = np.array(grouped.get_group('8')['unitprice'])
cxx = []
na = grouped.groups.keys()
del na[0]
for i in range(0,len(na)):
    cxx.append(np.array(grouped.get_group(na[i])['unitprice']))
figure()
#boxplot(cxx)
#violinplot(cxx)
#hist(cxx)

#---------------Intro to basic data structures------------- 

#---------------Visualization------------- 
#pd.Series(np.array(np.random.randn(1000)),
#          index=pd.date_range('1/1/2000', periods=1000)).plot()
#pd.Series(np.array(np.random.randn(1000)),
#         index=pd.date_range('1/1/2000', periods=1000)).cumsum().plot()

k = pd.DataFrame({'a':pd.Series(np.array(np.random.randn(100))),
                  'b':pd.Series(np.array(np.random.randn(100))),
                  'c':pd.Series(np.array(np.random.randn(100))),
                  'd':pd.Series(np.array(np.random.randn(100)))})
del(k['a'])  #删掉某列
k['e']=pd.Series(np.array(np.random.randn(100)))  #添加某列
#k['a'].plot()
#k['b'].plot()
'''
wen = pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')
grouped = wen.groupby('chaoxiang')
grouped.groups.keys()
cx1 = np.array(grouped.get_group('1')['unitprice'])
cx2 = np.array(grouped.get_group('2')['unitprice'])
cx3 = np.array(grouped.get_group('3')['unitprice'])
cx4 = np.array(grouped.get_group('4')['unitprice'])
cx5 = np.array(grouped.get_group('5')['unitprice'])
cx6 = np.array(grouped.get_group('6')['unitprice'])
cx7 = np.array(grouped.get_group('7')['unitprice'])
cx8 = np.array(grouped.get_group('8')['unitprice'])
cxx = []
na = grouped.groups.keys()
del na[0]
for i in range(0,len(na)):
    cxx.append(np.array(grouped.get_group(na[i])['unitprice']))
figure()
boxplot(cxx,vert=False)
#violinplot(cxx)
#hist(cxx)
'''

#scatter(k['a'],k['b'])
#hexbin(k['a'],k['b'])
wen = pd.read_csv('/Users/macbook/Documents/qianchen/wiserclub/xm.csv')
#scatter(wen['unitprice'],wen['totalprice'])
#hexbin(wen['unitprice'],wen['totalprice'].fillna(wen['totalprice'].mean()))
#hist2d(wen['unitprice'].fillna(wen['unitprice'].mean()),
#       wen['totalprice'].fillna(wen['totalprice'].mean()))
hist(wen['unitprice'].fillna(wen['unitprice'].mean()),bins=100)