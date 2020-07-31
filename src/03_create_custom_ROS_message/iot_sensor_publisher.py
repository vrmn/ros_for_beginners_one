#!/usr/bin/env python
# license removed for brevity
# compare to talker.py

import rospy
# from package_name.folder_message_is_in  (this is a module)
from ros_for_beginners_one.msg import iot_sensor # this imports the iot_sensor.msg in msg folder
import random

# create a new publisher. Specify the topic name, then type of messae then the queue size
pub = rospy.Publisher('iot_sensor_topic', iot_sensor, queue_size=10)

# we need to initialize the node. Give the pub node a nameself.
# the name is what will go in the rospy.Subscriber
rospy.init_node('iot_sensor_publisher_node', anonymous=True)

#set the loop rate
rate = rospy.Rate(1) # 1hz i message per second

#keep publishing until Ctrl-c is pressed
i = 0
while not rospy.is_shutdown():
    # look at message in msg file to see how to assign and write
    iot_sensory = iot_sensor()
    iot_sensory.id = 1
    iot_sensory.name="iot_parking_01"
    iot_sensory.temperature = 24.33 + (random.random()*2)
    iot_sensory.humidity = 33.41 + (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(iot_sensory)
    pub.publish(iot_sensory)
    rate.sleep()
    i = i + 1
