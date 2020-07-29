#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)
    # This declares that your node subscribes to the chatter topic which is of type std_msgs.msgs.String.
     # When new messages are received, callback is invoked with the message as the first argument. 

    rospy.spin()


if __name__ == '__main__':
    listener()
