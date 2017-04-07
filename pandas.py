# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:53:56 2017

@author: hunterlin
"""
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

obj=Series([4.5,7.4,3.5,3.2],index=['a','s','f','e'])
obj
#对索引重命名 obj,index=(['e','r','t','x'])
#按照索引重新排序
obj2=obj.reindex(['a','e','f','s','x'])
obj2
obj.reindex(['a','e','f','s','x'],fill_value=0) #填补缺失值，但不会对元数据造成影响

frame=DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Ohio','Texas','California'])
frame

frame2=frame.reindex(['a','b','c','d'])
states=['Texas','Unite','California']
frame.reindex(columns=states)

import pandas.io.data as web
all_data={}
for ticker in ['AAPL','IBM','MSFT']:
    all_data[ticker]=web.get_data_yahoo(ticker,'1/1/2000','1/1/2001')
    
price=DataFrame({tic:data['Adj Close']
                        for tic,data in all_data.items()}):
                            
obj=Series(['a','b','a','e','d'])
obj.value_counts

data=DataFrame({'a':[1,3,4],'b':[2,3,5]})
data
data.apply(pd.value_counts,axis=1).fillna(0)