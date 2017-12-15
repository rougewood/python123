import numpy as np

a = np.array([1,2,3])
print(a.dtype)


b= np.zeros((3,4))
print(b)

c=np.ones((3,4))
print(c)

d=np.empty((3,4))
print(d)

e= np.arange(10,20,2)
print(e)

f=np.linspace(1,10,6).reshape(2,3)
f=f**2
print(f)



print(f<3)

g = np.random.random((2,4))
print(g)

print(np.sum(g))
print(np.max(g, axis=0))
print(np.min(g))


A = np.arange(2,14).reshape((3,4))
print(np.argmin(A))
print(np.mean(A))
print(A.mean())
print(np.average(A))
print(np.median(A))
print(np.cumsum(A))
print(A)
print(np.diff(A))
print(np.nonzero(A))

print(np.transpose(A))
print(A.T).dot(A)
print(np.clip(A,5,9))


B = np.arange(3,15).reshape(3,4)
print(B)
print(B[1][1])
print(B[1,1])
print(B[2,:])
print(B[1,1:3])


for row in B:
    print(row)

for column in B.T:
    print(column)

print(B.flatten())
for item  in B.flat:
    print(item)

A = np.arange(12).reshape(3,4)
print(A)
print(np.split(A,2,axis=1))
print(np.array_split(A,3,axis=1))
print(np.vsplit(A,3))
print(np.hsplit(A,2))

a= np.arange(4)
b=a

b=a.copy()#deep copy




