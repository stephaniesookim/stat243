# 2(c)
import numpy as np
from decimal import Decimal
vec=np.array([1e-16]*(10001))
vec[0]=1
print (np.sum(vec))

# 2(d)
vec = np.array([1e-16]*(10001))
vec[0] = 1.0

fl1 = 0
for i in range(len(vec)):
  fl1 += vec[i]
print(Decimal(fl1))

fl2 = 0
for i in range(1, len(vec)):
  fl2 += vec[i]
fl2 = fl2 + vec[0]
print(Decimal(fl2))