
# coding: utf-8

# In[1]:

import numpy as np
import scipy.optimize as opt
from scipy.optimize import fmin_bfgs


# In[2]:

class Value_func:
    def __init__(self, alpha='', beta='', delta='', s = ''):
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.s = s
        #Here is a method

    def steady_state(self):
        return (self.alpha/(1/self.beta - 1 + self.delta))**(1/(1-self.alpha))

    def utility(self):
        v0=np.zeros([N,3])
        v1=np.zeros([N,3])
        policy=np.zeros([N,3])
        k=self*np.exp(x)/(np.exp(x)+1)
        klo=np.sum(k>kmat)
        if c>0:
            u1=(1/(1-s))*(c**(1-s)-1)
        else:
            u1=-9999999999
        return -1*(u1+beta*vn)

    def kmat(self, tol=[0.01,3,500]):
        #method kmat arguments are the range of ks and fineness of grid
        kss = self.steady_state()
        kmin = tol[0]*kss
        kmax = tol[1]*kss
        kmat = np.linspace(kmin,kmax,tol[2])
        v0=np.zeros([N])
        v1=np.zeros([N])
        policy=np.zeros([N])
        for j in range(0,tol[2]):
            k0=kmat[j]






# In[20]:

for j in 0:100:
        print(j)


# In[3]:

alpha = 0.3
beta = 0.95
delta = .1
s = 0.3


# In[4]:

val = Value_func(beta=.9, delta=.05, s=.4, alpha = .3)


# In[5]:

val.alpha


# In[6]:

val.steady_state()


# In[11]:

x = val.kmat(tol=[.2, 3, 100])


# In[15]:

for ind in x:
    print(x)
    print ('heee')


# In[9]:

amat=np.array([0.9,1,1.1])


# In[10]:

amat


# In[ ]:



