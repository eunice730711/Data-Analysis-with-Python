"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/np.sum(np.exp(x),axis=0)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
# numpy.arange(start=(-2.0),stop=(6.0),step=(0.1),dtype=None)
# numpy.arange(start,stop,step,dtype=None)
# example:
# >>> np.arange(3,7,2)
# array([3, 5])

scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
# print(scores)
# numpy.vstack(tup):
# Take a sequence of arrays and stack them vertically to make a single array. 
# Rebuild arrays divided by vsplit.
# >>> a = np.array([1, 2, 3])
# >>> b = np.array([2, 3, 4])
# >>> np.vstack((a,b))
# array([[1, 2, 3],
#        [2, 3, 4]])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()