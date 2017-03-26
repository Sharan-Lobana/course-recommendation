import numpy as np
import scipy.io as sio
import pandas as pd

matfile = sio.loadmat('/home/hp/dashboard/dataset.mat')
print matfile
y = matfile['Y']
r = matfile['R']
courses=[]
users=[]

'''for i in list(range(10)):
    print i
'''
for i in list(range(len(y))):
    users.append('user'+ str(i+1))
for i in list(range(len(y[0]))):
    courses.append('course'+ str(i+1),)

dfy = pd.DataFrame(y, index = users, columns = courses)
dfr = pd.DataFrame(r, index = users, columns = courses)
#print dfr
print dfy

parameter = sio.loadmat('/home/hp/dashboard/parameters.mat')
print parameter

