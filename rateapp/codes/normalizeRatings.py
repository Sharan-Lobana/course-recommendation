import numpy as np
import random

def normalizeRatings(Y,R,test_fraction):
    m, n = Y.shape
    Ymean = np.zeros((n,1))
    Ynorm = np.zeros(Y.shape)

    #Iterate for every course
    for i in xrange(n):
    	idx = R[:,i] == 1
        Ymean[i] = np.mean(Y[idx,i])
        Ynorm[idx,i] = Y[idx,i] - Ymean[i]

    # Generate the test data
    testY = np.zeros((m,n))
    testR = np.zeros((m,n))
    # Don't take out test data from latest user's ratings
    for i in range(m-1):
        for j in range(n):
            # Find if the current user has rated the current course
            if(R[i,j] != 0):
                # Take out test value with probability test_fraction
                if(random.random() < test_fraction):
                    testY[i,j] = Ynorm[i,j]
                    testR[i,j] = 1
                    Ynorm[i,j] = 0;
    return Ynorm, Ymean, testY, testR, R
