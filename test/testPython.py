condition=1
while condition<10:
    print condition
    condition = condition+1


for i in range(1,10):
    print i

def f(a,b):
    print(a,b)

f(1,2)

class Calculator:
    def add(self,x,y):
        print x+y

cal = Calculator()
cal.add(1,2)


#tuple list
a_tuple=(1,2,2,4)
another_tuple=2,3,4

a_list=[12,34,55,32]


a=[1,2,3,4,5]
multi_dim_a=[[1,2,3],
             [2,3,4],
             [3,4,5]]
print(a[0])
print(multi_dim_a[2][2])

#dictionary
d={"apple":1,"pear":2,"orange":{1:2,2:3}}
d2={1:'a',2:'b', 'c':'d'}
print(d["apple"])

del d["pear"]
print d


d["b"]=20
print d

a = [1,2,3]
b=[4,5,6]
print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i/2,j*2)

print(list(zip(a,a,b)))


#lambda
def fun1(x,y):
    return x+y
fun2= lambda x,y: x+y

#map
map(fun1,[1],[2])
print(list(map(fun1,[1],[3])))


print(list(map(fun1,[1,3],[2,4])))

#import copy
a=[1,2,3]
b=a
print(id(a),id(b))



#set
char_list=['a','b','c','c','d','d','d']
print(type(set(char_list)))
print(type({1:2}))
