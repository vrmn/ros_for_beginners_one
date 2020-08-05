#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

# this is an object that will make the transformation between ros image format to opencv image format
bridge = CvBridge()

def image_callback(ros_image):
    print 'got an image'
    global bridge

    # convert ros_image into an oppencv_compatible image
    try:
        # this uses the object to convert to ros_image into an opencv_image
        cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    except CvBridgeError as e:
        print(e)

    # from here below you can work exactly as you wood with opencv the only difference is not being able to use while loops

    (rows,cols,channels) = cv_image.shape
    if cols > 200 and rows > 200:
        cv2.circle(cv_image, (100,100),90,255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_image, 'Webcam Activated with ROS & OpenCV', (10, 350), font, 1, (255,255,255),2,cv2.LINE_AA)
    cv2.imshow("image window", cv_image)
    cv2.waitKey(3)

def main(args):

    # initiliaze subcriber node
    rospy.init_node('image_converter', anonymous=True)

    # exampole rostopics to enter
    #image_topic = "/camera/rgb/image_raw/compoerssed"
    # for usb camer  image_topic ="/usb_cam/image_raw"
    # "topic" , message_type, function_to_execute
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
