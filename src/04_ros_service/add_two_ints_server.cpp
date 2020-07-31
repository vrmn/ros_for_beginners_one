#include "ros/ros.h"
#include "ros_for_beginners_one/AddTwoints.h"

// this is why we include #include "ros_for_beginners_one/AddTwoints.h"
// this is similar to the handle method in the python version of this
//  this add method is going to have 2 parameters
//  one parameter that specifies the request
// and one parameter that specifies the response
// so when the server receives a request it is gong to execute the method we extrac information a and be from the request (req)
bool add(ros_for_beginners_one::AddTwoints::Request &req,
          ros_for_beginners_one::AddTwoints::Response &res)
          {
            res.sum = req.a + req.b;
            ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
            ROS_INFO("sending back response: [%ld]", (long int)res.sum);
            return true;
          }

int main(int argc, char **argv)
{

  // initialize the node
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHangle n;

  // define service server
  // n.advertiseService("service_name", define_method_that_will_handle_incoming_request)
  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}
