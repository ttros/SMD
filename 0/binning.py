import matplotlib.pyplot as plt
import numpy as np

height, weight = np.genfromtxt('height_weight.txt', unpack = True)

plt.hist(height, bins = 10)

def binning(data,x,y):
    plt.subplot(3,2,x)
    plt.hist(data, y)
    

binning(height,1,5)
binning(height,2,10)
binning(height,3,15)
binning(height,4,20)
binning(height,5,30)
binning(height,6,50)

plt.savefig('binning/1.pdf')
plt.close()

binning(weight,1,5)
binning(weight,2,10)
binning(weight,3,15)
binning(weight,4,20)
binning(weight,5,30)
binning(weight,6,50)

plt.savefig('binning/2.pdf')
plt.close()

plt.scatter(
    height,
    weight,
    s=5,
    alpha=1,
    linewidth=0,
)
plt.savefig('binning/3.pdf')
plt.close()

xx = np.log(np.random.uniform(1,100,10**5))

binning(xx,1,5)
binning(xx,2,10)
binning(xx,3,15)
binning(xx,4,20)
binning(xx,5,30)
binning(xx,6,50)

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('binning/4.pdf')
plt.close()


