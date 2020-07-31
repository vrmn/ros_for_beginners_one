#!/usr/bin/env python

import rospy
# from package_name.folder_message_is_in (this is a module)
from ros_for_beginners_one.msg import iot_sensor # this imports the iot_sensor.msg in msg folder
import random

def iot_sensor_callback(iot_sensor_message):
    rospy.loginfo("new IoT data received: (%d, %s, %.2f, %.2f)",
        iot_sensor_message.id,
        iot_sensor_message.name,
        iot_sensor_message.temperature,
        iot_sensor_message.humidity)

rospy.init_node('iot_sensor_subscriber_node', anonymous=True)

rospy.Subscriber("iot_sensor_topic", iot_sensor, iot_sensor_callback)

# .spin() keeps python from exititng unitl this node is stopped.
rospy.spin()
