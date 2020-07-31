#include "ros/ros.h"
#include "std_msgs/String.h"

// Topic messages callback
// this only takes one parameter which is (msgs)
// (ConstPtr&) is a pointer for the message
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  //  initiate a new ros node named "listener"
  ros::init(argc, argv, "listener");

  // create a node handle: it is reference assigned to a new node
  ros::NodeHandle node;  //you can give this any name

  // Subscribe to a given topic, in this case "chatter"
  //chatter callback is the name of the callback funciton that will be executed each time a message is received
  ros::Subscriber sub = node.subscribe("chatter", 1000, chatterCallback); //(<name of topic>, <buffer size>, <fucntion which is a callback)

  // enter a lopp, pumping callbacks
  ros::spin();

  return 0;

}
