#!/usr/bin/env python

import sys
import rospy
from ros_for_beginners_one.srv import AddTwoints
from ros_for_beginners_one.srv import AddTwointsRequest
from ros_for_beginners_one.srv import AddTwointsResponse

# this is responsbile for formulating the request and sending the request to the server
# an
def add_two_ints_client(x, y):
    # this starts by first waiting for the service
    rospy.wait_for_service('add_two_ints')
    try:
        # the .ServiceProx is responsible for sending the requst to the service and specifying the type of the service (AddTwoints)
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoints)
        # the add_two_ints object is going to take as input x and y

        #this method will be responsbile for connecting to the service, sending the request by sending the values of x and y
        # and then wating for the response to come when the response comes.
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# when the x and y value arguemetns are entered in the rosrun command line this below will hold and print them
def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    # this below will read x and y values from the arguments of the rosrun command line
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s + %s"%(x, y)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
    # the add_two_ints_client method will be executed. This is responsible for formulating the request and sending the request
    # and seding the request to the server
