import numpy as np

def loadcoursesList():

    with open("dummycourses.txt") as course_file:
        course_list = []

        for i,course in enumerate(course_file.readlines()):
            course_detail  = course.split()[1:]
            semester = course_detail[-1]
            course_id = course_detail[-2]
            course_name = course_detail[:-2]
            course_list.append([course_id," ".join(course_name),semester])
        print course_list
    return course_list

def loadRatedList():
    with open("rated.csv") as rated:
        rated_list = []
        for i,rate in enumerate(rated.readlines()):
            temp = rate.split(',')
            temp = [int(x) for x in temp]
            rated_list.append(temp)
        print rated_list
    return rated_list

def loadRatingValueList():
    with open("ratingvalues.csv") as rated:
        rating_list = []
        for i,rate in enumerate(rated.readlines()):
            temp = rate.split(',')
            temp = [int(x) for x in temp]
            rating_list.append(temp)
        print rating_list
    return rating_list

def loadThetaList():
    with open("userTheta.csv") as theta:
        theta_list = []
        for i,theta in enumerate(theta.readlines()):
            temp = theta.split(',')
            temp = [int(x) for x in temp]
            theta_list.append(temp)
        print theta_list
    return theta_list

#Debug
course_list = loadcoursesList()
Y = np.asarray(loadRatingValueList())
R = np.asarray(loadRatedList())
Theta = np.asarray(loadThetaList())

numstudents = Y.shape[0]
numparams = Theta.shape[1]
numcourses = len(course_list)
numfeatures = numparams

X = np.random.rand(numcourses, numfeatures)

print numstudents
print numfeatures
print numcourses
