#!/usr/bin/env python
# the above makes sure that the script is executed as a python script

import rospy
# You need to import rospy if you are writing a ROS Node.

from std_msgs.msg import String
# The std_msgs.msg import is so that we can reuse the std_msgs/String message
# type (a simple string container) for publishing.

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # pub = rospy.Publisher("chatter", String, queue_size=10) declares
    # that your node is publishing to the chatter topic using the message type String.
     # String here is actually the class std_msgs.msg.String.

    rospy.init_node('talker', anonymous=True)
    # The next line, rospy.init_node(NAME, ...), is very important as it tells rospy
     # the name of your node -- until rospy has this information, it cannot start communicating with the ROS Master.
      # In this case, your node will take on the name talker.
       # NOTE: the name must be a base name, i.e. it cannot contain any slashes "/".
       # anonymous = True ensures that your node has a unique name by adding random numbers to the end of NAME.


    rate = rospy.Rate(10)
    # This line creates a Rate object rate. With the help of its method sleep(),
     # it offers a convenient way for looping at the desired rate.
      # With its argument of 10, we should expect to go through the loop
      # 10 times per second (as long as our processing time does not exceed 1/10th of a second!)

    while not rospy.is_shutdown(): # this is the equivalent to ros::ok
    # This loop is a fairly standard rospy construct: checking the rospy.is_shutdown() flag and then doing work.
     # You have to check is_shutdown() to check if your program should exit (e.g. if there is a Ctrl-C or otherwise

        hello_str = "hello world %s" % rospy.get_time()

        rospy.loginfo(hello_str)
        # This loop also calls rospy.loginfo(str), which performs triple-duty:
         # the messages get printed to screen, it gets written to the Node's log file, and it gets written to rosout.

        pub.publish(hello_str)
        # In this case, the "work" is a call to pub.publish(hello_str) that publishes a string to our chatter topic.
        rate.sleep()
        #  The loop calls rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop.


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

# catkin_install_python(PROGRAMS scripts/talker.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )
