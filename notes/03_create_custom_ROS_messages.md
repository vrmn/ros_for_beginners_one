wiki.ros.org/msg

so far we have been dealing with already defined messages

like std_msgs and, String, geometry_msgs, ect


/////////////////////////////////////////////////////////////
///////////////////////////THE STRUCTUTE OF THE ROS MESSAGE////////////////////////////

typically a message is defined by two things
1) the package name where it belonds
2) and its proper name

example:
- package_name/message_type
- std_msgs/String
- geometry_msgs/Twist


In additon every last message as some content whihc is defined by the type of field  and also a filed that will
have a value with respect to its tyye

type1 field1
type2 field2

For example the string message contains one filed of type String and its names is data

std_msgs/String
type=>string field=> data

Another example is the twist messages
it has two attributes linear and angular type vectors coposes of 3 float values (x y z)




///////////////////////////THE STRUCTUTE OF THE ROS MESSAGE////////////////////////////
/////////////////////////////////////////////////////////////////

////////////////////////  MAKING A NEW ROS MESSAGE //////////////////////////////////////////

example practice: assume that we have a sensor node attached to ros and provides 4 values

1) id: int
2) name: String
3) temperature: double
4) humidity: double

such a message is not defined in ros
thus we must define it and create a custom message that be used to publish these values in ROS ecosystem
also create a subscriber that can listen to these values and process them.


STEPS
1) create a msg folder in your package
2) in it create the message file with extension ".msg"
3) edit the .msg file by addint the elements (one per line)
4) update the dependencies in package.xml and CMakeList.txt (this goes for python and c++)
- make sure when making a custom message that in package.xml you include
-  <build_depend>message_generation</build_depend> as well as
-  <exec_depend>message_runtime</exec_depend>
* make sure when making a custom message that in CMakeList.txt
* under find_package(you add actionlib_msgs)
* make sure add_message_files(FILES <message_name>.msg is in there) and doesnt have #
* under generate_messages(DEPENDENCIES std_msgs actionli_msgs <- these are included)  
* also that catkin_package( has in it   CATKIN_DEPENDS roscpp rospy std_msgs message_runtime )


5) compile the package using caktin build or catkin_make
6) make sure the message is created using rosmsg show <name of .msg>

REFER TO iot_sensor_publisher.py and iot_sensor_subscriber.py to see how to use the custom message

////////////////
