import numpy as np

qtd = [1,10,20,50]
custo = [100,12,200,1000]

arr1 = np.array(qtd)
arr2 = np.array(custo)


print(arr1)
print(arr2)

count = arr1*arr2
print(count)

aren = np.arange(0,51,2)
print(aren)

lis = np.linspace(0,1,10)
print(lis)


ex1 = np.random.rand(10)
print(ex1)

ex2 = np.random.rand(16)
print(ex2)

ex3 = np.random.randint(1,11,10)
print(ex3)

matr = np.zeros((4,5))
print(matr)

matr1 = np.ones((4,5))
print(matr1)

matr2 = np.eye((5))
print(matr2)

num = np.random.randint(15,30,25)
print(num)

maior18 = num > 18
print(len(maior18))