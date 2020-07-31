#include "ros/ros.h"
#include "ros_for_beginners_one/AddTwoints.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y"):
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<ros_for_beginners_one::AddTwoints>("add_two_ints")


}
