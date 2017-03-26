import load_data
import Model_Trainer
import math




def check_accuracy():
    total = 0   # total trials
    correct = 0 #sucessful trials
    for i in range(load_data.numstudents):
        for j in range(load_data.numcourses):
            if load_data.R[j, i] == 1:
                if math.fabs(load_data.Y[j, i] - Model_Trainer.output[j, i]) < 1.0:
                    correct = correct + 1
                total = total + 1

    print "Result is %d / %d" % (correct, total) # check accuracy
    accuracy = 100 * (float(correct) / total)
    print  " Accuracy : {0} '%'".format(accuracy)

    return accuracy

check_accuracy()
