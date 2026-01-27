import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

b=np.zeros((3, 4))
print (b)

c=np.arange(1,10,2)
print(c)        


d=np.array([1,1,1,1,])
e=np.array([2,2,2,2])
print(d + e) 
print(d * e)

f=np.array([1,2,3,4,5,6])

print(f)
print(f[1:2],f[2:5])
print(np.sum(f))
print(np.mean(f))
print(np.max(f))
print(np.std(f))
