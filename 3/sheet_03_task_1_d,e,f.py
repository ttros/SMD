import matplotlib .pyplot as plt
import numpy as np
from project_a2.random import LCG

#d)

random = np.random.default_rng(666)
generator = LCG(0, a=1601, c=3456, m=10000)
x1, y1, z1 = generator.uniform(size =(3, 10000))


plt.hist(x1, 100)
#plt.show ()

#e)

fig = plt.figure ()

ax = fig. add_subplot (1, 1, 1)

ax.scatter(
    x1, y1,
    s=5, # smaller points
    alpha =0.3 , # 70% transparency
)
# set the orientation of the 3d axis

#plt.show ()


#3-dimensional

fig = plt.figure ()

ax = fig. add_subplot (1, 1, 1, projection ='3d')

ax.scatter(
    x1, y1, z1,
    s=5, # smaller points
    alpha =0.3 , # 70% transparency
)
# set the orientation of the 3d axis
ax. view_init (elev =30, azim =20)
#plt.show ()

#f)

#histogram
x2, y2, z2 = random.uniform(size =(3, 10000))

plt.hist(x2, 100)
#plt.show ()


#2-dimensional

fig = plt.figure ()

ax = fig. add_subplot (1, 1, 1)

ax.scatter(
    x2, y2,
    s=5, # smaller points
    alpha =0.3 , # 70% transparency
)
# set the orientation of the 3d axis

#plt.show ()


#3-dimensional

fig = plt.figure ()

ax = fig. add_subplot (1, 1, 1, projection ='3d')

ax.scatter(
    x2, y2, z2,
    s=5, # smaller points
    alpha =0.3 , # 70% transparency
)
# set the orientation of the 3d axis
ax. view_init (elev =30, azim =20)
#plt.show ()