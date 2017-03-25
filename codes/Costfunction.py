import numpy as np


def costfunction(params,Y, R, num_students, num_courses, num_features, reg_param):

    # X is courses*features
    # Theta is students*parameters
    X = np.reshape(params[:num_courses * num_features], (num_courses, num_features), order='F')
    Theta = np.reshape(params[num_courses * num_features:], (num_students, num_features), order='F')

    # Take dot product of theta and x transpose to compute predicted rating
    # Compute squared error
    squared_error = np.power(np.dot(Theta, X.T) - Y, 2)
    # Contribution to squared error will come only from those ratings which
    # are not missing and which have not been relocated to test data
    J = (1 / 2.) * np.sum(squared_error * R)

    #Add contribution of theta and x to objective funciton incorporating the regularization parameter
    J = J + (reg_param / 2.) * (np.sum(np.power(Theta, 2)) + np.sum(np.power(X, 2)))

    X_grad = np.dot(Theta.T, (np.dot(Theta, X.T) - Y) * R).T
    Theta_grad = np.dot(((np.dot(Theta, X.T) - Y) * R), X)

    X_grad = X_grad + reg_param * X
    Theta_grad = Theta_grad + reg_param * Theta

    grad = np.concatenate((X_grad.reshape(X_grad.size, order='F'), Theta_grad.reshape(Theta_grad.size, order='F')))

    return J , grad
