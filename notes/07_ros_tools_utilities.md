how to configure a user workstation with robot machine

so for htis two work imagine you have two machines. Machine1 is the user workstation and Machine2 is the bot

so for both of them you want to open the .bashrc

at the bottom of machine2 .bashrc you want to add
#ROBOT MACHINE CONFIGURATION
export ROS_MASTER_URI=http://localhost:11311  #THIS IS DEFaul tpaort
#The IP address for the Master Node
export ROS_HOSTNAME=192.168.8.101
export ROS_IP=192.168.8.101

echo "ROS_HOSTNAME: "$ROS_HOSTNAME
echo "ROS_IP: "$ROS_IP
echo "ROS_MASTER_URI: "$ROS_MASTER_URI

to find the ip address of the robot go to terminal and type (ifconfig)
the ip address will be found in a line that says inet addr: 192.168.8.101  this is what will go into the ros hostname and ROS_IP

at the bottom of machine1 .bashrc you want to addr
#WORKSTATION CONFIGURATION
export ROS_IP=192.168.8.106  ip address for workstation ifconfig
export ROS_HOSTNAME=192.168.1.106  ip addrss for workstation ifconfig
export ROS_MASTER_URI=http://192.168.8.101:11311 #herer we need to specify the correct master uri this will be the ip address of machine2

to testif configured probperly

on machine2 in a terminal run rosrun turtlesim turtlesim_node
then type rostopic list

on machine1 type rostpic list as well and you should see the exact same topics
have furn on machine1 the workstation tyupe rosrun turtlesim turtle_teleop_key


////////////////////////////////////////////////////
running multiple nodes with launch files

What is a launch file?

A launch file is XML document, which specifies:
  1) which nodes to execute
  2) their parameters
  3) what other launch files to include

Roslaunch is a program that easiliy launches multiple ROS nodes

Launch file has a .launch extension

refer to launch file examples

///////////////////////////////

launch files and parametsfr
