#include "ros/ros.h"
#include "std_msgs/String.h"
/*
when building a c++ node and you #inlcude std_msgs/String.h you must make sure of 4 additional things outside of this script

1) in CMakeList.txt make sure that std_msgs is in
find_package(catkin REQUIRED COMPONENTS
      roscpp
      rospy
       std_msgs
     )

2) Furthermore in CMakeList.txt check that its onlso in the dependecies like below
# INCLUDE DIRS include
# LIBRARIES
CATKIN_DEPENDS roscpp rospy std_msgs

3) exectable is declared in CMakeList.txt as well

add_executable(talker src/talker.cpp)
target_link_libraries (talker ${catkin_LIBRARIES})
add_dependencies(talker )

4) Furthermore in the package.xml make sure that <build_depend>std_msgs</build_depend> and <run_depend>std_msgs</run_depend>
are included.
     */
#include <sstream>

int main(int argc, char **argv)
{

  // Initialize new ros node name "talker"
  ros::init(argc, argv, "talker");

  // Create a node handle, this represents a reference assinged to a new node
  // every node that you create must have a reference
  ros::NodeHandle n;

  // create a publisher with a topic "chatter" that will send a string message
  // we use the ros publisher class -->(ros::Publisher) to create a publisher object named(chatter_publisher)
  // then we use the node handle n that was created above (ros::NodeHandle n;) then use the method advertise (n.advertise)
  // which allows to advertise a new topic named ("chatter") and the message type is (std_msgs::String)
  // followed by the buffer size (1000) how many messages can be actually accumulated before being processed.
  ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter", 1000);


  // at this point nothing is being published yet. the steps above just allow the node to connect/register to the ros master

  // rate is a class that is used to define frequency for a loop. 1 message per second
  ros::Rate loop_rate(1.0);


// time to make an endless loop
  int count = 0;
  while (ros::ok()) // keep spinning loop unitl user presses Ctrl+C
  {
    //create a new string ros message
    //message definition in this  link http://docs.ros.org/api/std_msgs/html/msg/String.html
    std_msgs::String msg;

    //create a string for the data
    std::stringstream ss;
    ss << "hello world " << count;

    // assign the string data to ROS message that was created (std_msgs::String msg)
    msg.data = ss.str();

    //print the conent of the message in the terminal
    ROS_INFO("[Talker ] I published %s\n", msg.data.c_str());

    //publish the message. this is where the message will be published
    chatter_publisher.publish(msg);

    //
    ros::spinOnce(); // Need to call this function often to allow ROS to process incoming messages

    loop_rate.sleep(); // sleep for the rest of the cycle. to enforce the loop rate
    count++;



  }
return 0;

}




/* Now before this can be built so that it could be run some modification need to be done to CMakeLists.txt in src.
  Or else compilation will not happen.
  You must declare a cpp executable, which looks like this

  add_executable(talker src/talker.cpp)
  target_link_libraries (talker ${cakin_LIBRARIES})
  add_dependencies(talker beginner_tutorials_generate_message_cpp)



*/
