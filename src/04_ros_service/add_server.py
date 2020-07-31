#!/usr/bin/env python

from ros_for_beginners_one.srv import AddTwoints
from ros_for_beginners_one.srv import AddTwointsRequest
from ros_for_beginners_one.srv import AddTwointsResponse
# the above is referring the folder inside the include folder that is inside the workspaces devel folder

import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))  # this is kind of like the print("Returning [{} + {} = {}]".format(a, b, a+b))

    # we then  send the response to the client client using this statement.
    return AddTwointsResponse(req.a + req.b)


def add_two_ints_server():
    # initialize the node
    rospy.init_node('add_two_ints_server')

    # start service listening to incoming request
    # rospy.Service is going to create a server that will be listening to incoming request
    # rospy.Service('name_of_service', message_type, hanlde_function_for_the_server)
    # this handle functio will be executed anytime there is a new request coming. This is like a new thread that is going to execute when a nrew request arrives from the server
    s = rospy.Service('add_two_ints', AddTwoints, handle_add_two_ints)
    print "Ready to add two ints"
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
