first install opencv for ros melodic

sudo apt-get install ros-melodic-opencv3


sudo apt-get install ros-melodic-usb-cam

sudo apt-get install ros-melodic-image-view

opencv open/save image files (python)

/////////////// ///////////////////////////////////////////////////////////////////////////////////////
CVBRIDGE

we will be receving images from ros topics

thus a subscriber needs to be created in ros  in order to receive the image and then sending the image for further processing

however the image fromat in ros is different from the mage format in opencv so we need to covert the image back and forth
this is where cvbridge comes in


[opencv cv::Mat] <>       [CvBridge]  <> [ROS Image message]


to test and see
 rosrun usb_cam usb_cam_node _pixel_format:yuyv
rosrun image_view image_view image:=/usb_cam/image_raw
