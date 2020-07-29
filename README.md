# ros_for_beginners_one
ros for beginners: basics, motion, and opencv

//////////////////////// ROS PACKAGES ////////////////////////////////////////////////

Inside ros packages we have our nodes.
a package usually is one repo in github

to make a package

cd catkin_ws/src then type
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]

the go back to catkin_ws cd catkin_ws
catkin build

the package.xml and CMakeList will need some modifications whenever you start building nodes.

//////////////////////// ROS PACKAGES //////////////////////////////////////////////////


///////////////////////// ROS NODES/////////////////////////////////////////////////

creating a ros c++ node requires a bit more work than a python node.
Must be sure that your packaage.xml has the dependencies and that CMakeList.txt has the executables and other changes need that may be needed

In Ros, nodes are uniquely named. if two nodes with the same name are launched, the previous one is kicked off.
In nodes written in pyton the anonymous=True flag means that rospy will choose a unique name for our the node so that multiple of the node can run simultaneously in case you wanted to run a couple of the same node.(LOOK INTO C++ DOCUMENTATION AND COMPARE)

////////////////////////////ROS NODES///////////////////////////////////////////////////
