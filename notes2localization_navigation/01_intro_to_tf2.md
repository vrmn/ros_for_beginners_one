install demo

$ sudo apt-get install ros-$ROS_DISTRO-turtle-tf2 ros-$ROS_DISTRO-tf2-tools ros-$ROS_DISTRO-tf

run demo

$ roslaunch turtle_tf2 turtle_tf2_demo.launch

/////////////////////////////////////////////////////////////////////////////

What is Happening

This demo is using the tf2 library to create three coordinate frames: a world frame, a turtle1 frame, and a turtle2 frame. This tutorial uses a tf2 broadcaster to publish the turtle coordinate frames and a tf2 listener to compute the difference in the turtle frames and move one turtle to follow the other

we can use tf tools to see what tf2 is doing behind the scenes

$ rosrun tf2_tools view_frames.py
$ evince frames.pdf

Here we can see the three frames that are broadcast by tf2 the world, turtle1, and turtle2 and that world is the parent of the turtle1 and turtle2 frames. view_frames also report some diagnostic information about when the oldest and most recent frame transforms were received and how fast the tf2 frame is published to tf2 for debugging purposes.
////////////////////////////////////////////////////////////////

Using tf_echo

tf_echo reports the transform between any two frames broadcast over ROS.

Usage: rosrun tf tf_echo [reference_frame] [target_frame]

At time 1596576884.211
- Translation: [0.000, 0.000, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.163, 0.987]
            in RPY (radian) [0.000, -0.000, 0.327]
            in RPY (degree) [0.000, -0.000, 18.727]


////////////////////////////

rviz and tf2

rviz is a visualization tool that is useful for examining tf2 frames. Let's look at our turtle frames using rviz. Let's start rviz with the turtle_tf2 configuration file using the -d option for rviz:

$ rosrun rviz rviz -d `rospack find turtle_tf2`/rviz/turtle_rviz.rviz


/////////////////

follow up

http://wiki.ros.org/tf2/Tutorials/Using%20stamped%20datatypes%20with%20tf2%3A%3AMessageFilter
