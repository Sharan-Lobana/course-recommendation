import numpy as np

# Load the list of courses
# TODO: modify the semester to point to correct semester in courses.txt
def loadcoursesList():
    with open("courses.txt") as course_file:
        course_list = []

        for i,course in enumerate(course_file.readlines()):
            course_detail  = course.split()[1:]
            semester = course_detail[-1]
            course_id = course_detail[-2]
            course_name = course_detail[:-2]
            course_list.append([course_id," ".join(course_name),semester])
    return course_list

def loadData():
    with open("electrical.csv") as rated:
        rating_list = []
        rated_list = []
        theta_list = []
        for i,rate in enumerate(rated.readlines()):
            # Skip the header row
            if(i == 0):
                continue
            temp = rate.split(',')

            rating = temp[2:31]
            rating = [int(i) if i is not '' else 0 for i in rating]
            rating_list.append(rating)

            rated = [1 if i is not 0 else 0 for i in rating]
            rated_list.append(rated)

            theta_params = temp[31:]
            local_theta = [int(x) if x is not '' else 0 for x in theta_params]
            theta_list.append(local_theta)
    return rating_list,rated_list,theta_list

course_list = loadcoursesList()

# Y and R are students*courses
data = loadData()
Y = np.asarray(data[0])   #Contains values
R = np.asarray(data[1]) #Contains rated boolean vals
Theta = np.asarray(data[2])

test_data_Y = None
test_data_R = None

numstudents = Y.shape[0]
numparams = Theta.shape[1]
numcourses = len(course_list)
numfeatures = numparams

X = np.random.rand(numcourses, numfeatures)

#Debug
print "NumStudents: "+str(numstudents)
print "NumFeatures: "+str(numfeatures)
print "NumCourses: "+str(numcourses)
