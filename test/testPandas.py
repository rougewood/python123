import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan, 44, 1])
print(s)

dates = pd.date_range('20130101',periods=6)
print(dates)

df= pd.DataFrame(np.random.randn(6,4),index=dates, columns=['a','b','c','d'])
print(df)

df1= pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)

print(df1.dtypes)
print(df1.index)
print(df1.columns)
print(df1.values)
print(df1.describe())

print(df1.T)

print(df.sort_index(axis=1, ascending=False))
      
print(df.sort_index(axis=0, ascending=False))
print(df.sort_values(by="b"))


df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
print(df)
print(df[0:3],df['20130102':'20130104'])


#select by label:loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df['A'])


#select by position: iloc
print(df.iloc[3:5, 1:3])
print(df.iloc[[1,3,5], 1:3])

#mixed slection:ix
print(df.ix[:3,['A','C']])

#Boolean indexing
print(df[df.A>8])


df.iloc[2,2] = 1111
print df

df.loc['20130101','B']=2222
print df

#df[df.A>4]=0
#print df

df.A[df.A>4]=0
print df

df['F']=np.nan
print df


df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101', '20130106',perieds=6))
print df

df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
print df

#print(df.dropna(axis=0, how='any'))# how ={ 'any', 'all'}
print(df.fillna(value=0))

print df

print(df.isnull())
print(np.any(df.isnull())==True)

#read_csv, to_csv

#concatenating
df1= pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2= pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3= pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

print(df1)
print(df2)
print(df3)



res = pd.concat([df1,df2,df3], axis = 0, ignore_index=True)
print res


#join, ['inner', 'outer']
df1= pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2= pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
print df1
print df2
res = pd.concat([df1,df2], join='outer')
print res
res = pd.concat([df1,df2], join='inner')
print res

#join_axes
res=pd.concat([df1,df2], axis=1)
print(res)
res=pd.concat([df1,df2], axis=1, join_axes=[df1.index])
print(res)

#append
df1= pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2= pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
res= df1.append(df2, ignore_index=True)
print res

df3= pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
res=df1.append([df2,df3], ignore_index=True)
print res

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
print s1
res= df1.append(s1,ignore_index=True)
print res


#merge
left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                'A':['A1','A2','A3','A4'],
                'B':['B1','B2','B3','B4']    })
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                'C':['C1','C2','C3','C4'],
                'D':['D1','D2','D3','D4']    })

print left
print right
res=pd.merge(left,right,on='key')
print res



left=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                   'key2':['K0','K1','K0','K1'],
                'A':['A1','A2','A3','A4'],
                'B':['B1','B2','B3','B4']    })
right=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                   'key2':['K0','K0','K0','K0'],
                'C':['C1','C2','C3','C4'],
                'D':['D1','D2','D3','D4']    })
print left
print right
#how=['left','right','inner','outer']
res= pd.merge(left,right,on=['key1','key2'], how='inner')
print res

res= pd.merge(left,right,on=['key1','key2'], how='right')
print res


#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print df1
print df2

res=pd.merge(df1,df2, on='col1', how='outer', indicator='indicator_column')
print res


#index
left=pd.DataFrame({'A':['A1','A2','A3'],
                'B':['B1','B2','B3']},
                   index=['K0','K1','K2'])    

right=pd.DataFrame({'C':['C1','C2','C3'],
                'D':['D1','D2','D3']},
                   index=['K0','K2','K3'])
print(left)
print(right)

res=pd.merge(left, right, left_index=True, right_index=True, how='outer')
print res

res=pd.merge(left, right, left_index=True, right_index=True, how='inner')
print res



#handle overlapping
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})

print boys
print girls

res=pd.merge(boys,girls, on='k', suffixes=['_boy','_girl'], how='inner')
print res





import matplotlib.pyplot as plt

#plot data
#Series
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
data.plot()
plt.show()

#DataFrame
data=pd.DataFrame(np.random.randn(1000,4),
                  index=np.arange(1000),
                  columns=list("ABCD"))
data=data.cumsum()
#print data.head()
data.plot()
plt.show()

#plot method:
#bar, hist, box, kde, area, scatter, hexbin, pie


ax= data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A',y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()



