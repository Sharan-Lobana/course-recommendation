import load_data
import Costfunction as ccf
from scipy.optimize import minimize
import numpy as np

Y = load_data.Y
R = load_data.R

numstudents = load_data.numstudents
numcourses = load_data.numcourses
numfeatures = load_data.numfeatures

reg = 1000    #For limiting values of theta and course features
reg2 = 10 #For keeping modified values of theta close to original values

Y = Y[:numstudents,:numcourses]
R = R[:numstudents,:numcourses]

X = np.random.randn(numcourses, numfeatures)
Theta = load_data.Theta
print Theta
print "Before concatenate"
initial_parameters = np.concatenate((X.reshape(X.size, order='F'), Theta.reshape(Theta.size, order='F')))

def J(initial_parameters):
    return ccf.costfunction(initial_parameters, Y, R, numstudents, numcourses, numfeatures, reg, reg2, Theta)

maxiter = 2000
options = {'disp': True, 'maxiter':maxiter}

result = minimize(J, x0=initial_parameters, options=options, method="L-BFGS-B", jac=True )

params = result['x']

#Result interpretation
min_val = result['fun']
grad_val = result['jac']
message = result['message']
successful = result['success']
# Other attributes can be found at
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult

print "\n\n\nMin Value of the objective function: ",
print min_val
print "\nValue of gradient during exit: ",
print grad_val
print "\nExit Message: ",
print message
print "\nSuccess Code: ",
print successful
print "\n\n\n"

X = np.reshape(params[:numcourses * numfeatures], (numcourses, numfeatures), order='F')
Theta = np.reshape(params[numcourses * numfeatures:], (numstudents, numfeatures), order='F')
output = np.dot(Theta, X.T)

print output
