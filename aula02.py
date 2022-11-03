import numpy as np
num = np.random.randint(15,30,25)
print(num)

maior18 = (num > 18)
print(len(num[maior18]))