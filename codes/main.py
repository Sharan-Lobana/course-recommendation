import load_data
import numpy as np
import random
import normalizeRatings
import Model_Trainer

numcourses = load_data.numcourses
courseslist = load_data.course_list
numfeatures = load_data.numfeatures

#Initialize the rating for every course as zero for the new user
new_user = np.zeros((1,load_data.Y.shape[1]))

# Testing
#Take ratings for some questions
for i in range(0,numcourses/3):
    ind = random.randint(0,numcourses-1)
    new_user[0][ind] = random.randint(1,5)

print new_user
for i, rating in enumerate(new_user[0]):
    if rating > 0:
        print('Rated {:.0f} for {:s}\n'.format(rating, courseslist[i]))

print new_user.shape
print load_data.Y.shape


load_data.Y = np.vstack((load_data.Y, new_user))
load_data.R = np.vstack((load_data.R, (new_user != 0).astype(int)))

# Normalize data and get test data
[load_data.Y, Y_Mean, load_data.test_data_Y, load_data.test_data_R, load_data.R] = normalizeRatings.normalizeRatings(load_data.Y,load_data.R,0.40)

load_data.numstudents = load_data.Y.shape[0]

print "Training our model: \n Please keep patience \n"
print Y_Mean
print load_data.Y
# TODO: append a column containing 1 to theta at the end for constant factor
print Model_Trainer.output
output = Model_Trainer.output[-1,:] + Y_Mean.flatten()

outputarg = output.argsort()[::-1]

for i in xrange(numcourses):
    j = outputarg[i]
    print('Predicting rating {:.5f} for course {:s}'.format(output[j], courseslist[j]))

# Compute error

testDataY = load_data.test_data_Y
testDataR = load_data.test_data_R
print "Starting error computation "
print testDataY
print testDataR

error = np.power(output*testDataR - testDataY,2)

print error
total_error = np.sum(error)
print total_error
numTestInstances = np.sum(testDataR)
print numTestInstances
averageSqError = total_error/numTestInstances
print averageSqError
standaverageError = pow(averageSqError,0.5)
print standaverageError
